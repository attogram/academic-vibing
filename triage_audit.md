# Project Triage Audit (June 2026)

This audit applies the Epistemic Triage skill (v1.0) to the current repository state to separate canonical research from exploratory narrative.

## 1. [PAPER] - Target: arXiv cs.AI / cs.HC
These artifacts are meant for external publication and must remain free of "mythology" leakage.

| Artifact | Description | Status |
| :--- | :--- | :--- |
| `papers/academic-vibing/v0.8/` | Latest stable draft of the core methodology. | ACTIVE |
| `CLAIMS.md` (1-15, 17-18) | Methodological and operational claims. | STABLE |
| `scripts/calculate_cdi.py` | Implementation of the Consensus Divergence Index. | VERIFIED |
| `CITATIONS.md` | Master bibliography for the research corpus. | STABLE |
| `skills/arxiv/` | Procedures for preprint submission. | STABLE |

## 2. [OUTLET] - Target: Culture & Generative Layer
These artifacts are used for creative exploration and cognitive throughput. They are allowed to be "fun" but must not contaminate the paper.

| Artifact | Description | Status |
| :--- | :--- | :--- |
| `podcasts/` | Audio volumes 1-3 and mascot assets. | ACTIVE |
| `SOUNDTRACK.md` | Acoustic context metadata. | ACTIVE |
| `podcasts/mascot/` | ROCK the puppy and "Rock Talk" dialect. | NARRATIVE |
| `issues/` (Most) | Narrative state ledger and conversational history. | PERSISTENT |
| `TRIAGE.md` | High-level workstream management (contains meta-mythology). | OPERATIONAL |

## 3. [NEEDS VERIFICATION] - Target: Empirical Testing
Claims that look like PAPER but lack formal "receipts" or measurement.

| Artifact | Claim / Issue | Blocker |
| :--- | :--- | :--- |
| `CLAIMS.md` #16 | Leapfrog Effect (Well-being increase). | Needs longitudinal n=2 data. |
| `CLAIMS.md` #19 | Re-entry Cost Reduction (23m -> 3m). | Needs formal timing test. |
| Issue #120 | Voice transcription environmental noise. | Needs controlled measurement. |
| `podcasts/cdi_audit_claims.json` | High friction result (0.8000). | Needs peer replication. |

## 4. [TOO RAW] - Target: Internal Buffer
Premature ideas requiring more iteration.

| Artifact | Description | Risk |
| :--- | :--- | :--- |
| Phase L issues | Endorsement gate procedures. | Admin/Bureaucratic drift. |
| "Cosmic Shame" | Aesthetic critiques of the process. | Purely expressive. |

---
**Triage Rule Applied:** Nothing from Section 2 or 4 is allowed into Section 1 without formal re-derivation.
