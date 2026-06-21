# Skill: Epistemic Triage (v1.0)

## ROCK
Context: Sorting cognitive artifacts to prevent epistemic contamination.
Goal: Separate exploratory "vibing" from publishable research claims.
Method: Route every artifact into one of four buckets: PAPER, OUTLET, NEEDS VERIFICATION, TOO RAW.
Rule: No leakage from OUTLET to PAPER without re-derivation.

## PROSE

### 1. The Decision Procedure
Classify every incoming artifact, claim, or document into exactly one category:

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

### 2. Failure Modes (Epistemic Contamination)
Triage exists to prevent these specific risks:
1. **Context Leakage**: Mascot logic or in-group shorthand (e.g., "ROCK", "KIT") entering the canonical paper.
2. **Premature Formalization**: "Math-ifying" ideas that haven't been empirically grounded.
3. **Consensus Trap**: Treating multi-agent agreement as "truth" without external verification.
4. **Overfitting**: Building systems that only make sense within the repo's own narrative.

### 3. The Coupling Constraint
**Nothing from OUTLET becomes part of PAPER unless it is re-derived under PAPER rules.**

It is not promoted. It is not copied. It is *re-derived*. This ensures that the paper's logic is independent of the generative "vibe" that produced the insight.

### 4. Implementation
- Tag issues and files with the corresponding category.
- Use `triage_audit.md` to track the state of the repository.
- Prioritize moving [NEEDS VERIFICATION] items to [PAPER] via empirical testing.
