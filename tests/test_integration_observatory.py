import json
import re
import unittest
from pathlib import Path
import jsonschema

ROOT = Path(__file__).resolve().parent.parent


class TestObservatoryIntegration(unittest.TestCase):
    def _load_json(self, rel):
        return json.loads((ROOT / rel).read_text(encoding="utf-8"))

    def test_required_governance_and_architecture_files_exist(self):
        required = [
            "README.md", "LICENSE", "CITATION.cff", "CONTRIBUTING.md", "CHANGELOG.md",
            "governance/program-charter.md", "governance/integration-governance.md",
            "governance/data-governance.md", "governance/privacy-policy.md",
            "governance/publication-policy.md", "governance/research-ethics.md",
            "governance/risk-register.md", "governance/independence-disclaimer.md",
            "architecture/system-architecture.md", "architecture/common-data-model.md",
            "architecture/interoperability.md", "architecture/source-provenance.md",
            "architecture/integration-contracts.md", "architecture/project-dependency-map.md",
            "reports/integration-feasibility-report.md",
        ]
        for rel in required:
            self.assertTrue((ROOT / rel).is_file(), f"Missing required file: {rel}")

    def test_project_registry_validates_and_has_six_projects(self):
        schema = self._load_json("shared/schemas/project_registry.schema.json")
        registry = self._load_json("projects/project-registry.json")
        self.assertEqual(len(registry), 6)
        ids = {r["project_id"] for r in registry}
        self.assertEqual(ids, {"P01", "P02", "P03", "P04", "P05", "P06"})
        for entry in registry:
            jsonschema.validate(instance=entry, schema=schema)

    def test_common_data_dictionary_covers_all_16_domains(self):
        schema = self._load_json("shared/schemas/common_variable.schema.json")
        dd = self._load_json("shared/data-dictionary/common_data_dictionary.json")
        domains = {row["domain_id"] for row in dd}
        expected = {f"D{i:02d}" for i in range(1, 17)}
        self.assertEqual(domains, expected)
        for row in dd:
            jsonschema.validate(instance=row, schema=schema)

    def test_indicator_framework_covers_all_5_families(self):
        schema = self._load_json("shared/schemas/indicator_framework.schema.json")
        indicators = self._load_json("shared/indicators/indicator_framework.json")
        families = {ind["family"] for ind in indicators}
        self.assertEqual(
            families,
            {"TRANSPARENCY", "ACCESSIBILITY", "AFFORDABILITY", "EFFECTIVENESS", "PUBLIC_VALUE"},
        )
        for ind in indicators:
            jsonschema.validate(instance=ind, schema=schema)
            self.assertFalse(ind["comparability_validated"])

    def test_synthetic_integrated_records_schema_and_missingness_rules(self):
        schema = self._load_json("shared/schemas/integrated_record.schema.json")
        records = self._load_json("data/synthetic/synthetic_integrated_records.json")
        self.assertGreaterEqual(len(records), 10)
        for rec in records:
            jsonschema.validate(instance=rec, schema=schema)
            self.assertEqual(rec["publication_class"], "P5")
            self.assertEqual(rec["data_origin"], "synthetic")
            if rec["missing_value_status"] in {"unknown", "unavailable", "not_applicable", "suppressed", "not_collected"}:
                self.assertIsNone(rec["indicator_value"], "Missing value must never be encoded as 0")
            if rec["missing_value_status"] == "zero":
                self.assertEqual(rec["indicator_value"], 0.0)

    def test_provenance_policy_and_public_value_schemas(self):
        prov_schema = self._load_json("shared/schemas/provenance_record.schema.json")
        for r in self._load_json("data/synthetic/synthetic_provenance.json"):
            jsonschema.validate(instance=r, schema=prov_schema)

        pol_schema = self._load_json("shared/schemas/policy_recommendation.schema.json")
        for r in self._load_json("data/synthetic/synthetic_policy_proposals.json"):
            jsonschema.validate(instance=r, schema=pol_schema)
            self.assertEqual(r["review_status"], "PENDING_HUMAN_REVIEW")

        pv_schema = self._load_json("shared/schemas/public_value_evaluation.schema.json")
        for r in self._load_json("data/synthetic/synthetic_public_value_eval.json"):
            jsonschema.validate(instance=r, schema=pv_schema)
            self.assertFalse(r["causal_claim_permitted"])

    def test_no_pii_in_synthetic_data(self):
        text = (ROOT / "data/synthetic/synthetic_integrated_records.json").read_text(encoding="utf-8")
        # Check for 16-digit Indonesian NIK or email addresses
        self.assertIsNone(re.search(r"\b\d{16}\b", text))
        self.assertIsNone(re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text))


if __name__ == "__main__":
    unittest.main()
