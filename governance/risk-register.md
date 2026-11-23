# Integration Risk Register

| Risk ID | Category | Description | Likelihood | Impact | Mitigation |
|---|---|---|---|---|---|
| R01 | Institutional | Misinterpretation as official Mahkamah Agung RI program | Medium | High | Mandatory disclaimer (`governance/independence-disclaimer.md`), Gate 7 & 8 |
| R02 | Legal/Copyright | Unauthorized bulk republication of `P2` public sources | Medium | High | Strict `P1`–`P5` gating; only `P1`/`P5` in integration pipeline |
| R03 | Methodological | Merging incompatible populations/timeframes (e.g., synthetic vs. empirical) | High | High | Mandatory `observation_period` & `publication_class` checks; zero-imputation |
| R04 | Missing Project | Project 06 (`Justice for the Last Mile`) not yet initialized | High | Medium | Register as `NOT STARTED`; exclude from empirical integration until created |
| R05 | Privacy | Accidental PII leakage from court decisions or survey records | Low | Critical | Automated PII regex/field checks + Gate 2 & 10 |
| R06 | Source Access | `putusan3.mahkamahagung.go.id` rate-limiting / HTTP retries (observed in P04) | High | Medium | Respect `robots.txt` (`crawl_delay=3.0s`), pause automated crawling, manual verification |
