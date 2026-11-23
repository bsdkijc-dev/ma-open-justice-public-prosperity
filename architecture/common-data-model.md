# Common Data Model (D01–D16)

## 16 Core Data Domains
- `D01` — Institutional information
- `D02` — Judicial case statistics
- `D03` — Judicial decision metadata
- `D04` — Legal source metadata
- `D05` — Access-to-justice indicators
- `D06` — Geographic accessibility
- `D07` — Legal aid availability
- `D08` — Justice affordability
- `D09` — Legal knowledge accessibility
- `D10` — UMKM legal disputes
- `D11` — Labour disputes
- `D12` — Rural justice indicators
- `D13` — Vulnerable population access barriers
- `D14` — Intervention and evaluation records
- `D15` — Public value and outcome indicators
- `D16` — Data provenance and quality

## Mandatory Variable Attributes (18 Fields)
`variable_id`, `variable_name`, `definition`, `unit`, `data_type`, `allowed_values`, `numerator`, `denominator`, `observation_period`, `geographic_level`, `source_reference`, `collection_method`, `transformation_method`, `missing_data_rule`, `quality_status`, `limitations`, `project_owner`, `approval_status`.

## Standards & Missing-Value Semantics
- **Dates:** ISO 8601 (`YYYY-MM-DD` or `YYYY` / `YYYY-QN`)
- **Country Codes:** ISO 3166-1 alpha-2 (`ID`)
- **Indonesian Admin Codes:** Official BPS/Kemendagri codes where verified (e.g., `32` Jawa Barat, `52` NTB)
- **Explicit Missingness Distinction (Never treat missing as zero):**
  `zero` | `unknown` | `unavailable` | `not_applicable` | `suppressed` | `not_collected`
