from __future__ import annotations

import copy
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))

import update_checksum
from keymap_format import FACTORY_EXPORT, ROOT, keymap_md5, load_json, validate_export


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

    def test_export_version_is_compared_to_factory_baseline(self) -> None:
        baseline = copy.deepcopy(self.factory)
        candidate = copy.deepcopy(self.factory)
        baseline["version"] = "fixture-version"
        candidate["version"] = "fixture-version"
        self.assertEqual(validate_export(candidate, baseline), [])

        candidate["version"] = "different-version"
        errors = validate_export(candidate, baseline)
        self.assertTrue(any("must match factory export version" in error for error in errors))

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

    def test_generated_sha256_manifests_match_all_json(self) -> None:
        generated_roots = (ROOT / "exports/windows-wow", ROOT / "exports/experiments")
        listed_files: set[Path] = set()
        for root in generated_roots:
            for manifest in root.rglob("SHA256SUMS"):
                for line_number, line in enumerate(
                    manifest.read_text(encoding="utf-8").splitlines(), start=1
                ):
                    if not line.strip():
                        continue
                    parts = line.split(maxsplit=1)
                    self.assertEqual(
                        len(parts),
                        2,
                        f"Malformed entry in {manifest}:{line_number}",
                    )
                    expected_hash, filename = parts
                    artifact = manifest.parent / filename
                    self.assertTrue(artifact.is_file(), f"Missing artifact: {artifact}")
                    actual_hash = hashlib.sha256(artifact.read_bytes()).hexdigest()
                    self.assertEqual(
                        actual_hash,
                        expected_hash.lower(),
                        f"Stale SHA-256 in {manifest}:{line_number}",
                    )
                    listed_files.add(artifact.resolve())

        generated_json = {
            path.resolve()
            for root in generated_roots
            for path in root.rglob("*.json")
        }
        self.assertEqual(generated_json, listed_files)


if __name__ == "__main__":
    unittest.main()