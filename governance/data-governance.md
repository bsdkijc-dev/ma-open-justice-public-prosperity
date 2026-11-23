# Data Governance & Publication Classes

## Shared Publication Classes
- **P1** — Public and approved for redistribution.
- **P2** — Public source, reuse conditions require review.
- **P3** — Internal working material.
- **P4** — Restricted or sensitive.
- **P5** — Synthetic test data.

## Core Rules
- Each project maintains its own source and approval records.
- The integration layer may only consume datasets whose reuse is explicitly authorized.
- Never assume public availability equals permission for bulk republication.
- Never overwrite original project datasets; reference approved source datasets via integration contracts.
- Never combine incompatible datasets simply to produce a larger national dataset.
- No mass crawling or access-control circumvention.
