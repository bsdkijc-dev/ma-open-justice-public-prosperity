# Six-Project Dependency Map

```
[P01: Indonesia Open Justice] ──(D01 Courts, D02 Case Stats, D03 Decisions)──┐
[P02: Justice for UMKM]       ──(D10 UMKM Disputes, D08 Costs, D05)──────────┤
[P03: Justice for Rural]      ──(D06 Geo Access, D07 Legal Aid, D12 Rural)───┼──> [Integration Layer (D01-D16)]
[P04: Labour Justice (PHI)]   ──(D11 Labour Disputes, D03, D08)──────────────┤         │
[P05: People's Legal Knowl.]  ──(D04 Legal Sources, D09 Plain-Lang Guides)───┘         v
                                                                              [Analytical Modules 01-08]
[P06: Justice for Last Mile]  ──(D14 Interventions, D15 Public Value) <───────┘         │
       (NOT STARTED - Upstream Consumer & Evaluation Feedback)                          v
                                                                              [Policy Intelligence & Public Value]
```

## Cross-Project Dependencies
- **P01 -> P02, P03, P04:** Provides canonical court identifiers (`D01`) and baseline judicial statistics (`D02`).
- **P05 -> P02, P03, P04, P06:** Provides verified legal source register (`D04`) and plain-language knowledge items (`D09`).
- **P03 -> P06:** Rural geographic & OBH legal-aid gap baselines (`D06`, `D07`, `D12`) inform Last Mile intervention targeting.
- **P02 & P04 -> P06:** UMKM and worker cost/remedy barriers (`D08`, `D10`, `D11`) inform practical intervention design.
- **P06 -> Integration Layer:** Currently `BLOCKED` / `NOT STARTED`; `D14` (Intervention records) and `D15` (Public value outcomes) rely on `P5` synthetic schemas until P06 is launched.
