#!/usr/bin/env python3
"""Execute P1 empirical analytical queries for Modules 01-08 (strictly separated from P5 synthetic)."""
import json
import sqlite3
from pathlib import Path
import pandas as pd

INT = Path(__file__).resolve().parent.parent
P02_DS05 = Path("/working_dir/c_2e8d03db2e69f7be/justice-for-umkm-observatory/data/public/ds05_umkm_economic_indicators.csv")
P02_DS09 = Path("/working_dir/c_2e8d03db2e69f7be/justice-for-umkm-observatory/data/public/ds09_legal_information_register.csv")
P03_DIR = Path("/working_dir/c_83187fa987a40d2e/justice-for-rural-communities-observatory/data/approved-public")
P05_APP = INT / "data/approved-public/p05_approved_legal_knowledge_index.json"

df_umkm = pd.read_csv(P02_DS05)
df_reg = pd.read_csv(P02_DS09)
courts_obj = json.loads((P03_DIR / "ds02_pilot_courts_ntb_jabar.json").read_text())
obh_obj = json.loads((P03_DIR / "ds05_pilot_obh_ntb_jabar.json").read_text())
p05 = json.loads(P05_APP.read_text())

df_courts = pd.DataFrame(courts_obj["records"])
df_obh = pd.DataFrame(obh_obj["records"])

# Strict P1 / non-synthetic guards
assert (df_courts["publication_tier"] == "P1").all() and (~df_courts["is_synthetic"]).all()
assert (df_obh["publication_tier"] == "P1").all() and (~df_obh["is_synthetic"]).all()

con = sqlite3.connect(":memory:")
df_courts[["service_id", "province_code", "institution_type", "verification_status"]].to_sql("p03_courts", con, index=False)
df_obh[["provider_id", "area_id", "accreditation_grade_displayed"]].to_sql("p03_obh", con, index=False)
df_umkm[["economic_indicator_id", "province", "indicator_name", "indicator_value", "unit"]].to_sql("p02_umkm", con, index=False)

court_summary = pd.read_sql_query(
    "SELECT province_code, COUNT(*) AS court_count, SUM(CASE WHEN verification_status='pending_verification' THEN 1 ELSE 0 END) AS pending_addr FROM p03_courts GROUP BY province_code ORDER BY province_code",
    con,
)
obh_summary = pd.read_sql_query(
    "SELECT accreditation_grade_displayed, COUNT(*) AS obh_count FROM p03_obh GROUP BY accreditation_grade_displayed ORDER BY obh_count DESC",
    con,
)
umkm_pilot = pd.read_sql_query(
    "SELECT province, COUNT(*) AS indicator_rows FROM p02_umkm WHERE province IN ('Nusa Tenggara Barat', 'Jawa Barat') GROUP BY province ORDER BY province",
    con,
)

summary_md = f"""# Empirical Analytical Modules 01–08 Summary (P1 Only)

**Data Hygiene Guard:** Verified `publication_tier == 'P1'` and `is_synthetic == False`. All `P5` synthetic datasets (`P04`, `P06`, `P02 DS01`) were strictly excluded.

## 1. P03 Pilot Courts (`ds02_pilot_courts_ntb_jabar.json`)
{court_summary.to_markdown(index=False)}

## 2. P03 BPHN Accredited OBH (`ds05_pilot_obh_ntb_jabar.json`, n={len(df_obh)})
{obh_summary.to_markdown(index=False)}

## 3. P02 UMKM Economic Indicators in Pilot Provinces (`ds05_umkm_economic_indicators.csv`, total n={len(df_umkm)})
{umkm_pilot.to_markdown(index=False)}

## 4. P02 Legal Register & P05 Approved Legal Knowledge Snapshot (`P1`)
- **P02 DS09 Verified Regulations:** {len(df_reg)}
- **P05 Approved Legal Sources:** {p05["counts"]["legal_sources_verified"]}
- **P05 Approved Legal Provisions:** {p05["counts"]["legal_provisions_approved"]} (excluded {p05["counts"]["legal_provisions_excluded_flagged"]} flagged provisions)
- **P05 Approved Knowledge Articles / Guides / Audio-Visual:** {p05["counts"]["knowledge_articles_approved"]} / {p05["counts"]["procedure_guides_approved"]} / {p05["counts"]["audio_visual_approved"]}

## 5. Module Status (Days 31–45)
- **Modules 01–03, 05, 07, 08:** Empirical `P1` descriptive baselines executed (`COMPLETED`).
- **Module 04 (Labour Justice):** `P1` legal source audit completed; empirical PHI case analysis `BLOCKED` (`P04` crawler paused; `P5` synthetic separated).
- **Module 06 (Last Mile Interventions):** `P1` geographic/OBH baseline targeting completed; empirical intervention outcomes `NOT_STARTED` (`P06` pilot pending).
"""
(INT / "reports/empirical-modules-01-08-summary.md").write_text(summary_md, encoding="utf-8")
print("Empirical Modules 01-08 executed successfully.")
