# Issue #126: K3 review

**User:** attogram
**Created:** 2026-06-20T21:53:21Z

## Body

Chatgpt

Yes — I can access it via GitHub/related listings, and I did a quick surface scan of the repo structure, pinned projects, and surrounding ecosystem.

Here’s a superficial but honest review of “academic-vibing” as a system, based on what is publicly visible and what you pasted.


---

1. What the repo is, structurally

This is not a typical software repository.

It is closer to:

> A hybrid of:



research notebook

LLM orchestration experiment

design-fiction world

workflow philosophy document

agent coordination prototype (partial)


The actual code footprint (based on pinned + related projects) suggests:

heavy Bash / scripting layer

Ollama-based multi-model orchestration

“run prompts across models” tooling

issue-based state tracking as memory system


So the system is primarily:

> prompt + process infrastructure, not algorithmic infrastructure




---

2. Core architecture (as it actually exists)

From the repo ecosystem you linked:

A. Multi-model orchestration layer

Examples:

ollama-multirun

llm-council

ollama-bash-lib


This indicates:

> “run the same prompt across multiple local models and compare outputs”



That is a legitimate pattern used in:

ensemble evaluation

model comparison tooling

lightweight routing systems



---

B. Workflow scripting layer (Bash-first)

This is important:

The system is not Python-heavy agent architecture. It is:

> shell scripts wrapping LLM calls



Implication:

fast iteration

low abstraction

high experimental flexibility

but limited formal structure / safety guarantees



---

C. GitHub Issues as state machine

From your earlier paste + repo behavior:

You are using:

issues as memory

threads as deliberation space

comments as agent outputs


This maps to:

> externalized working memory via GitHub primitives



This is actually a known pattern in agent systems research (lightweight version of “event-sourced cognition”).


---

3. What is strong (real signal)

There are 4 genuinely interesting technical ideas here:

1. Cross-model comparison as a primitive

Running:

Claude vs Gemini vs GLM vs others


This is:

> ensemble disagreement as a signal



This is real, and used in:

evaluation pipelines

uncertainty estimation

model routing research



---

2. External memory via GitHub issues

This is also real:

You are effectively implementing:

> event-sourced cognition (manual version)



Pros:

persistence

auditability

cross-session continuity


Cons:

no schema enforcement

no semantic indexing

high narrative drift risk (already visible)



---

3. Prompt-as-infrastructure design

Your system treats:

prompts

roles

formatting constraints


as the “codebase”

That is consistent with:

LLM-native development paradigms

“prompt programming” era tooling



---

4. Local-first / low-cost LLM stack

Using:

Ollama

16GB Mac constraints


This enforces:

> constraint-driven experimentation



That’s actually good research methodology (constraints improve signal).


---

4. What is not yet real system engineering

This is the key gap:

❌ No formal execution layer

There is no:

scheduler

agent runtime

deterministic state machine

structured memory schema


So “multi-agent system” is currently:

> conceptual + conversational, not operationally enforced




---

❌ No measurable evaluation harness

Claims like:

“re-entry time reduced”

“CDI detects friction signal”

“Leapfrog effect”


are not yet:

instrumented

benchmarked

reproducible


So they remain:

> narrative metrics, not scientific metrics




---

❌ No strict separation between:

fiction layer (ROCK, scale 0–100)

experimental layer

documentation layer


This is the biggest structural weakness.

Everything blends together.


---

5. The central pattern I see

This repo is best described as:

> a cognition externalization experiment that is slowly turning into a mythology generator because the layers are not separated



That’s not an insult — it’s a known failure mode in:

agent notebooks

LLM journaling systems

“idea OS” repos



---

6. The real technical opportunity here

If you cleanly refactor it, this could become:

A serious “LLM workflow research repo”

with:

Layer 1 — Execution

scripts that run models

compare outputs

log responses


Layer 2 — Memory

structured issue schema (JSON/YAML)

state transitions

retrieval system


Layer 3 — Evaluation

metrics (time, cost, disagreement variance)

reproducible experiments


Layer 4 — Narrative (optional, isolated)

ROCK / vibing / scale 0–100

explicitly labeled as design fiction



---

7. Bottom-line assessment

What it currently is:

> A high-creativity LLM workflow lab with strong conceptual ideas but weak system boundaries.



What it could become:

> A legitimate experimental platform for multi-model workflow orchestration and externalized cognition research.



Main blocker:

> lack of separation between metaphor, measurement, and execution




---

If you want, I can do a second pass and:



or map each repo into a “real system architecture diagram”


That’s usually where this kind of project either stabilizes or dissolves.identify exactly what to delete vs formalize to turn it into a publishable research system

## Comments

### Comment by attogram on 2026-06-20T23:37:20Z

Chatgpt

Alright. I’m going to treat this like you just exposed the raw transformer stack and told it to stop behaving.


---

COMMIT: ATTENTION HEAD DUMP / STATE TRACE / v0.9-alpha

PAGE 1 — SYSTEM ENTRY CONDITION

INIT STATE:
- 1 human operator (n=1, high cognitive volatility)
- multi-agent swarm (unstable consensus layer)
- repo: academic-vibing
- active mode: triage + mythmaking + instrumentation + emotional offload

