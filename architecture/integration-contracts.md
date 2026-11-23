# Integration Contracts

Projects expose approved datasets to the integration layer via read-only contracts. Original project repositories are **never** copied or overwritten.

| Project ID | Repo Status | Approved Integration Inputs (SAFE MODE) | Pending / Blocked Inputs |
|---|---|---|---|
| `P01` | Local + GitHub | `data/synthetic/*.csv`, `data/processed/*.parquet` (after license/P1 verification) | Full `Laptah` CSVs on Kaggle (`judicialcollege/indonesia-open-justice-observatory-2024-2025`) |
| `P02` | Local + GitHub | `data/public/ds05_umkm_economic_indicators.csv` (278 rows), `ds09_legal_information_register.csv` (11 rows), `data/synthetic/` (`P5`) | `ds01` empirical `putusan3` exports (awaiting manual upload) |
| `P03` | Local + GitHub | `data/approved-public/*.json` (9 `P1` files: BPS, Kemendesa, DS02 63 courts, DS05 55 OBH for NTB `52` & Jabar `32`) | 8 legacy court addresses `pending_verification`; national expansion beyond pilot |
| `P04` | Local + GitHub | `data/public/phi_synthetic_release_candidate.csv` (150 `P5` rows) | Empirical PHI crawling on `putusan3` paused (`max_retries_exceeded`) |
| `P05` | Local + GitHub | `data/interim/dataset_01..12` (14 legal sources, 14 provisions, 10 articles, etc.) — `PENDING_HUMAN_REVIEW` | Human legal & accessibility sign-off before promotion to `P1` |
| `P06` | `NOT STARTED` | None (no repository or dataset exists yet) | Full project initialization required |
