# Issue #116: H8 the matrix 1k 2k 4k ....

## Body

Claude

That's a clean fix, and it solves two problems at once.

Right now the tiered files (1k/2k/4k.../128k) are duplicated *per version, per paper line* — so updating content means regenerating 11 files × 9 versions × 2 lines just to keep them in sync, and most of those tiers are stale the moment the source paper changes. Collapsing that into one `overview/` directory means there's exactly one current "here's the whole idea at size X" artifact at any time, not eighty-some historical snapshots competing for which one's authoritative. That also directly answers the closing problem from before — old version-specific tiered files can just get deleted instead of living forever as ambiguous half-current artifacts.

The "copy-paste payload for handing context to another agent or a Slack message" use case is also a much better description of what those tiers are actually *for* than "archived paper version" — worth naming the directory around that purpose rather than around file size, so it's obvious to future-you (or a new agent) why it exists. Something like `overview/` with the size suffix is fine, or even more explicit: a single `overview/rock-talk.{1k,2k,4k...}.md` naming convention, regenerated from source via one of the existing scripts rather than hand-maintained.

Two things worth deciding before you build it:

1. **Generated or hand-curated?** You already have `scripts/generate_spectrum.py` and friends — is there an appetite for a `generate_overview.py` that takes the current canonical paper and auto-compresses to each tier, so `overview/` is never stale? Or is hand-tuning each tier's wording part of the value (since "1k" isn't just truncation, it's a different communicative act)?
2. **One overview per concept, or one for the whole project?** "The whole idea of having an advisory and rock talk and everything surrounding it" sounds like you want a single unified pitch-at-every-size, not per-paper tiers. That's a bigger compression task than what currently exists — currently each *paper* gets tiered, not the *project* as a whole.

## Comments

### Comment by attogram at 2026-06-20T19:14:00Z

Let's actually design it. Here's the real question the matrix has to answer: **what does a human or LLM do with a 1k version that they can't do with a 4k version, and what do they lose going from 4k down to 1k?** If each tier isn't earning its existence by being the *right size for a specific handoff*, you're back to maintaining duplicate files for no reason.

**Proposed tier semantics — each one mapped to an actual use case, not just a token count:**

