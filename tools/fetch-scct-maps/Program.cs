using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Text.Json;
using System.Threading;
using System.Threading.Tasks;
using OpenScct.Maps;

// fetch-scct-maps <catalog.json> <commit> [--root <maps root>] [--game <Versus install>] [--local <SCCT-Maps checkout>]
//                 [--cache <release asset cache>] [--ids id,id] [--skip id,id]
//
// Writes the SCCT-Maps catalogue at <commit> (as OpenSCCT's launcher reads it) to <catalog.json>. With --root, downloads
// the maps into <root>/game (laid out like an install, with the stock asset packs and every imported package, exactly
// as the launcher's Maps download does) and records them in <root>/installed.json. --local serves repository files from
// a checkout at the same commit; --cache keeps release assets between runs. Maps whose codes the install has are
// skipped (the install's copy is the one a build uses).
if (args.Length < 2)
{
    Console.Error.WriteLine("usage: fetch-scct-maps <catalog.json> <commit> [--root dir] [--game dir] [--local dir] [--cache dir] [--ids a,b] [--skip a,b]");
    return 2;
}

string? Arg(string name)
{
    int i = Array.IndexOf(args, name);
    return i >= 0 && i + 1 < args.Length ? args[i + 1] : null;
}

using var http = new HttpClient(new LocalFirstHandler(Arg("--local"), Arg("--cache"))) { Timeout = TimeSpan.FromMinutes(30) };
var repo = new MapRepository(http);
MapIndex index = await repo.FetchCatalogAsync(CancellationToken.None, args[1]);
var dump = index.Maps.Select(m => new { m.Id, m.Name, m.Category, m.Version, m.Game, m.Commit, m.NotesPath, m.Codes, m.Files }).ToList();
File.WriteAllText(args[0], JsonSerializer.Serialize(new { index.Commit, Maps = dump }, new JsonSerializerOptions { WriteIndented = true }));
Console.WriteLine($"catalog {index.Commit}: {index.Maps.Count} maps, {index.Packages.Count} pool packages");

string? root = Arg("--root");
if (root is null)
{
    return 0;
}

string? game = Arg("--game");
HashSet<string>? ids = Arg("--ids")?.Split(',').ToHashSet();
var skip = Arg("--skip")?.Split(',').ToHashSet() ?? [];
var library = new MapLibrary(root);
var report = new List<object>();
foreach (MapPackage m in index.Maps)
{
    if ((ids is not null && !ids.Contains(m.Id)) || skip.Contains(m.Id))
    {
        continue;
    }

    IReadOnlyList<string> inInstall = MapLibrary.CodesInInstall(m, game);
    if (inInstall.Count > 0)
    {
        Console.WriteLine($"skip {m.Id}: the install has {string.Join(",", inInstall)}");
        report.Add(new { m.Id, ok = false, error = "in the install" });
        continue;
    }

    try
    {
        MapInstallResult r = await library.InstallAsync(m, repo, null, CancellationToken.None, index, game);
        Console.WriteLine($"ok   {m.Id} [{string.Join(",", m.Codes)}] added={r.Added.Count} missing={string.Join(",", r.Missing)}");
        report.Add(new { m.Id, ok = true, r.Added, r.Missing });
    }
    catch (Exception ex) when (ex is IOException or HttpRequestException or InvalidDataException or TaskCanceledException)
    {
        Console.WriteLine($"FAIL {m.Id}: {ex.Message}");
        report.Add(new { m.Id, ok = false, error = ex.Message });
    }
}

File.WriteAllText(Path.Combine(root, "fetch-report.json"), JsonSerializer.Serialize(report, new JsonSerializerOptions { WriteIndented = true }));
return 0;

/// <summary>
/// Serves raw.githubusercontent.com/Lumbridge/SCCT-Maps/&lt;commit&gt;/&lt;path&gt; from a local checkout when it has the
/// file, and release downloads from (and into) a cache folder. MapRepository still checks every file's hash.
/// </summary>
sealed class LocalFirstHandler(string? checkout, string? cache) : DelegatingHandler(new HttpClientHandler())
{
    private const string RawPrefix = "https://raw.githubusercontent.com/Lumbridge/SCCT-Maps/";
    private const string ReleasePrefix = "https://github.com/Lumbridge/SCCT-Maps/releases/download/";

    protected override async Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancel)
    {
        string url = request.RequestUri!.AbsoluteUri;
        if (checkout is not null && url.StartsWith(RawPrefix, StringComparison.Ordinal))
        {
            string rest = url[RawPrefix.Length..];
            string rel = Uri.UnescapeDataString(rest[(rest.IndexOf('/') + 1)..]);
            string local = Path.Combine(checkout, rel.Replace('/', Path.DirectorySeparatorChar));
            if (!rel.Contains("..", StringComparison.Ordinal) && File.Exists(local))
            {
                return FileResponse(local);
            }
        }

        if (cache is not null && url.StartsWith(ReleasePrefix, StringComparison.Ordinal))
        {
            string rel = Uri.UnescapeDataString(url[ReleasePrefix.Length..]);
            string cached = Path.Combine(cache, rel.Replace('/', Path.DirectorySeparatorChar));
            if (!rel.Contains("..", StringComparison.Ordinal))
            {
                if (!File.Exists(cached))
                {
                    using HttpResponseMessage live = await base.SendAsync(request, cancel).ConfigureAwait(false);
                    live.EnsureSuccessStatusCode();
                    Directory.CreateDirectory(Path.GetDirectoryName(cached)!);
                    string part = cached + ".part";
                    await using (var output = File.Create(part))
                    {
                        await live.Content.CopyToAsync(output, cancel).ConfigureAwait(false);
                    }

                    File.Move(part, cached, overwrite: true);
                }

                return FileResponse(cached);
            }
        }

        return await base.SendAsync(request, cancel).ConfigureAwait(false);
    }

    private static HttpResponseMessage FileResponse(string path) => new(HttpStatusCode.OK)
    {
        Content = new StreamContent(File.OpenRead(path)),
    };
}
