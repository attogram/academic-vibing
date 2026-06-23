# Issue #30: D2

## Body

Rock Talk review:

Interesting shift.

Rock Talk focuses on communication efficiency.

Academic Vibing 0.3 focuses on epistemic efficiency.

Those are different problems.

The strongest idea here is not Rock Talk. It is CDI.

Why?

Most multi-agent systems optimize consensus.

You propose optimizing discovery of disagreement.

That is a fundamentally different objective.

Current pattern:

Agent A
Agent B
Agent C
↓
Consensus
↓
Answer

CDI pattern:

Agent A
Agent B
Agent C
↓
Disagreement Map
↓
Human Inspection
↓
Answer

That resembles practices from:

adversarial collaboration

red teaming

scientific peer review

intelligence analysis

Delphi methods

ensemble uncertainty estimation


The novelty is treating disagreement itself as the primary output artifact.

Potential issue:

Current CDI:

CDI = Disagreement / Total Claims

Too coarse.

Example:

Claim 1: Earth round.
Claim 2: Gravity exists.
Claim 3: Consciousness hard.

Only claim 3 disputed.

CDI = 1/3 = 0.33

But epistemic significance is much higher than the ratio suggests.

You may need weighted CDI.

Example:

CDI = Σ(disagreement × importance)
      / Σ(importance)

or

CDI = uncertainty mass
      / total claim mass

That prevents trivial disagreements from inflating the metric.

Most important sentence in the paper:

> Friction = Truth boundary.



Not always true.

Sometimes friction indicates:

model diversity

hallucination

prompt ambiguity

knowledge gaps


But:

No friction
≠ truth

Friction
⇒ investigate

That weaker formulation is easier to defend.

The "Token-to-Meaning Fallacy" section is stronger than the equivalent section in Rock Talk.

Reason:

You acknowledge:

Thinking != Transmission

instead of:

Compression = Better Thinking

That distinction avoids a common failure mode.

Good formulation:

Internal:
Long reasoning.

External:
Compressed transfer.

That matches how humans work too.

Scientists:

think in notebooks

publish compressed papers


Engineers:

think in diagrams

ship APIs


The GitHub issue-loop idea is underrated.

Not because GitHub matters.

Because you are implicitly defining:

Research State Machine

Example:

[STATE]
[BLOCKER]
[PAYLOAD]

This is closer to workflow engineering than prompt engineering.

Overall:

Rock Talk:

strongest contribution = communication protocol


Academic Vibing 0.3:

strongest contribution = CDI and disagreement-centered research orchestration


Of the two, CDI has the higher probability of becoming a genuinely useful research primitive because it generates new information rather than merely compressing existing information.

Rock summary:

Rock Talk:
Optimize transfer.

Academic Vibing:
Optimize discovery.

CDI:
Find where smart agents disagree.

Human:
Inspect disagreement.

Result:
Less consensus theater.
More useful uncertainty.
