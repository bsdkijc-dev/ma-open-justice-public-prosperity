# Phase 2 Integration Feasibility Report (SAFE MODE)

**Date:** 2026-11-23  
**Scope:** Inspection of existing project repositories (`P01`–`P06`), dataset inventory, ownership/permissions, variable compatibility mapping, gaps/conflicts, and integration feasibility.

## 1. Inspected Repositories & Actual Datasets Found

1. **P01 — Indonesia Open Justice Observatory (`indonesia-open-justice-observatory`)**
   - *Local Path:* `/working_dir/c_9f0ef59312a8a465/indonesia-open-justice-observatory`
   - *Code License:* MIT
   - *Actual Datasets Found:* `data/processed/` (`ds01_institutions.parquet`, `ds02_case_statistics.parquet`, `ds03_judgment_publication.parquet`, `jurisdiction_summary.csv` [4 rows], `data_quality_report.json`) + `data/synthetic/` (`ds01`–`ds08` in CSV/JSON). *Note:* Memory also records 2024–2025 Laptah CSVs uploaded to private Kaggle (`judicialcollege/indonesia-open-justice-observatory-2024-2025`), not stored in local `data/processed/` as CSV.
2. **P02 — Justice for UMKM Observatory (`justice-for-umkm-observatory`)**
   - *Local Path:* `/working_dir/c_2e8d03db2e69f7be/justice-for-umkm-observatory` (Git `4bc561b`, `origin` `bsdkijc-dev/justice-for-umkm-observatory`)
   - *Code License:* MIT
   - *Actual Datasets Found:* Empirical `P1` in `data/public/` & `data/processed/`: `ds05_umkm_economic_indicators.csv` (278 rows, 98.5 KB) and `ds09_legal_information_register.csv` (11 rows); plus `data/synthetic/` (`ds01`–`ds10` in CSV/Parquet, including 120 synthetic dispute rows and 100 synthetic survey rows).
3. **P03 — Justice for Rural Communities Observatory (`justice-for-rural-communities-observatory`)**
   - *Local Path:* `/working_dir/c_83187fa987a40d2e/justice-for-rural-communities-observatory`
   - *Code License:* MIT
   - *Actual Datasets Found:* 9 `P1` JSON files in `data/approved-public/` (BPS 2014–2018 baseline, PODES 2024–2025, 2025 ICT/digital, 2025–2026 poverty/HDI, 2025 transport vehicles; Kemendesa Indeks Desa 2025; `ds02_pilot_courts_ntb_jabar.json` [63 courts]; `ds05_pilot_obh_ntb_jabar.json` [55 OBH]) + 44 raw BPS CSVs in `data/raw/bps/` + 12 synthetic JSONs (`ds01`–`ds12`).
4. **P04 — Indonesia Labour Justice Observatory (`indonesia-labour-justice-observatory`)**
   - *Local Path:* `/working_dir/c_da47cce57e1f6832/indonesia-labour-justice-observatory`
   - *Code License:* MIT
   - *Actual Datasets Found:* `data/public/phi_synthetic_release_candidate.csv` (150 `P5` rows), `data/synthetic/phi_synthetic_pilot.csv` (154 rows), `data/processed/phi_pilot_validated.parquet`, and pipeline audit logs (`pipeline_summary.json`, `privacy_report.json`). Live `putusan3` PHI crawling is paused (`max_retries_exceeded`).
5. **P05 — People's Legal Knowledge Observatory (`peoples-legal-knowledge-observatory`)**
   - *Local Path:* `/working_dir/c_63d12d3880bbb2c8/peoples-legal-knowledge-observatory` (Git `74e5ccf`, `origin` `bsdkijc-dev/peoples-legal-knowledge-observatory`)
   - *Code License:* MIT
   - *Actual Datasets Found:* `data/interim/dataset_01..12.json` (14 legal sources, 14 provisions, 10 knowledge articles, 10 questions, 10 answers, 4 procedure guides, 10 terminology items, 4 audio-visual scripts, 6 literacy items, 0 feedback items, 4 legal updates, 10 provenance records) — all marked `PENDING_HUMAN_REVIEW`; plus 12 synthetic JSONs in `data/synthetic/`.
