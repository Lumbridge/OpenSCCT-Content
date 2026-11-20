"""Regression checks for the public source-only catalogue policy."""

import copy
import json
import unittest
from pathlib import Path

from check_community import check_catalog


class CommunityPolicyTests(unittest.TestCase):
    def setUp(self):
        path = Path(__file__).resolve().parents[1] / "community.json"
        self.catalog = json.loads(path.read_text(encoding="utf8"))

    def rejects(self, change):
        catalog = copy.deepcopy(self.catalog)
        change(catalog)
        with self.assertRaises(ValueError):
            check_catalog(catalog)

    def test_no_retail_or_preconverted_payloads(self):
        self.rejects(lambda doc: doc["maps"][0].update(full={"url": "https://example.org/map.zip"}))
        self.rejects(lambda doc: doc.update(shared=[{"id": "core"}]))
        self.rejects(lambda doc: doc["maps"][0].update(code="AQU03", id="community/AQU03"))

    def test_sources_are_pinned_and_confined(self):
        self.rejects(lambda doc: doc["maps"][0]["steamRecipe"].update(commit="main"))
        self.rejects(lambda doc: doc["maps"][0]["steamRecipe"]["files"][0].update(path="community/../Packages/Maps/a.sdc"))
        self.rejects(lambda doc: doc["maps"][0]["steamRecipe"]["files"][0].update(destination="System/_PC_/Engine.u"))
        self.rejects(lambda doc: doc["maps"][0]["steamRecipe"].update(evidence="https://example.org/map"))
