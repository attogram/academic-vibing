# Skill: Epistemic Triage (v1.1)

## ROCK
Context: Sorting cognitive artifacts to prevent epistemic contamination.
Goal: Separate exploratory "vibing" from publishable research claims.
Method: Route every artifact into one of four buckets: PAPER, OUTLET, NEEDS VERIFICATION, TOO RAW.
Rule: No leakage from OUTLET to PAPER without re-derivation.
**Constraint: Total synchronization. Exact copies. No compression. No placeholders.**

## PROSE

### 0. The Source of Truth Rule
The GitHub Issues are the absolute source of truth. Any local archive (`issues/`) must be an **exact, uncompressed, full-thread replica** of the corresponding GitHub issue, including the original body and all comments.
- **NEVER** use placeholders (e.g., "[Placeholder for issue body]").
- **NEVER** summarize the issue content in the local version.
- **NEVER** omit comments.
- **EXACT** copy-paste from the source is the only acceptable method.

### 1. The Decision Procedure
Classify **every single issue** and artifact into exactly one category. Selective triage is a failure state.

- **[PAPER]**:
  - Claims meant to survive external scrutiny (e.g., arXiv, peer review).
  - High-density, falsifiable, and structurally sound.
  - Must stand alone without the "mythology" layer.
  - *Heuristic:* "If I delete everything fun, does the idea still stand?"

- **[OUTLET]**:
  - Non-verifiable, expressive, or internal-context material (e.g., memes, podcasts, mascots).
  - Maximizes cognitive throughput and creative exploration.
  - Allows contradiction and aesthetic drift.
  - *Heuristic:* "Does this produce interesting structure without constraints?"

- **[NEEDS VERIFICATION]**:
  - Claims that look like PAPER but lack empirical "receipts."
  - Held in a buffer until CDI or measurement (e.g., Leapfrog timings) is completed.

- **[TOO RAW]**:
  - Premature or under-formed ideas.
  - Fragile insights requiring more internal iteration before routing.

### 2. Failure Modes (Epistemic Contamination & Lossy Archiving)
Triage exists to prevent these specific risks:
1. **Context Leakage**: Mascot logic or in-group shorthand entering the canonical paper.
2. **Premature Formalization**: "Math-ifying" ideas that haven't been empirically grounded.
3. **Consensus Trap**: Treating multi-agent agreement as "truth" without external verification.
4. **Lossy Sync**: Summarizing or using placeholders for GitHub issues, which destroys the audit trail and researcher context.

### 3. The Coupling Constraint
**Nothing from OUTLET becomes part of PAPER unless it is re-derived under PAPER rules.**

It is not promoted. It is not copied. It is *re-derived*. This ensures that the paper's logic is independent of the generative "vibe" that produced the insight.

### 4. Implementation
- **Comprehensive Audit:** Check **every single f****** issue** every single time triage is performed.
- **Zero Placeholders:** Identify and overwrite any existing placeholders or summaries with full content.
- **Categorization:** Tag every issue in `TRIAGE.md` or `triage_audit.md` with its bucket.
- **Validation:** Use `grep` to verify no placeholders remain in the archive.