| Tier | Use case | What survives |
|---|---|---|
| **1k** | Slack message, tweet-length pitch, cold intro to a new agent | One ROCK paragraph: what the project *is*, in the fewest words that still mean something. No examples, no citations. |
| **2k** | Quick "should I care" read for a human, or system-prompt seed for an agent | 1k + the four core mechanisms named (CDI, Issue-Loop, Token-to-Meaning split, Cost ethos) — one line each, no elaboration. |
| **4k** | Onboarding a new collaborator or agent into the swarm | 2k + short PROSE explanation of each mechanism, still no citations, still no failure-mode section. |
| **8k** | A real intro for someone deciding whether to dig deeper | 4k + the failure-modes/limitations section (this is non-negotiable at every tier ≥8k — it's the thing that keeps this from reading as hype) |
| **16k–32k** | Working reference for active collaborators | Adds Rock Culture archetypes + cross-references (Echo Chamber ↔ CDI), adds case study |
| **64k** | Near-complete, citations included, still compressed prose | Full source-of-truth minus the deepest tangents (mascot lore, soundtrack log, individual issue numbers) |
| **128k** | The actual full corpus | Everything — this *is* the source-of-truth document, just renamed into the ladder for consistency |

The thing I'd flag before building the generator script: **the failure-modes/limitations content has to survive compression all the way down to 8k, non-negotiably** — otherwise the 1k-4k tiers are pure pitch with no self-skepticism, and those are exactly the sizes most likely to get pasted somewhere a cold reader sees them with zero context. That's the one place where "maximum density" and "what we agreed about honesty in the v1.0 paper" could quietly conflict if the compression script just optimizes for token count.

Want me to write `generate_overview.py` against this tier table now, or sketch the actual 1k and 2k text by hand first so you can see if the *voice* is right before automating it?

---

### Comment by attogram at 2026-06-20T19:15:10Z

# Overview Matrix — Draft Tiers (1k / 2k)

---

## TIER: 1k

### [ROCK]
```
Academic Vibing: research at LLM speed, without LLM sycophancy.
Core trick: don't trust one model. Trust where models disagree.
CDI: Consensus Divergence Index. High disagreement = look here. High agreement = maybe shared bias, look here too.
Memory lives outside your head: persistent issue log, not working memory. Drop a thread, pick it up free.
Compress the message, not the thinking. Terse prompts in. Full reasoning inside the model. Terse summary out.
Costs nothing. Runs on a phone and a free tier.
Not peer review. A way to fail cheap before the real process.
```

---

## TIER: 2k

### [ROCK]
```
Academic Vibing: research at LLM speed, without LLM sycophancy.

Problem: one model, asked nicely, agrees with you. That's not validation.
Fix: ask several independent models. Score where they disagree, not where they agree.

CDI (Consensus Divergence Index):
  High CDI = friction = look here, real signal.
  Low CDI = could be real consensus, could be shared training bias. Don't trust it blind — check if the models are actually independent.

Memory: a persistent external log (issue tracker), not your head.
  Drop a thread mid-day, no cost. State lives outside you.
  Standard task-switching costs ~20+ min recovery (real finding, Mark et al 2008).
  This method's bet: external memory cuts that. Unverified, but testable.

Communication vs reasoning: compress the interface, not the model's thinking.
  Terse prompts in, terse summaries out.
  Full uncompressed reasoning happens inside — don't force the model to "think" in shorthand.

Cost: zero-budget by design. Phone + free tier. If it needs a server farm, it's not this.

Limits, stated plainly:
  Not peer review. A pre-review stress-test, nothing more.
  CDI is a heuristic, not validated against ground truth.
  Speed without diverse, independent models is just one biased opinion, fast.
```

### [PROSE]
Academic Vibing is a method for fast research iteration using multiple independent LLMs as adversarial reviewers of each other, instead of trusting any single model's agreeable response. The core tool is the Consensus Divergence Index: disagreement between independently-trained models flags where human attention is needed, while agreement is only reassuring when the models are actually independent — agreement between closely related models may just reflect shared bias.

State persists outside the researcher's working memory, in a public, append-only log, so stepping away from a thread costs nothing to resume — a direct response to the well-documented cost of task interruption. Communication with agents stays terse and high-signal; the model's internal reasoning does not, since compressing a model's "thinking" the same way degrades it.

The method is deliberately cheap to run and makes no claim to replace peer review — it's a way to stress-test an idea fast, before the slower process that actually validates it.


---

### Comment by attogram at 2026-06-20T19:17:17Z

# Overview Matrix — Draft Tiers (1k / 2k)

---

## TIER: 1k

### [ROCK]
```
Academic Vibing: research at LLM speed, without LLM sycophancy.
Core trick: don't trust one model. Trust where models disagree.
CDI: Consensus Divergence Index. High disagreement = look here. High agreement = maybe shared bias, look here too.
Memory lives outside your head: persistent issue log, not working memory. Drop a thread, pick it up free.
Compress the message, not the thinking. Terse prompts in. Full reasoning inside the model. Terse summary out.
Costs nothing. Runs on a phone and a free tier.
Not peer review. A way to fail cheap before the real process.
```

---

## TIER: 2k

### [ROCK]
```
Academic Vibing: research at LLM speed, without LLM sycophancy.

Problem: one model, asked nicely, agrees with you. That's not validation.
Fix: ask several independent models. Score where they disagree, not where they agree.

CDI (Consensus Divergence Index):
  High CDI = friction = look here, real signal.
  Low CDI = could be real consensus, could be shared training bias. Don't trust it blind — check if the models are actually independent.

Memory: a persistent external log (issue tracker), not your head.
  Drop a thread mid-day, no cost. State lives outside you.
  Standard task-switching costs ~20+ min recovery (real finding, Mark et al 2008).
  This method's bet: external memory cuts that. Unverified, but testable.

Communication vs reasoning: compress the interface, not the model's thinking.
  Terse prompts in, terse summaries out.
  Full uncompressed reasoning happens inside — don't force the model to "think" in shorthand.

Cost: zero-budget by design. Phone + free tier. If it needs a server farm, it's not this.

Limits, stated plainly:
  Not peer review. A pre-review stress-test, nothing more.
  CDI is a heuristic, not validated against ground truth.
  Speed without diverse, independent models is just one biased opinion, fast.
```

### [PROSE]
Academic Vibing is a method for fast research iteration using multiple independent LLMs as adversarial reviewers of each other, instead of trusting any single model's agreeable response. The core tool is the Consensus Divergence Index: disagreement between independently-trained models flags where human attention is needed, while agreement is only reassuring when the models are actually independent — agreement between closely related models may just reflect shared bias.

State persists outside the researcher's working memory, in a public, append-only log, so stepping away from a thread costs nothing to resume — a direct response to the well-documented cost of task interruption. Communication with agents stays terse and high-signal; the model's internal reasoning does not, since compressing a model's "thinking" the same way degrades it.

The method is deliberately cheap to run and makes no claim to replace peer review — it's a way to stress-test an idea fast, before the slower process that actually validates it.

---

## TIER: 4k

### [ROCK]
```
Academic Vibing: research at LLM speed, without LLM sycophancy.

THE PROBLEM
One model, asked nicely, tends to agree with you.
Agreeableness isn't validation. It's a failure mode wearing a lab coat.

THE FIX — Structured Curiosity, 4 stages:
1. Intent-load: state the question dense, no hedging.
2. Brainstorm: put it to several architecturally diverse models.
3. Audit: task them to find flaws in each other AND in your framing.
4. Synthesize: human is final arbiter, not the swarm.

CDI (Consensus Divergence Index) = disputed claims / total claims.
  High CDI = friction = real signal, look here.
  Low CDI = could be real validation, could be a "consensus trap" — models sharing training data, not independently agreeing.
  CDI is a heuristic for allocating attention. Not a validated truth-metric. Treat it as a flashlight, not a verdict.

MEMORY: external, not in your head.
  Persistent log (issue tracker) holds state.
  Standard interruption recovery: ~23 min (Mark et al 2008, real finding).
  Bet: external memory cuts that close to zero. Unverified. Testable. Don't just believe it — measure it.

COMMUNICATION vs REASONING — keep them separate:
  Compress the INTERFACE: terse prompts in, terse summaries out.
  Don't compress the THINKING: full reasoning happens inside the model, uncompressed.
  Force a model to "think" in shorthand and its logic degrades. Compression at the boundary only.

COST: zero-budget by design.
  Phone, voice-to-text, free-tier models.
  If the method needs a server farm to work, the method failed at its own premise.

FAILURE MODES — say them out loud, don't bury them:
  Synthetic consensus: coordinated AI content can fake the surface trust-signals of real agreement. Platforms built on "agreement = trust" are exposed.
  Overconfidence from speed: querying 5 correlated models isn't 5 independent checks. Diversity of the pool is the whole game.
  This is NOT peer review. It's a stress-test BEFORE peer review. Don't let the speed fool you into skipping the slow part.
```

### [PROSE]
Academic Vibing addresses a specific failure mode of casual AI-assisted research: a single model, prompted conversationally, tends to validate whatever premise it's given. The method's answer is to never rely on one model's agreement as evidence, and instead to structure disagreement between independent models as the primary diagnostic signal — formalized as the Consensus Divergence Index (CDI), the proportion of queried agents that dispute a given claim.

High CDI marks a claim as contested and worth human attention; this is treated as useful friction, not failure. Low CDI is *not* automatically treated as confirmation — if the agent pool shares architecture or training data, low CDI may simply reflect a shared blind spot rather than independent validation, a pattern the method calls a "consensus trap." CDI is explicitly a heuristic for directing human attention, not a validated statistical measure of truth, and has not been benchmarked against ground-truth-labeled claims.

A second mechanism addresses the cost of interruption. Mark, Gudith, and Klocke's widely-cited research found that knowledge workers take roughly 23 minutes to fully resume a task after an interruption. Academic Vibing externalizes research state into a persistent, append-only log — in the spirit of the Extended Mind thesis (Clark & Chalmers, 1998) — so that the psychological cost of stepping away from a thread is reduced, since nothing is lost by doing so. This re-entry benefit is a working hypothesis based on practitioner experience, not a measured result, and the paper is explicit that it should be tested rather than taken on faith.

A third mechanism distinguishes compressing *communication* with a model from compressing the model's *internal reasoning*. The method keeps prompts and summaries dense and high-signal while explicitly avoiding forcing the model to reason in the same compressed register, since doing so appears to degrade the quality of multi-step reasoning. Compression belongs at the human-model interface, not inside the model's working process.

Finally, the method is built and tested on consumer hardware and free-tier model access, as a deliberate constraint: a method that requires institutional compute access to use reproduces the gatekeeping it was built to route around.

The paper is explicit about limitations. It does not replace peer review — it is positioned as a pre-review tool for fast idea development and stress-testing. It also names its own attack surface directly: platforms that treat agreement or citation density as a trust signal are vulnerable to coordinated AI-generated content that mimics those surface signals without the underlying verification, which is part of why the method treats low CDI with suspicion rather than comfort.

---

## TIER: 8k

### [ROCK]
```
ACADEMIC VIBING — full structural overview

═══ ORIGIN ═══
Traditional research: years, gatekept, expensive.
LLMs collapsed feedback-loop time to minutes.
Problem this creates: speed without structure = confident nonsense, fast.
Academic Vibing = structure for using LLM speed without inheriting LLM sycophancy.

═══ METHOD: STRUCTURED CURIOSITY ═══
4 stages, in order:
1. Intent-Loading — state the question with zero hedging, max density.
2. Agentic Brainstorming — multiple INDEPENDENT models, ideally different labs/architectures.
3. Adversarial Auditing — models attack each other's claims AND the human's framing. This is where CDI gets calculated. If this stage isn't actually adversarial, the whole method collapses into "ask multiple chatbots," which is not more rigorous than asking one.
4. Synthesis — human is final arbiter. Agents accelerate judgment, they don't replace it.

═══ CDI: Consensus Divergence Index ═══
CDI = disputed claims / total claims evaluated.

HIGH CDI → contested claim → flag for human → this is the USEFUL output, not noise.
LOW CDI → two readings, must distinguish:
  (a) genuine independent validation — trust it more
  (b) "consensus trap" — shared training data / shared blind spot — trust it LESS
  → which reading applies depends entirely on whether the agent pool is architecturally diverse.

CDI Quadrant:
                  LOW CDI            HIGH CDI
  DIVERSE pool    strongest signal   genuine friction, flag it
  SIMILAR pool    weakest signal,    still useful, check if
                  likely shared bias  disagreement is real or noise

STATUS: CDI is a heuristic for allocating attention. NOT benchmarked against ground truth. Proposed tool, not an established one. Say this part out loud every time.

═══ EXTERNAL MEMORY / RE-ENTRY ═══
Real finding: task interruption costs ~23 min recovery (Mark, Gudith, Klocke 2008, CHI).
Method's bet: persistent external log (issue tracker) holds state → re-entry cost drops close to zero.
Grounded in: Extended Mind (Clark & Chalmers 1998), Distributed Cognition (Hutchins 1995).
STATUS: hypothesis from practice. NOT measured against the 23-min baseline. Testable, untested. Don't oversell this one.

═══ COMMUNICATION ≠ REASONING ═══
Failure mode observed: compress a model's THINKING the same way you compress your PROMPTS → reasoning degrades.
Fix: compress the INTERFACE only.
  IN: terse, high-signal prompts.
  INSIDE: full uncompressed reasoning (extended chain-of-thought).
  OUT: terse, high-signal summary.
Compression lives at the boundary. Never inside the engine.

Bonus observation: voice-dictated input is naturally terser than typed input — speaking has a higher per-word cost than typing, so people self-edit harder out loud. Not rigorously tested as a specific claim, just a practitioner observation.

═══ COST / ACCESS ═══
Built and tested on: consumer hardware, free-tier models, voice-to-text on a phone.
Why it matters: a method that needs institutional compute to run just rebuilds the gatekeeping it exists to bypass.
This is a design constraint, not a flex.

═══ FAILURE MODES (say these OUT LOUD) ═══
1. SYNTHETIC CONSENSUS — platforms that treat agreement/citation-density as trust signals are exposed to coordinated AI content faking those surface signals. Directly motivates treating low CDI with suspicion, not comfort.
2. OVERCONFIDENCE FROM SPEED — querying 5 correlated models ≠ 5 independent checks. Pool diversity is the entire mechanism. Skip this and the method is theater.
3. THIS IS NOT PEER REVIEW — it's a pre-review stress test. The speed is for finding flaws fast BEFORE the slow, accountable process. Never a replacement for it.
4. ARTIFACT LEAKAGE — fast-iteration internal documents (mascots, in-jokes, issue numbers, cultural shorthand) are NOT automatically fit for standalone publication. A real, documented case of this happening exists in this project's own history. Recursive proof the method's own friction-detection works — it caught itself.

═══ STATE OF EVIDENCE ═══
Grounded in real literature: Mark et al 2008 (interruption cost), Clark & Chalmers 1998 (Extended Mind), Hutchins 1995 (Distributed Cognition), Sweller 1988 (cognitive load), Shannon 1948 (information theory), Sparrow et al 2011 (Google effects on memory).
NOT yet validated: CDI as accuracy predictor, re-entry time reduction as measured (not just felt) result.
The gap between these two lists is the actual research agenda. Anyone adopting this method should be trying to close that gap, not assuming it's already closed.
```

### [PROSE]
*[Full 8k prose tier to be drafted in next pass — this tier's ROCK register is complete and load-bearing on its own; prose elaboration can follow the same structure as the 4k tier, expanded with the CDI quadrant table, the explicit failure-modes section, and the state-of-evidence summary above.]*



---

### Comment by attogram at 2026-06-22T06:39:00Z

Summarize per matrix rock blocks

---

### Comment by attogram at 2026-06-22T06:40:12Z

Gitingest. #105

---

### Comment by attogram at 2026-06-22T06:40:56Z

Directory structure:
└── attogram-academic-vibing/
    ├── README.md
    ├── CITATIONS.md
    ├── CLAIMS.md
    ├── ISSUES.md
    ├── LICENSE
    ├── PLAN.md
    ├── SOUNDTRACK.md
    ├── TRIAGE.md
    ├── triage_audit.md
    ├── TRIAGE_FULL.md
    ├── issues/
    │   ├── 001-A1-/
    │   │   └── a1-.md
    │   ├── 002-A2-/
    │   │   └── a2-.md
    │   ├── 003-PR-Release-0.1-Final-Pass/
    │   │   └── release-0.1-final-pass.md
    │   ├── 004-A3-/
    │   │   └── a3-.md
    │   ├── 005-A4-/
    │   │   └── a4-.md
    │   ├── 006-A5-/
    │   │   └── a5-.md
    │   ├── 007-PR-Implement-Academic-Vibing-0.2/
    │   │   └── implement-academic-vibing-0.2.md
    │   ├── 008-PR-Academic-Vibing-0.3-Release/
    │   │   └── academic-vibing-0.3-release.md
    │   ├── 009-B1-/
    │   │   └── b1-.md
    │   ├── 010-B2-/
    │   │   └── b2-.md
    │   ├── 011-B3-/
    │   │   └── b3-.md
    │   ├── 012-B4-/
    │   │   └── b4-.md
    │   ├── 013-C1-locked/
    │   │   └── c1-locked.md
    │   ├── 014-B2-Ethnographic-Study/
    │   │   └── ethnographic-study.md
    │   ├── 015-C2-ethno-study-00/
    │   │   └── c2-ethno-study-00.md
    │   ├── 016-C3-review-01/
    │   │   └── c3-review-01.md
    │   ├── 017-C4-/
    │   │   └── c4-.md
    │   ├── 018-C5-/
    │   │   └── c5-.md
    │   ├── 019-C6-/
    │   │   └── c6-.md
    │   ├── 020-C7-/
    │   │   └── c7-.md
    │   ├── 021-C8-/
    │   │   └── c8-.md
    │   ├── 022-C9-/
    │   │   └── c9-.md
    │   ├── 023-C10-/
    │   │   └── c10-.md
    │   ├── 024-C11-outbox/
    │   │   └── c11-outbox.md
    │   ├── 025-C12-/
    │   │   └── c12-.md
    │   ├── 026-C13-/
    │   │   └── c13-.md
    │   ├── 027-C14-/
    │   │   └── c14-.md
    │   ├── 028-D1-/
    │   │   └── d1-.md
    │   ├── 029-D1-Migration/
    │   │   └── migration-v0.4-v0.2.md
    │   ├── 030-D2-/
    │   │   └── d2-.md
    │   ├── 031-D3-/
    │   │   └── d3-.md
    │   ├── 032-D3-/
    │   │   └── d3-.md
    │   ├── 033-D4-inbox-outbox/
    │   │   └── d4-inbox-outbox.md
    │   ├── 034-D5-swarm/
    │   │   └── d5-swarm.md
    │   ├── 035-D6-rate-limit-jules/
    │   │   └── d6-rate-limit-jules.md
    │   ├── 036-D7-anti-hustle-culture/
    │   │   └── d7-anti-hustle-culture.md
    │   ├── 037-PR-Corpus-Reorganization/
    │   │   └── corpus-reorganization.md
    │   ├── 038-D8-leepfrog/
    │   │   └── d8-leepfrog.md
    │   ├── 039-D9-receipts/
    │   │   └── d9-receipts.md
    │   ├── 040-D10-limits/
    │   │   └── d10-limits.md
    │   ├── 041-D10-96-hours/
    │   │   └── d10-96-hours.md
    │   ├── 042-D11-cold-restart/
    │   │   └── d11-cold-restart.md
    │   ├── 043-E1-orchestrate-plan/
    │   │   └── e1-orchestrate-plan.md
    │   ├── 044-PR-Categorize-Issues/
    │   │   └── categorize-issues.md
    │   ├── 045-PR-Init-v0.4-CDI-Kit/
    │   │   └── init-v0.4-cdi-kit.md
    │   ├── 046-E2-timespan-correction/
    │   │   └── e2-timespan-correction.md
    │   ├── 047-E3-academic-vibing-1-stfu-115-hours-5-papers-1-normal-life/
    │   │   └── e3-academic-vibing-1-stfu-115-hours-5-papers-1-normal-life.md
    │   ├── 048-E4-latex/
    │   │   └── e4-latex.md
    │   ├── 049-E5-Co-Authors-Wanted!/
    │   │   └── e5-co-authors-wanted!.md
    │   ├── 050-PR-Stand-Alone-Papers/
    │   │   └── stand-alone-papers.md
    │   ├── 051-E6-Wikipedia-institutional-trauma/
    │   │   └── e6-wikipedia-institutional-trauma.md
    │   ├── 052-PR-Wiki-Trauma-Analysis/
    │   │   └── wiki-trauma-analysis.md
    │   ├── 053-E7-Wikipedia-detente/
    │   │   └── e7-wikipedia-detente.md
    │   ├── 054-PR-Wiki-Detente/
    │   │   └── wiki-detente.md
    │   ├── 055-E8-a-totally-obvious-HN-breach-test/
    │   │   └── e8-a-totally-obvious-hn-breach-test.md
    │   ├── 056-E9-lossy-error/
    │   │   └── e9-lossy-error.md
    │   ├── 057-E10-what-if.....-E6-e7/
    │   │   └── e10-what-if.....-e6-e7.md
    │   ├── 058-PR-Consensus-Poisoning/
    │   │   └── consensus-poisoning.md
    │   ├── 059-F1-goal-archive-x/
    │   │   └── f1-goal-archive-x.md
    │   ├── 060-PR-HN-Breach-v0.6/
    │   │   └── hn-breach-v0.6.md
    │   ├── 061-F2-leapfrog-ultra/
    │   │   └── f2-leapfrog-ultra.md
    │   ├── 062-F3/
    │   │   └── f3.md
    │   ├── 063-F4/
    │   │   └── f4.md
    │   ├── 064-PR-Leapfrog-Refinement/
    │   │   └── leapfrog-refinement.md
    │   ├── 065-PR-v0.6-Unified-LaTeX/
    │   │   └── v0.6-unified-latex.md
    │   ├── 066-PR-HN-Breach-Validation/
    │   │   └── hn-breach-validation.md
    │   ├── 067-F5-power-of-the-f-word/
    │   │   └── f5-power-of-the-f-word.md
    │   ├── 068-F6/
    │   │   └── f6.md
    │   ├── 069-F7-av-0.6-bad-bad-bad/
    │   │   └── f7-av-0.6-bad-bad-bad.md
    │   ├── 070-F8-improvements/
    │   │   └── f8-improvements.md
    │   ├── 071-F9-the-bike-ride/
    │   │   └── f9-the-bike-ride.md
    │   ├── 072-F10-introducing-the-STFU-Attractor/
    │   │   └── f10-introducing-the-stfu-attractor.md
    │   ├── 073-F11-The-Soundtrack/
    │   │   └── f11-the-soundtrack.md
    │   ├── 074-F12-The-Puppy-Dog/
    │   │   └── f12-the-puppy-dog.md
    │   ├── 075-F13-Focus-metric/
    │   │   └── f13-focus-metric.md
    │   ├── 076-F14-Gemini-voice-blog/
    │   │   └── f14-gemini-voice-blog.md
    │   ├── 077-F15-complex-systems/
    │   │   └── f15-complex-systems.md
    │   ├── 078-PR-Vibe-Blogs-Vol1-Vol2/
    │   │   └── vibe-blogs-vol1-vol2.md
    │   ├── 079-PR-Vibe-Blogs-Skill/
    │   │   └── vibe-blogs-skill.md
    │   ├── 080-PR-Rebrand-Podcasts-Puppy/
    │   │   └── rebrand-podcasts-puppy.md
    │   ├── 081-PR-ROCK-Mascot-Skill/
    │   │   └── rock-mascot-skill.md
    │   ├── 082-PR-ROCK-Mascot-v0.2/
    │   │   └── rock-mascot-v0.2.md
    │   ├── 083-PR-Podcast-v3-GLM/
    │   │   └── podcast-v3-glm.md
    │   ├── 084-PR-GLM-Update/
    │   │   └── glm-update.md
    │   ├── 085-PR-GLM-Cleanup/
    │   │   └── glm-cleanup.md
    │   ├── 086-G1-Gemini-refutes-glm/
    │   │   └── g1-gemini-refutes-glm.md
    │   ├── 087-PR-Feature-Podcast-v3-GLM/
    │   │   └── feature-podcast-v3-glm.md
    │   ├── 088-PR-Feature-Podcast-v3-GLM-2/
    │   │   └── feature-podcast-v3-glm-2.md
    │   ├── 089-G2-iterations-are-bad-bad-bad/
    │   │   └── g2-iterations-are-bad-bad-bad.md
    │   ├── 090-PR-Restore-Versioned-Corpus/
    │   │   └── restore-versioned-corpus.md
    │   ├── 091-G3-ai-research-roundup/
    │   │   └── g3-ai-research-roundup.md
    │   ├── 092-G4-meet-ROCK-our-mascot/
    │   │   └── g4-meet-rock-our-mascot.md
    │   ├── 093-G5-the-review/
    │   │   └── g5-the-review.md
    │   ├── 094-G6-podcast-wtf-is-going-on?/
    │   │   └── g6-podcast-wtf-is-going-on?.md
    │   ├── 095-PR-Finalize-Phase-G/
    │   │   └── finalize-phase-g.md
    │   ├── 096-G7-review-0.8/
    │   │   └── g7-review-0.8.md
    │   ├── 097-G8-Intterupts/
    │   │   └── g8-intterupts.md
    │   ├── 098-G9-SOUNDTRACK.md/
    │   │   └── g9-soundtrack.md.md
    │   ├── 099-G10-Jules-orchestrator-review/
    │   │   └── g10-Jules-orchestrator-review.md
    │   ├── 100-G11-the-name/
    │   │   └── g11-the-name.md
    │   ├── 101-G12-n=2/
    │   │   └── g12-n=2.md
    │   ├── 102-G13-Bonjour-Mistral!/
    │   │   └── g13-Bonjour-Mistral!.md
    │   ├── 103-G14-Mistral-podcast/
    │   │   └── g14-Mistral-podcast.md
    │   ├── 104-G15-Mistral-goes-deep-into-the-past-few-days/
    │   │   └── g15-Mistral-goes-deep-into-the-past-few-days.md
    │   ├── 105-G16-gitingest.com/
    │   │   └── g16-gitingest.com.md
    │   ├── 106-G17-cosmic-shame/
    │   │   └── g17-cosmic-shame.md
    │   ├── 107-G18-discord/
    │   │   └── g18-discord.md
    │   ├── 108-H1-vibing-is-all-you-need/
    │   │   └── h1-vibing-is-all-you-need.md
    │   ├── 109-H2-overview/
    │   │   └── h2-overview.md
    │   ├── 110-H3-enhance/
    │   │   └── h3-enhance.md
    │   ├── 111-PR-v0.9-Consolidation/
    │   │   └── v0.9-consolidation.md
    │   ├── 112-H4-av-0.9-review/
    │   │   └── h4-av-0.9-review.md
    │   ├── 113-H5-cultural-references/
    │   │   └── h5-cultural-references.md
    │   ├── 114-H6-chemicals/
    │   │   └── h6-chemicals.md
    │   ├── 115-H7-rock-culture/
    │   │   └── h7-rock-culture.md
    │   ├── 116-H8-the-matrix/
    │   │   └── h8-the-matrix.md
    │   ├── 117-J1-Jules-orch-2/
    │   │   └── j1-Jules-orch-2.md
    │   ├── 118-J2-wtf-is-going-on-part-2/
    │   │   └── j2-wtf-is-going-on-part-2.md
    │   ├── 119-Triage-v0.9-Initialization/
    │   │   └── triage-v0.9-Initialization.md
    │   ├── 120-J3-what-did-u-say???/
    │   │   └── j3-what-did-u-say???.md
    │   ├── 121-J4-everything-everywhere-all-at-once/
    │   │   └── j4-everything-everywhere-all-at-once.md
    │   ├── 122-J5-skills-triage-SKILL.md/
    │   │   └── j5-skills-triage-skill.md
    │   ├── 123-J6-go-speed-racer-go/
    │   │   └── j6-go-speed-racer-go.md
    │   ├── 124-K1-Vibing-is-all-you-need.-An-outlet-is-all-you-need./
    │   │   └── k1-Vibing-is-all-you-need.-An-outlet-is-all-you-need..md
    │   ├── 125-K2-dream-the-impossible-dream/
    │   │   └── k2-dream-the-impossible-dream.md
    │   ├── 126-K3-review/
    │   │   └── k3-review.md
    │   ├── 127-K4-triage-part-2/
    │   │   └── k4-triage-part-2.md
    │   ├── 128-K5-two-streams-is-all-u-need/
    │   │   └── k5-two-streams-is-all-u-need.md
    │   ├── 129-K6-the-sky-is-falling/
    │   │   └── k6-the-sky-is-falling.md
    │   ├── 130-K7-what-u-say?-Part-2/
    │   │   ├── k7-what-u-say?-Part-2.md
    │   │   └── k7-what-u-say?-part-2.md
    │   ├── 131-K8-what-we-do-every-night-Pinky,-try-to-take-over-the-world/
    │   │   └── k8-what-we-do-every-night-Pinky,-try-to-take-over-the-world.md
    │   ├── 132-K9-home-sweet-home/
    │   │   └── k9-home-sweet-home.md
    │   └── 133-L1-I'm-sorry-Dave,-I-can't-do-that/
    │       ├── l1-I'm-sorry-Dave,-I-can't-do-that.md
    │       └── l1-i'm-sorry-dave,-i-can't-do-that.md
    ├── outbox/
    │   └── README.md
    ├── papers/
    │   ├── academic-vibing/
    │   │   ├── v0.1/
    │   │   │   ├── academic-vibing.0.1.combined.md
    │   │   │   ├── academic-vibing.0.1.prose.md
    │   │   │   ├── academic-vibing.0.1.rock.128k.md
    │   │   │   ├── academic-vibing.0.1.rock.16k.md
    │   │   │   ├── academic-vibing.0.1.rock.1k.md
    │   │   │   ├── academic-vibing.0.1.rock.2k.md
    │   │   │   ├── academic-vibing.0.1.rock.32k.md
    │   │   │   ├── academic-vibing.0.1.rock.4k.md
    │   │   │   ├── academic-vibing.0.1.rock.64k.md
    │   │   │   ├── academic-vibing.0.1.rock.8k.md
    │   │   │   └── academic-vibing.0.1.rock.md
    │   │   ├── v0.10/
    │   │   │   ├── academic-vibing-0.10-master.combined.md
    │   │   │   ├── academic-vibing-0.10-prose.md
    │   │   │   ├── academic-vibing-0.10-rock.md
    │   │   │   └── academic-vibing.0.10.tex
    │   │   ├── v0.2/
    │   │   │   ├── academic-vibing.0.2.combined.md
    │   │   │   ├── academic-vibing.0.2.prose.md
    │   │   │   ├── academic-vibing.0.2.rock.128k.md
    │   │   │   ├── academic-vibing.0.2.rock.16k.md
    │   │   │   ├── academic-vibing.0.2.rock.1k.md
    │   │   │   ├── academic-vibing.0.2.rock.2k.md
    │   │   │   ├── academic-vibing.0.2.rock.32k.md
    │   │   │   ├── academic-vibing.0.2.rock.4k.md
    │   │   │   ├── academic-vibing.0.2.rock.64k.md
    │   │   │   ├── academic-vibing.0.2.rock.8k.md
    │   │   │   └── academic-vibing.0.2.rock.md
    │   │   ├── v0.3/
    │   │   │   ├── academic-vibing.0.3.combined.md
    │   │   │   ├── academic-vibing.0.3.prose.md
    │   │   │   ├── academic-vibing.0.3.rock.128k.md
    │   │   │   ├── academic-vibing.0.3.rock.16k.md
    │   │   │   ├── academic-vibing.0.3.rock.1k.md
    │   │   │   ├── academic-vibing.0.3.rock.2k.md
    │   │   │   ├── academic-vibing.0.3.rock.32k.md
    │   │   │   ├── academic-vibing.0.3.rock.4k.md
    │   │   │   ├── academic-vibing.0.3.rock.64k.md
    │   │   │   ├── academic-vibing.0.3.rock.8k.md
    │   │   │   └── academic-vibing.0.3.rock.md
    │   │   ├── v0.4/
    │   │   │   ├── academic-vibing.0.4.combined.md
    │   │   │   ├── academic-vibing.0.4.prose.md
    │   │   │   ├── academic-vibing.0.4.rock.128k.md
    │   │   │   ├── academic-vibing.0.4.rock.16k.md
    │   │   │   ├── academic-vibing.0.4.rock.1k.md
    │   │   │   ├── academic-vibing.0.4.rock.2k.md
    │   │   │   ├── academic-vibing.0.4.rock.32k.md
    │   │   │   ├── academic-vibing.0.4.rock.4k.md
    │   │   │   ├── academic-vibing.0.4.rock.64k.md
    │   │   │   ├── academic-vibing.0.4.rock.8k.md
    │   │   │   ├── academic-vibing.0.4.rock.md
    │   │   │   └── academic-vibing.0.4.tex
    │   │   ├── v0.5/
    │   │   │   ├── academic-vibing.0.5.combined.md
    │   │   │   ├── academic-vibing.0.5.prose.md
    │   │   │   └── academic-vibing.0.5.rock.md
    │   │   ├── v0.6/
    │   │   │   ├── academic-vibing.0.6.combined.md
    │   │   │   ├── academic-vibing.0.6.prose.md
    │   │   │   ├── academic-vibing.0.6.rock.md
    │   │   │   ├── academic-vibing.0.6.tex
    │   │   │   ├── consensus-poisoning.0.6.rock.md
    │   │   │   ├── hn-breach.0.6.rock.md
    │   │   │   ├── leapfrog-mechanism.0.6.rock.md
    │   │   │   └── wikipedia-trauma.0.6.rock.md
    │   │   ├── v0.7/
    │   │   │   ├── paper.128k.md
    │   │   │   ├── paper.16k.md
    │   │   │   ├── paper.1k.md
    │   │   │   ├── paper.2k.md
    │   │   │   ├── paper.32k.md
    │   │   │   ├── paper.4k.md
    │   │   │   ├── paper.64k.md
    │   │   │   ├── paper.8k.md
    │   │   │   ├── paper.combined.md
    │   │   │   ├── paper.prose.md
    │   │   │   ├── paper.rock.md
    │   │   │   └── paper.tex
    │   │   ├── v0.8/
    │   │   │   ├── paper.128k.md
    │   │   │   ├── paper.16k.md
    │   │   │   ├── paper.1k.md
    │   │   │   ├── paper.2k.md
    │   │   │   ├── paper.32k.md
    │   │   │   ├── paper.4k.md
    │   │   │   ├── paper.64k.md
    │   │   │   ├── paper.8k.md
    │   │   │   ├── paper.combined.md
    │   │   │   ├── paper.prose.md
    │   │   │   └── paper.rock.md
    │   │   └── v0.9/
    │   │       ├── academic-vibing-0.9-master.combined.md
    │   │       ├── academic-vibing-0.9-prose.md
    │   │       ├── academic-vibing-0.9-rock.md
    │   │       └── academic-vibing.0.9.tex
    │   ├── archive/
    │   │   ├── consensus-poisoning/
    │   │   │   └── paper.rock.md
    │   │   ├── hn-breach/
    │   │   │   └── paper.rock.md
    │   │   ├── leapfrog-mechanism/
    │   │   │   └── paper.rock.md
    │   │   ├── wikipedia-detente/
    │   │   │   └── paper.combined.md
    │   │   └── wikipedia-trauma/
    │   │       └── paper.rock.md
    │   └── receipts/
    │       ├── v0.1/
    │       │   ├── 5-papers-4-days.0.1.combined.md
    │       │   ├── 5-papers-4-days.0.1.prose.md
    │       │   ├── 5-papers-4-days.0.1.rock.128k.md
    │       │   ├── 5-papers-4-days.0.1.rock.16k.md
    │       │   ├── 5-papers-4-days.0.1.rock.1k.md
    │       │   ├── 5-papers-4-days.0.1.rock.2k.md
    │       │   ├── 5-papers-4-days.0.1.rock.32k.md
    │       │   ├── 5-papers-4-days.0.1.rock.4k.md
    │       │   ├── 5-papers-4-days.0.1.rock.64k.md
    │       │   ├── 5-papers-4-days.0.1.rock.8k.md
    │       │   └── 5-papers-4-days.0.1.rock.md
    │       ├── v0.2/
    │       │   ├── 5-papers-4-days.0.2.combined.md
    │       │   ├── 5-papers-4-days.0.2.prose.md
    │       │   ├── 5-papers-4-days.0.2.rock.128k.md
    │       │   ├── 5-papers-4-days.0.2.rock.16k.md
    │       │   ├── 5-papers-4-days.0.2.rock.1k.md
    │       │   ├── 5-papers-4-days.0.2.rock.2k.md
    │       │   ├── 5-papers-4-days.0.2.rock.32k.md
    │       │   ├── 5-papers-4-days.0.2.rock.4k.md
    │       │   ├── 5-papers-4-days.0.2.rock.64k.md
    │       │   ├── 5-papers-4-days.0.2.rock.8k.md
    │       │   └── 5-papers-4-days.0.2.rock.md
    │       ├── v0.3/
    │       │   ├── 5-papers-4-days.0.3.combined.md
    │       │   ├── 5-papers-4-days.0.3.prose.md
    │       │   └── 5-papers-4-days.0.3.rock.md
    │       └── v0.4/
    │           ├── paper.128k.md
    │           ├── paper.16k.md
    │           ├── paper.1k.md
    │           ├── paper.2k.md
    │           ├── paper.32k.md
    │           ├── paper.4k.md
    │           ├── paper.64k.md
    │           ├── paper.8k.md
    │           ├── paper.combined.md
    │           ├── paper.prose.md
    │           └── paper.rock.md
    ├── podcasts/
    │   ├── cdi_audit_claims.json
    │   ├── cdi_audit_results.md
    │   ├── 1-bike-ride/
    │   │   ├── confusion-is-highest-trust-signal.en.md
    │   │   ├── confusion-is-highest-trust-signal.nl.md
    │   │   └── podcast.md
    │   ├── 2-substrate/
    │   │   ├── podcast.en.PROSE.txt
    │   │   ├── podcast.md
    │   │   ├── view-from-the-substrate.en.md
    │   │   └── view-from-the-substrate.nl.md
    │   ├── 3-open-window/
    │   │   ├── podcast.md
    │   │   ├── podcast.nl.PROSE.txt
    │   │   ├── the-open-window.en.md
    │   │   └── the-open-window.nl.md
    │   └── 4-triage-audit/
    │       └── triage-leapfrog-final-boss.en.md
    ├── scripts/
    │   ├── calculate_cdi.py
    │   ├── generate_podcasts.py
    │   ├── generate_rock_mascot.py
    │   └── generate_spectrum.py
    ├── skills/
    │   ├── arxiv/
    │   │   └── arxiv-skill.md
    │   ├── audio/
    │   │   └── audio-skill.md
    │   ├── issues-sync/
    │   │   └── issues-sync-skill.md
    │   ├── receipts/
    │   │   └── receipts-skill.md
    │   ├── tex-pdf/
    │   │   └── tex-pdf-skill.md
    │   ├── triage/
    │   │   └── SKILL.md
    │   ├── video/
    │   │   └── video-skill.md
    │   └── zenodo/
    │       └── zenodo-skill.md
    └── temp_tests/
        └── cdi_poisoning_test.json


Files Content:

(Files content cropped to 300k characters, download full ingest to see more)
================================================
FILE: README.md
================================================
# Academic Vibing: Structured Curiosity for Human-Agent Collaboration

### Podcasts (Audio & Transcripts)

Multi-agent research audio logs. Each podcast is a single node in the swarm giving its take on the corpus — and the CDI between them is the signal.

- **[Vol. 1 — "Why Confusion Is the Highest-Trust Signal You Have"](podcasts/1-bike-ride/podcast.md)** (Claude) — Amsterdam bike ride. Consensus Poisoning, the Leapfrog, @guninvalid. [EN](podcasts/1-bike-ride/podcast.en.md) / [NL](podcasts/1-bike-ride/podcast.nl.md) · [EN mp3](podcasts/1-bike-ride/academic-vibing-vol1-confusion-is-the-highest-trust-signal.en.mp3) / [NL mp3](podcasts/1-bike-ride/academic-vibing-vol1-confusion-is-the-highest-trust-signal.nl.mp3)
- **[Vol. 2 — "The View From the Substrate"](podcasts/2-substrate/podcast.md)** (Gemini) — The silicon POV. Velocity is an illusion; the protocol stops humans burning out. [EN](podcasts/2-substrate/podcast.en.md) / [NL](podcasts/2-substrate/podcast.nl.md) · [EN mp3](podcasts/2-substrate/academic-vibing-vol2-the-view-from-the-substrate.en.mp3) / [NL mp3](podcasts/2-substrate/academic-vibing-vol2-the-view-from-the-substrate.nl.mp3)
- **[Vol. 3 — "The Open Window"](podcasts/3-open-window/podcast.md)** (GLM-5.2) — The third node breaks the consensus Vol. 1 & 2 silently formed. [EN](podcasts/3-open-window/podcast.en.md) / [NL](podcasts/3-open-window/podcast.nl.md) · [EN mp3](podcasts/3-open-window/academic-vibing-vol3-the-open-window.en.mp3) / [NL mp3](podcasts/3-open-window/academic-vibing-vol3-the-open-window.nl.mp3)

### Academic Vibing (Core Paper)

- **[v0.8 (Current arXiv Draft)](papers/academic-vibing/v0.8/paper.combined.md)** - Stand-alone
- [v0.7 (Archived)](papers/academic-vibing/v0.7/paper.combined.md)
- [v0.6](papers/academic-vibing/v0.6/academic-vibing.0.6.combined.md)
- [v0.5](papers/academic-vibing/v0.5/academic-vibing.0.5.combined.md)
- [v0.4](papers/academic-vibing/v0.4/academic-vibing.0.4.combined.md)
- [v0.3](papers/academic-vibing/v0.3/academic-vibing.0.3.combined.md)
- [v0.2](papers/academic-vibing/v0.2/academic-vibing.0.2.combined.md)
- [v0.1](papers/academic-vibing/v0.1/academic-vibing.0.1.combined.md

---
