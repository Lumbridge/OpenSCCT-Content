"""Publisher index compatibility checks; run with python -m unittest discover -s tools -p test_occ.py."""
import contextlib
import importlib.util
import io
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('occ', Path(__file__).with_name('occ.py'))
occ = importlib.util.module_from_spec(spec)
spec.loader.exec_module(occ)


def map_row(code, version):
    return {'id': 'stock/' + code, 'code': code, 'title': code, 'category': 'stock', 'version': '1.0.1',
            'modes': ['Story'], 'contentHash': 'a' * 16, 'manifestSha256': 'b' * 64,
            'treeSha256': 'c' * 64, 'requires': [], 'source': {'kind': 'install'}, 'generator': 'test',
            'svmapFormatVersion': version,
            'full': {'file': code + '.zip', 'size': 1, 'sha256': 'd' * 64},
            'sim': {'file': code + '-sim.zip', 'size': 1, 'sha256': 'e' * 64}}


class IndexFormatTests(unittest.TestCase):
    def build(self, versions, previous='1.1'):
        index = {'svmapFormat': previous, 'shared': [], 'maps': []}
        plan = {'shared': [], 'maps': [map_row(str(i), version) for i, version in enumerate(versions)]}
        return occ.build_index(index, plan, 'content-test')

    def test_compatible_minor_versions_share_the_index(self):
        result = self.build(['1.1.0', '1.2.0'])
        self.assertEqual('1.2', result['svmapFormat'])
        self.assertEqual(2, len(result['maps']))

    def test_patch_versions_keep_the_major_minor_format(self):
        self.assertEqual('1.1', self.build(['1.1.0', '1.1.1'])['svmapFormat'])

    def test_shared_only_publish_preserves_the_format(self):
        self.assertEqual('1.2', self.build([], previous='1.2')['svmapFormat'])

    def test_partial_publish_does_not_lower_existing_minor(self):
        self.assertEqual('1.2', self.build(['1.1.0'], previous='1.2')['svmapFormat'])

    def test_incompatible_major_versions_are_refused(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            self.build(['1.2.0', '2.0.0'])

    def test_navigation_publish_keeps_map_downloads_and_rejects_stale_map(self):
        old = self.build(['1.2.0'])
        original = old['maps'][0]
        nav = {'id': original['id'], 'simHash': 'a' * 64, 'manifestSha256': 'b' * 64,
               'formatVersion': 13, 'activationMask': 0,
               'archive': {'file': 'navigation.zip', 'size': 2, 'sha256': 'f' * 64}}
        plan = {'maps': [], 'shared': [], 'botNavigation': [nav]}
        published = occ.build_index(old, plan, 'content-nav')['maps'][0]
        self.assertEqual(original, {k: v for k, v in published.items() if k != 'botNavigation'})
        self.assertEqual('a' * 64, published['botNavigation']['simHash'])
        self.assertTrue(published['botNavigation']['download']['url'].endswith('/content-nav/navigation.zip'))
        nav['manifestSha256'] = 'e' * 64
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            occ.build_index(old, plan, 'content-nav')


if __name__ == '__main__':
    unittest.main()
