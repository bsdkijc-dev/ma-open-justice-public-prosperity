# Empirical Analytical Modules 01–08 Summary (P1 Only)

**Data Hygiene Guard:** Verified `publication_tier == 'P1'` and `is_synthetic == False`. All `P5` synthetic datasets (`P04`, `P06`, `P02 DS01`) were strictly excluded.

## 1. P03 Pilot Courts (`ds02_pilot_courts_ntb_jabar.json`)
|   province_code |   court_count |   pending_addr |
|----------------:|--------------:|---------------:|
|              32 |            49 |              6 |
|              52 |            14 |              2 |

## 2. P03 BPHN Accredited OBH (`ds05_pilot_obh_ntb_jabar.json`, n=55)
| accreditation_grade_displayed   |   obh_count |
|:--------------------------------|------------:|
| C                               |          32 |
| B                               |          18 |
| A                               |           5 |

## 3. P02 UMKM Economic Indicators in Pilot Provinces (`ds05_umkm_economic_indicators.csv`, total n=278)
| province            |   indicator_rows |
|:--------------------|-----------------:|
| Jawa Barat          |                7 |
| Nusa Tenggara Barat |                7 |

## 4. P02 Legal Register & P05 Approved Legal Knowledge Snapshot (`P1`)
- **P02 DS09 Verified Regulations:** 11
- **P05 Approved Legal Sources:** 14
- **P05 Approved Legal Provisions:** 11 (excluded 3 flagged provisions)
- **P05 Approved Knowledge Articles / Guides / Audio-Visual:** 10 / 4 / 4

## 5. Module Status (Days 31–45)
- **Modules 01–03, 05, 07, 08:** Empirical `P1` descriptive baselines executed (`COMPLETED`).
- **Module 04 (Labour Justice):** `P1` legal source audit completed; empirical PHI case analysis `BLOCKED` (`P04` crawler paused; `P5` synthetic separated).
- **Module 06 (Last Mile Interventions):** `P1` geographic/OBH baseline targeting completed; empirical intervention outcomes `NOT_STARTED` (`P06` pilot pending).