6. **P06 — Justice for the Last Mile**
   - *Status:* `NOT_STARTED` — No repository, schemas, or datasets found in workspace, memory, or Google Drive.

## 2. Compatible Variable Mapping Across Inspected Projects

| Common Variable | Projects Sharing Concept | Local Field Names Observed | Compatibility Status |
|---|---|---|---|
| `institution_id` / `court_name` | `P01`, `P02`, `P03`, `P04` | `institution_id`, `court_id`, `court_name` | **Partial** — `P01` uses `institution_id`/`court_id`; `P02`/`P04` use `court_name` text strings without canonical `MA-COURT-*` IDs. |
| `province` / `district` | `P01`, `P02`, `P03` | `province`, `district`, BPS codes `32`/`52` | **Partial** — `P03` uses BPS 2-digit codes (`32`, `52`) in `P1` JSONs; `P01`/`P02` use province/district names. |
| `legal_source_id` / `regulation_number` | `P01`, `P02`, `P05` | `regulation_id` (`P01`), `legal_source_id` (`P02`), `source_id` (`P05`) | **Compatible with mapping** — requires ID crosswalk and `P05` human review sign-off. |
| `reporting_period` / `observation_period` | `P01`, `P02`, `P03`, `P04` | `reporting_period`, `observation_period`, `decision_date` | **Compatible** — aligns to ISO 8601 (`2024`–`2026`), but `P01` is 2024–2025 while `P02`/`P03` span 2014–2026. |
| `validation_status` / `review_status` | `P01`, `P02`, `P03`, `P04`, `P05` | `validation_status`, `review_status`, `approval_status` | **Compatible** — maps cleanly to Common Data Model `approval_status`. |

## 3. Gaps & Conflicts Identified

1. **Missing Project (`P06`):** Zero empirical or synthetic intervention/evaluation datasets (`D14`) exist because `Justice for the Last Mile` has not been created.
2. **Empirical vs. Synthetic Asymmetry:** `P04` (PHI labour disputes) and `P02` (`ds01` UMKM court disputes, `ds07` survey) currently have **only `P5` synthetic** case/survey data locally; combining them with `P01`/`P02`/`P03` `P1` empirical datasets is strictly prohibited.
3. **Geographic Scope Mismatch:** `P03` empirical `P1` court (`63`) and OBH (`55`) datasets cover only two pilot provinces (`52` NTB and `32` Jawa Barat), whereas `P01` and `P02` `DS05` cover broader national/multi-province scopes.
4. **Approval Gate Hold (`P05`):** All 12 `P05` `data/interim/` datasets are `PENDING_HUMAN_REVIEW` and cannot be promoted to `P1` integration inputs without human legal and accessibility sign-off.
5. **Source Access Bottleneck (`P04` & `P02`):** `putusan3.mahkamahagung.go.id` returned `max_retries_exceeded` in `P04` crawler tests; `P02` empirical `ds01` awaits manual judgment exports.
6. **Legacy Address Verification (`P03`):** 8 legacy court addresses in `P03` `ds02_pilot_courts_ntb_jabar.json` are flagged `pending_verification`.

## 4. Feasibility Verdict (SAFE MODE)

- **Metadata & Schema Integration:** **FEASIBLE NOW** — All 5 existing projects use MIT-licensed schemas/code and compatible domain concepts (`D01`–`D16`).
- **Empirical Cross-Project Integration:** **PARTIALLY FEASIBLE (GATED)** — Empirical `P1` integration is currently feasible only for `P02` (`DS05`, `DS09`) + `P03` (BPS/Kemendesa/DS02/DS05 in NTB `52` & Jawa Barat `32`) + `P01` (once Laptah CSVs are linked via integration contract), subject to Human Approval Gates 1, 4, and 10.
- **Full 6-Project Empirical Integration:** **BLOCKED** pending `P06` initialization, `P05` human legal review, `P04`/`P02` `putusan3` data acquisition, and `P01`–`P04` canonical `court_id` crosswalk.
