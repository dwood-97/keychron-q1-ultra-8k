from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))

import update_checksum
from keymap_format import FACTORY_EXPORT, keymap_md5, load_json, validate_export


class KeymapFormatTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.factory = load_json(FACTORY_EXPORT)

    def test_factory_keymap_digest_matches_export(self) -> None:
        self.assertEqual(keymap_md5(self.factory), "10cfb8ae547419ff0c5257e0b8a01bac")

    def test_stale_digest_is_rejected(self) -> None:
        candidate = copy.deepcopy(self.factory)
        candidate["keymap"][2][0]["val"] = 104
        errors = validate_export(candidate, self.factory)
        self.assertTrue(any("MD5 mismatch" in error for error in errors))

    def test_correct_digest_passes_schema_validation(self) -> None:
        candidate = copy.deepcopy(self.factory)
        candidate["keymap"][2][0]["val"] = 104
        candidate["MD5"] = keymap_md5(candidate)
        self.assertEqual(validate_export(candidate, self.factory), [])

    def test_duplicate_matrix_position_is_rejected(self) -> None:
        candidate = copy.deepcopy(self.factory)
        candidate["keymap"][2][1]["row"] = candidate["keymap"][2][0]["row"]
        candidate["keymap"][2][1]["col"] = candidate["keymap"][2][0]["col"]
        candidate["MD5"] = keymap_md5(candidate)
        errors = validate_export(candidate, self.factory)
        self.assertTrue(any("duplicate matrix positions" in error for error in errors))

    def test_mac_layer_changes_are_rejected(self) -> None:
        candidate = copy.deepcopy(self.factory)
        candidate["keymap"][0][0]["val"] = 4
        candidate["MD5"] = keymap_md5(candidate)
        errors = validate_export(candidate, self.factory)
        self.assertTrue(any("Mac layers" in error for error in errors))

    def test_caps_layer_requires_transparent_wasd(self) -> None:
        candidate = copy.deepcopy(self.factory)
        candidate["keymap"][2][45]["val"] = 21027
        candidate["MD5"] = keymap_md5(candidate)
        errors = validate_export(candidate, self.factory)
        self.assertTrue(any("requires W to be transparent" in error for error in errors))

    def test_malformed_layer_is_reported_without_crashing(self) -> None:
        candidate = copy.deepcopy(self.factory)
        candidate["keymap"][2][45]["val"] = 21027
        candidate["keymap"][3] = None
        candidate["MD5"] = keymap_md5(candidate)
        errors = validate_export(candidate, self.factory)
        self.assertTrue(any("layer 3 must be an array" in error for error in errors))

    def test_checksum_helper_updates_generated_file(self) -> None:
        candidate = copy.deepcopy(self.factory)
        candidate["keymap"][2][0]["val"] = 104
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(json.dumps(candidate), encoding="utf-8")
            self.assertTrue(update_checksum.update(path, check_only=False))
            updated = load_json(path)
        self.assertEqual(updated["MD5"], keymap_md5(updated))


if __name__ == "__main__":
    unittest.main()