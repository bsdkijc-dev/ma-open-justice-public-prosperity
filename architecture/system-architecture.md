# System Architecture

## Low-Cost Reproducible Stack
- **Core Engine:** Python 3.11+, `pandas`, `DuckDB` (analytical SQL over Parquet/CSV), `jsonschema`
- **Version Control & CI:** Git, GitHub, GitHub Actions
- **Dataset Distribution (Gated):** Kaggle (private datasets during SAFE MODE)
- **Optional Extensions (Phase 2+):** Neo4j (legal/institutional/policy graphs), Qdrant (verified source-grounded RAG), static dashboard/website

## Layered Architecture
1. **Source Project Layer (Autonomous):** Six independent repositories (`P01`–`P06`) retaining full ownership and raw data.
2. **Integration Contract Layer:** Read-only metadata & approved dataset interfaces (`P1` and `P5` only in SAFE MODE).
3. **Common Data Model & Validation Layer:** Shared data dictionary (D01–D16), JSON schemas, missing-value semantics, PII checks.
4. **Cross-Project Analytics Layer:** Modules 01–08 investigating transparency, accessibility, affordability, effectiveness, and public value.
5. **Policy Intelligence & Public Value Layer:** Structured policy register (`P1`–`P5`) and 5-dimension evaluation framework.
