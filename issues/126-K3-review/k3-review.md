**URL:** https://github.com/attogram/academic-vibing/issues/126

# K3 review #126

**attogram** opened this issue on Jun 20, 2026

Chatgpt

Yes — I can access it via GitHub/related listings, and I did a quick surface scan of the repo structure, pinned projects, and surrounding ecosystem.

Here’s a superficial but honest review of “academic-vibing” as a system, based on what is publicly visible and what you pasted.

---

1. What the repo is, structurally

This is not a typical software repository.

It is closer to:

A hybrid of:
- research notebook
- LLM orchestration experiment
- design-fiction world
- workflow philosophy document
- agent coordination prototype (partial)

The actual code footprint (based on pinned + related projects) suggests:
- heavy Bash / scripting layer
- Ollama-based multi-model orchestration
- “run prompts across models” tooling
- issue-based state tracking as memory system

So the system is primarily:
- prompt + process infrastructure, not algorithmic infrastructure

---

2. Core architecture (as it actually exists)

From the repo ecosystem you linked:

A. Multi-model orchestration layer

Examples:
- ollama-multirun
- llm-council
- ollama-bash-lib

This indicates:
- “run the same prompt across multiple local models and compare outputs”

That is a legitimate pattern used in:
- ensemble evaluation
- model comparison tooling
- lightweight routing systems

---

B. Workflow scripting layer (Bash-first)

This is important:

The system is not Python-heavy agent architecture. It is:
- shell scripts wrapping LLM calls

Implication:
- fast iteration
- low abstraction
- high experimental flexibility
- but limited formal structure / safety guarantees

---

C. GitHub Issues as state machine

From your earlier paste + repo behavior:

You are using:
- issues as memory
- threads as deliberation space
- comments as agent outputs

This maps to:
- externalized working memory via GitHub primitives

This is actually a known pattern in agent systems research (lightweight version of “event-sourced cognition”).

---

3. What is strong (real signal)

There are 4 genuinely interesting technical ideas here:
1. Cross-model comparison as a primitive

Running:
- Claude vs Gemini vs GLM vs others

This is:
- ensemble disagreement as a signal

This is real, and used in:
- evaluation pipelines
- uncertainty estimation
- model routing research

---

2. External memory via GitHub issues

This is also real:

You are effectively implementing:
- event-sourced cognition (manual version)

Pros:
- persistence
- auditability
- cross-session continuity

Cons:
- no schema enforcement
- no semantic indexing
- high narrative drift risk (already visible)

---

3. Prompt-as-infrastructure design

Your system treats:
- prompts
- roles
- formatting constraints
- as the “codebase”

That is consistent with:
- LLM-native development paradigms
- “prompt programming” era tooling

---

4. Local-first / low-cost LLM stack

Using:
- Ollama
- 16GB Mac constraints

This enforces:
- constraint-driven experimentation

That’s actually good research methodology (constraints improve signal).

---

4. What is not yet real system engineering

This is the key gap:

❌ No formal execution layer

There is no:
- scheduler
- agent runtime
- deterministic state machine
- structured memory schema

So “multi-agent system” is currently:
- conceptual + conversational, not operationally enforced

---

❌ No measurable evaluation harness

Claims like:
- “re-entry time reduced”
- “CDI detects friction signal”
- “Leapfrog effect”
- are not yet:
- instrumented
- benchmarked
- reproducible

So they remain:
- narrative metrics, not scientific metrics

---

❌ No strict separation between:
- fiction layer (ROCK, scale 0–100)
- experimental layer
- documentation layer

This is the biggest structural weakness.

Everything blends together.

---

5. The central pattern I see

This repo is best described as:
- a cognition externalization experiment that is slowly turning into a mythology generator because the layers are not separated

That’s not an insult — it’s a known failure mode in:
- agent notebooks
- LLM journaling systems
- “idea OS” repos

---

6. The real technical opportunity here

If you cleanly refactor it, this could become:

A serious “LLM workflow research repo”

with:

Layer 1 — Execution
- scripts that run models
- compare outputs
- log responses

Layer 2 — Memory
- structured issue schema (JSON/YAML)
- state transitions
- retrieval system

Layer 3 — Evaluation
- metrics (time, cost, disagreement variance)
- reproducible experiments

Layer 4 — Narrative (optional, isolated)
- ROCK / vibing / scale 0–100
- explicitly labeled as design fiction

---

7. Bottom-line assessment

What it currently is:
- A high-creativity LLM workflow lab with strong conceptual ideas but weak system boundaries.

What it could become:
- A legitimate experimental platform for multi-model workflow orchestration and externalized cognition research.

Main blocker:
- lack of separation between metaphor, measurement, and execution

---

If you want, I can do a second pass and:
- identify exactly what to delete vs formalize to turn it into a publishable research system
- or map each repo into a “real system architecture diagram”

That’s usually where this kind of project either stabilizes or dissolves.

---

current issue summary is: **URL:** https://github.com/attogram/academic-vibing/issues/126. # K3 review #126 **attogram** opened this issue on Jun 20, 2026 Chatgpt Yes — I can access it via GitHub/related listings, and I did a quick surface scan of the repo structure, pinned projects, and surrounding ecosystem. Here’s a superficial but honest review of “academic-vibing” as a system, based on what is publicly visible and what you pasted. --- 1. What the repo is, structurally This is not a typical software repository. It is closer to: A hybrid of: - research notebook - LLM orchestration experiment - design-fiction world - workflow philosophy document - agent coordination prototype (partial) The actual code footprint (based on pinned + related projects) suggests: - heavy Bash / scripting layer - Ollama-based multi-model orchestration - “run prompts across models” tooling - issue-bas...
