# Interoperability Specification

- **Join Keys:** `province_code` (BPS 2-digit), `district_code` (BPS 4-digit), `court_id` / `institution_id`, `source_id`, `observation_period`.
- **Compatibility Guardrails:** Never join `P5` synthetic records with `P1` empirical records in analytical tables. Always tag `publication_class` and `data_origin` (`empirical` vs. `synthetic`).
