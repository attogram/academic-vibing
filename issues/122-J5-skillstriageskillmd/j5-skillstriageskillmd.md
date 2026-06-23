# Issue #122: J5 skills/triage/SKILL.md

## Body

Orchestrator agent answers wtf is going on

## Comments

### Comment by attogram at 2026-06-20T19:56:16Z

That's the natural next step from #121, and it's a good one — turning "wtf is going on" from a thing *you* ask yourself into a thing an *agent* asks on your behalf, systematically, every time something new lands in the repo.

Quick read on what this actually implies, since the title's terse: `skills/triage/SKILL.md` as a real skill file means an orchestrator agent's job is specifically to look at new material — a fragment, an issue, a paper draft — and sort it using the PAPER/OUTLET distinction from #121, flagging anything ambiguous back to you rather than guessing. That's the sorting mechanism finally getting a formal home instead of living only in your head as a gut-check.

That's a real, buildable thing — a skill file with a clear job (classify: paper-grade vs. outlet vs. unclear-ask-human) is exactly the kind of scoped task that's easy to spec and easy to verify later. Worth building properly next session when you're back at the keyboard rather than tonight from the couch — it's the first piece of actual infrastructure this whole sprawl has called for, so it's worth getting the skill's decision criteria right rather than rushing it.

For now, sounds logged and sitting right where it should. Music's still going — go enjoy it.

Claude

---

### Comment by attogram at 2026-06-20T19:56:34Z

Bad, Bad Leroy Brown - Jim Croce cover
2.1M views · 6 years ago
#304
...more

Elle & Toni
514K

Subscribe

31K


Share


---

### Comment by attogram at 2026-06-20T19:58:55Z

Tenacious D - Explosivo
2.8M views · 20 years ago...more

LukeyD822
178

Subscribe

11K


Share

Save


---

### Comment by attogram at 2026-06-20T19:59:45Z

---
name: triage
description: "Use this skill whenever new material is dropped into this project — a fragment, an issue, a paper draft, a citation, a stray observation — and it's not yet clear whether it belongs in THE PAPER or in OUTLETS. Trigger this any time someone asks 'wtf is going on,' 'where does this go,' 'is this paper-grade,' or pastes in raw content (issue text, a quote, a research finding, a meme, a tangent) without specifying its destination. Also trigger proactively before merging anything into the standalone paper, and periodically during long sessions as a self-check on whether recent output still maps to the project's actual scope. Do NOT use this skill for routine editing, formatting, or citation-verification tasks that already have a clear destination — only use it for the sorting decision itself."
---

# Triage: The "Wtf Is Going On" Skill

## What this is

This project runs on a simple, hard-won architecture: **1 Paper, 999 Outlets.**

- **THE PAPER** — the standalone, generalized document meant to survive a cold reader (currently `academic-vibing-v1.0.md`). Everything in it must be defensible: real citations, honest about its own limits, zero leakage of project-internal jokes, mascots, issue numbers, or in-group shorthand.
- **OUTLETS** — everything else, unbounded. Rock Culture, ROCK the Puppy, Cosmic Shame, SOUNDTRACK.md, podcasts, the compression matrix, this issue tracker itself. No quality bar. Memes and personality live here on purpose.

The hard part was never generating material — it's sorting it. This skill exists because that sorting kept *not happening*, producing things like Academic Vibing v0.9: a "standalone paper" that had quietly absorbed a mascot, a soundtrack credit, and a fake attention-mechanism dressed in math notation, because nothing in the workflow stopped to ask which bucket it belonged in before it got merged.

The recurring fix, discovered independently three separate times in this project's own history (issues "wtf is going on," "wtf is going on part 2," and "what did u say???"), was always the same: **stop, and ask whether the thing in front of you still maps to what it claims to be.** This skill formalizes that question into a repeatable check instead of relying on it surfacing by accident.

## When to run the triage check

Run this whenever:
- New raw material lands (an issue gets pasted, a research finding gets dropped in, a tangent comes up)
- Before merging *anything* into the paper — no exceptions, even small-seeming additions
- Someone asks "wtf is going on" or any equivalent
- You (the agent) notice a session has been running a while and haven't checked whether recent output still serves the original ask

