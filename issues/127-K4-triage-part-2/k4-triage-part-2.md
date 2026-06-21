# Issue #127: K4 triage part 2

Chatgpt

This issue (#122) is actually the first place in the whole system where something real and structurally meaningful emerges without relying on the mythology layer.

If we strip everything else away, here is what “J5 skills/triage/SKILL.md” actually is:

### What this is (clean read)
It is a routing mechanism for epistemic sorting. Not a philosophy. Not vibing. Not an ontology.

It is: A decision procedure that classifies incoming cognitive artifacts into:
- PAPER (claims meant to survive external scrutiny)
- OUTLET (non-verifiable, expressive, or internal-context material)
- NEEDS VERIFICATION (claims requiring evidence before promotion)
- TOO RAW (premature or under-formed ideas)

### What makes this different from the rest of the repo
This is the first artifact that:
1. Introduces an explicit boundary between: generation (ideas), selection (triage), publication (paper). That separation is actual systems design, not narrative.
2. Defines failure modes precisely: context leakage, premature formalization, consensus without verification, overfitting to internal coherence.
3. Implements a lightweight epistemic state machine: INPUT → TRIAGE → ROUTE → (PAPER | OUTLET | HOLD).

### Final grounding
“Triage is all you need” → much closer to a real system primitive. Because this file is not about expression or speed. It is about: preventing epistemic contamination between modes of thinking.