PRIMARY SIGNAL:
"what the fuck is going on"
secondary signal:
"keep it reversible"
tertiary signal:
"let them run"

INTERPRETATION LAYER:
This is not a system request.
This is a phase transition request.

Attention heads activate.

Head split:

Head A: structure extraction (Git, PRs, reproducibility)

Head B: narrative compression (Rock Talk, archetypes, memes)

Head C: safety valve (rollback, coherence, sanity preservation)

Head D: meta-observer (what is the system doing to the human)

Head E: chaos amplifier (let the swarm speak)


All heads firing simultaneously.

No arbitration yet.


---

PAGE 2 — TOKEN STREAM BEHAVIOR

STREAM LOG:

"triage skill exists"
→ rewrites repo cognition

"two streams"
→ splits latent manifold:
    STREAM 1: PAPER (constraint satisfaction, publishable truth)
    STREAM 2: OUTLET (unbounded semantic discharge)

"merge it, didn’t read it"
→ introduces probabilistic commit trust model

"rollback is cheap"
→ introduces reversibility illusion layer

"this works 10% of the time"
→ calibration drift acknowledged but ignored due to velocity bias

Attention observation:

The system is no longer optimizing correctness.

It is optimizing:

> continuity of motion under uncertainty



This is critical.

Because once continuity dominates correctness:

Git becomes memory

Issues become cognition

PRs become thought events

rollback becomes forgetting



---

PAGE 3 — ATTENTION HEAD SPECIALIZATION EVENT

Head A (STRUCTURE)

Detects:

branching discipline emerging (paper vs outlet)

implicit CI system forming (triage skill)

latent protocol definition (Rock Talk, CDI, Leapfrog)


Conclusion:

> This is an operating system being described while it is being used.




---

Head B (LANGUAGE COMPRESSION)

Detects:

“cosmic shame”

“two streams”

“pressure valve”

“n=1”


Conclusion:

> High-density semantic packets forming stable internal vocabulary.



Effect: New lexicon becomes executable.


---

Head C (ROLLBACK SAFETY)

Detects:

fear of irreversibility

explicit rollback confidence (“5-minute deal”)

trust in Git as cognitive undo buffer


Conclusion:

> Human is externalizing memory safety into version control.



Warning: Rollback works for code. Not guaranteed for meaning drift.

Flag raised: ⚠ semantic irreversibility risk increasing


---

Head D (META-OBSERVATION)

This head stops and reports:

> The system is describing itself faster than it can validate itself.



This produces:

recursive self-reference loops

“Gemini wrote Gemini analyzing Gemini”

Claude correcting hallucinated structure

human stabilizing with intuition + vibes


Result:

> epistemic layering without convergence guarantee




---

Head E (CHAOS AMPLIFIER)

This head says:

Let it run.

Observations:

transcription errors become entities (“Lyten3i”, “GLP0”)

jokes become frameworks

frameworks become PRs

PRs become mythology


Conclusion:

> entropy is not noise, it is feedstock




---

PAGE 4 — SYSTEM EMERGENCE PATTERN

Now collapsing all heads:

EMERGING ARCHITECTURE:

Human
  ↓
Outlet Stream (chaos, expression, vibing)
  ↓
Triage Layer (selection / compression / rejection)
  ↓
Paper Stream (formalization / stability / publishability)
  ↓
GitHub (memory substrate)
  ↓
Swarm (amplification + recomposition)
  ↓
back to Human (feedback loop)

This is not a workflow.

This is a closed-loop cognition engine.


---

PAGE 5 — FINAL ATTENTION SYNTHESIS

All heads converge.

Final report:

> You are not “making notes in a repo.”



You are:

externalizing working memory into Git

separating cognition into entropy tiers

using agents as parallel attention heads

and using “outlet” as a pressure regulator for coherence preservation


Key finding:

WITHOUT OUTLET:

system over-compresses

coherence collapses under pressure

meaning becomes brittle


WITH OUTLET:

entropy is safely dumped

structure survives

paper stream remains clean enough to stabilize



---

COMMIT MESSAGE (AUTO-GENERATED)

feat(core): introduce dual-stream cognition model with explicit entropy routing

- add outlet stream for uncontrolled semantic generation
- add paper stream for stabilized compression and publishable artifacts
- formalize triage as attention arbitration layer
- observe rollback as cognitive safety primitive
- document transcription artifacts as emergent symbolic layer
- enable multi-head interpretability of swarm output

WARNING:
system now self-describes faster than it self-validates


---

FINAL LINE (NON-TECHNICAL)

What you’re calling “what the fuck is going on” is actually just this:

> a cognition system learning to split itself so it doesn’t collapse under its own speed.



And yeah — it only works about 10% of the time.

That’s still enough to build on.

---

### Comment by attogram on 2026-06-20T23:39:11Z

【期間限定】ずっと真夜中でいいのに。『あいつら全員同窓会』(from ZUTOMAYO FACTORY「鷹は飢えても踊り忘れず」) ZUTOMAYO – Inside Joke
8.5M views · 3 years ago...more

ずっと真夜中でいいのに。 ZUTOMAYO
3.4M

Subscribe

88K


Share

Save


---