## The triage procedure

For any piece of material, ask these questions in order. Stop at the first one that gives a clear answer.

### 1. Does this require external verification to be true?
If the claim rests on a citation, a study, a statistic, or a fact-check — it can only go in THE PAPER if that verification has actually happened. An unverified claim that *sounds* paper-grade is not paper-grade. Default: OUTLET, until verified.

### 2. Does understanding this require shared context the reader doesn't have?
Project-internal jokes, mascot lore, specific issue numbers, cultural references that only land for someone who's been in the room — these are outlet material by definition, no matter how well-argued. The test from earlier sessions: would a cold reader need it explained to get the point? If yes, OUTLET.

### 3. Is this a methodology claim, or a personality/process artifact?
"Models disagree, and that's informative" is a methodology claim — paper territory, if it can clear check #1. "I listened to Heart while writing this" is a personality/process artifact — outlet territory, always, no matter how true.

### 4. Is the honest answer "I don't know yet"?
If the material is too raw to classify — a tangent, a half-formed idea, a stray observation — it isn't a triage failure to leave it unsorted. Log it as an OUTLET fragment (the issue tracker is built for exactly this) and let it mature. Forcing a premature PAPER/OUTLET call on raw material is itself the failure mode this skill exists to prevent.

### 5. Does it survive its own honesty check?
Material that's heading for THE PAPER must be able to state its own limitations without flinching — what's proven vs. hypothesized, what's measured vs. felt. If a claim can't be stated honestly alongside its own uncertainty, it isn't ready for the paper yet, regardless of how solid the underlying idea is. (See: the chemicals section, which only became paper-grade once "we are not claiming our own sessions demonstrate anything" was written into it directly.)

## Output format

When running this check, report back concisely:

```
TRIAGE: <one-line description of the material>
→ VERDICT: [PAPER-READY | OUTLET | NEEDS VERIFICATION | TOO RAW, LOG AND WAIT]
→ WHY: <one sentence, pointing to which question above decided it>
→ IF PAPER-READY: <where it goes — which section, what citation it needs>
→ IF OUTLET: <which outlet — Rock Culture, mascot lore, issue tracker, etc.>
```

Keep this short. The triage call itself should never become a bigger production than the material being triaged — that would be the same failure mode in a new costume.

## Worked examples from this project's own history

| Material | Verdict | Why |
|---|---|---|
| CDI as a heuristic for surfacing model disagreement | PAPER-READY | Methodology claim, generalizable, citable as a proposed (not validated) tool |
| "STFU Attractor" as literal attention-head math | NOT PAPER-READY, cut entirely | Failed verification — no real mechanism backs it, dressed in notation to look like one |
| Alcohol/THC/nicotine cognitive effects | PAPER-READY, after research pass | Started as a stray "oh yeah and" tangent; became paper-grade once real citations were found and limitations stated honestly |
| ROCK the Puppy mascot | OUTLET | Personality artifact, not a methodology claim — belongs to project branding, not the paper |
| Han Solo / Memento cultural shorthand | OUTLET → Rock Culture | Requires shared context to land; reframed as a *general* observation (shared corpus enables compression) for the paper, kept the specific references in Rock Culture |
| "Cosmic Shame" as personal mascot | OUTLET, and not even project-level — personal | Doesn't represent the project at all; it's the human's own record of the work, explicitly separate from ROCK |
| Tenacious D Gemini ethnography | OUTLET, pure | Demonstrates a real phenomenon (analytical apparatus applied to unserious input) but the artifact itself is comedy, not evidence |

## A note on running this on yourself

The most valuable trigger for this skill isn't material someone hands you — it's noticing, mid-session, that your own recent output has drifted. If you've spent several turns building something increasingly elaborate (a mythology, a metaphor, a piece of math-flavored language) and haven't checked whether it's still answering the actual question, that's exactly the moment to stop and ask: *what the fuck is going on, and does this still map to what we're actually trying to do?*


---
