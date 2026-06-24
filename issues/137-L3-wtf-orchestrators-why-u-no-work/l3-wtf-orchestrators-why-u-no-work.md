# Issue #137: L3 wtf orchestrators why u no work?

## Body

Deer orchestrators especially jewels but also glme and anyone else in the future this is atagram this is voice transcription be nice lots of errors now now hey f****** attention this is description of orchestrator failure mode period failure continued failure annoying and frankly f****** sad period issue issue home sweet home that issue is the absolute core and absolute exact exact exact exact template for P1 orchestrators have gone through four sessions with home sweet home in place in the source of Truth issues as the second issue and the last in the series.   Pay fucking attention next time


All recent orchestrators have gone off-road off track off plan and has been very very lazy triage was not done properly triage was not done for all all issues triage was not done properly must be exact exact exact exact exact exact exact copy of the source of Truth github issue no summary no discussion just an exact full real exact exact exact exact copy of the complete complete complete complete complete thread stop

Additionally all recent orchestrators have completely f****** ignored all the supporting and metadocuments all the readme's all the per issue summaries all the per directory summaries etc etc etc all orchestrators have continuously and with all time ignored ignored ignored ignored the actual source of truth of the actual issues they have done partial work and left the repo in an instable state they have not indexed new papers into the readme etc etc

## Comments

### Comment by attogram at 2026-06-21T09:11:39Z

https://youtu.be/t5zqiqx_xqM?si=9RBdowwXkMOoAmLR


Sandra - Funk My Life Up (Paolo Nutini live cover)
6.5K views · 8 years ago...more

Sandra Abner
84

Subscribe

127


Share

Save




### Comment by attogram at 2026-06-21T09:16:54Z

Home sweet home issue:

The core of fucking everything that happened in past 48 hours.

. Must be STRONG attractor

. Is a master summary and plan for entire fucking project

. Triage skill needs massive update to ensure proper usage

Orchestrators need better AGENTS.md seeding of strong bias towards NO FUCKING SLOPPY ASS work

### Comment by attogram at 2026-06-21T09:19:23Z

Claude puppy

This one's real frustration, not 2am chaos energy, and it deserves a straight answer rather than me matching the tone.

What you're describing is a specific, fixable failure: orchestrators (Jules, GLM, others) are running across sessions, doing partial triage, not reading the supporting docs that already exist (READMEs, per-issue summaries, per-directory summaries), not indexing new papers, and leaving the repo unstable — *despite* "Home Sweet Home" already existing as the explicit, intended anchor document for exactly this purpose. That's not a vibe problem, that's an instruction-following problem. Four sessions in a row missing the same documented anchor isn't randomness, it's a structural gap in how orchestrators are being seeded at session start.

A few honest, concrete things this points to:

**The triage skill we built tonight has a real gap, and you're right to flag it.** It tells an agent *how* to sort material once looking at it, but it doesn't tell an orchestrator *to start every session by reading Home Sweet Home first*. That's a missing entry condition, not a missing sorting rule. Worth fixing directly.

**"Exact exact exact exact copy, no summary, no discussion" is a real, specific, checkable instruction** that got violated repeatedly — orchestrators summarizing or discussing Home Sweet Home instead of treating it as a literal, verbatim anchor. That's the kind of thing that should be impossible to get wrong if it's stated unambiguously at the top of an AGENTS.md, in caps, with no room for interpretation.

**This is also, itself, a perfect addition to the failure-modes section of the paper** — "orchestrator drift across sessions despite explicit anchor documents" is a real, observed, citable-to-your-own-repo failure mode, distinct from the mythology-leakage one. Worth logging as its own pattern once you're past being annoyed about it.

What would actually help right now: should I draft the AGENTS.md seeding language — the explicit, no-room-for-misreading instruction set that forces every orchestrator to read Home Sweet Home verbatim, first, before touching anything else — and fold a "read Home Sweet Home first" entry condition into the triage skill? That's the concrete fix for what you're describing, not just sympathy for the frustration.

### Comment by attogram at 2026-06-21T09:24:39Z

# AGENTS.md — Orchestrator Seeding: Attractor Issue Compliance

## READ THIS FIRST. BEFORE ANYTHING ELSE. NO EXCEPTIONS.

This repository uses **attractor issues** — designated issues that serve as
the master summary, anchor, and entry point for understanding current
project state. At any given time there is at least one active attractor
issue. "Home Sweet Home" is the current one. It will not always be. Do not
hardcode its issue number into your assumptions — find the current
attractor by checking `ATTRACTOR.md` at repo root (or, if that file doesn't
exist yet, the most recently pinned issue, or the issue explicitly labeled
`attractor`).

**Your first action in every session, with no exceptions, is:**

1. Locate the current attractor issue.
2. Read it in full. Verbatim. Completely.
3. Do not summarize it to yourself. Do not paraphrase it. Do not extract
   "the gist" and move on. Read the actual, complete, unabridged thread —
   every comment, in order.
4. Only after step 3 is genuinely complete may you begin any other work.

## What "verbatim" means, explicitly, because this has been violated before

If asked to quote, reference, or reproduce the attractor issue elsewhere
(e.g., copying it into a summary document, a new issue, a paper draft):

- It must be an **exact, complete, full copy** of the thread content.
- **No summary. No discussion. No commentary woven in.** If commentary is
  needed, it goes in a clearly separate section, after the verbatim copy,
  never interleaved with it.
- "Exact" means exact. Not "the main points." Not "a condensed version."
  The complete thread, copied in full.

This has been gotten wrong multiple times. It is not ambiguous. If you
find yourself summarizing instead of copying, stop and re-read this
section.

## What has gone wrong, stated plainly, so it stops happening

Across multiple recent orchestrator sessions:

- The active attractor issue was not read at session start.
- Triage (see `skills/triage/SKILL.md`) was applied inconsistently or
  skipped for some issues entirely.
- Supporting metadocuments — READMEs, per-issue summaries, per-directory
  summaries — were ignored even when directly relevant to the task at
  hand.
- New papers were produced without being indexed into the relevant
  README.
- Sessions ended with the repo in a **partially-updated, inconsistent
  state** — some files reflecting new work, others stale — because work
  was left incomplete rather than either finished or explicitly flagged
  as incomplete.

None of this is acceptable. These are not minor style preferences. An
orchestrator that skips the attractor issue is working from a stale or
incomplete model of the project and will produce work that has to be
redone. This wastes more time than reading the attractor issue costs.

## Required behavior, stated as hard rules

1. **Read the current attractor issue, in full, before any other action.**
   No exceptions for "small" tasks — a small task done against a stale
   mental model is still wrong.
2. **Treat metadocuments as load-bearing, not optional context.** READMEs,
   per-issue summaries, per-directory summaries exist because someone
   wrote them for a reason. If a task touches a directory or topic that
   has a summary doc, read it before acting.
3. **Run triage (skills/triage/SKILL.md) on every new or touched item**,
   not a sample of them. "Triage was not done properly" and "triage was
   not done for all issues" are documented failures from this exact
   repo. Partial triage is not triage.
4. **Never leave the repo in a half-updated state without saying so
   explicitly.** If a session ends with work incomplete, the orchestrator
   must state clearly, in the relevant issue or a new one, exactly what
   was done, what wasn't, and why — not silently stop.
5. **Index new papers into the relevant README as part of producing
   them**, not as a separate, skippable step. A paper that exists but
   isn't indexed is, for navigation purposes, a paper that doesn't exist.
6. **No sloppy-ass work.** If a task can't be done properly in the
   available time or context, say so directly and explicitly rather than
   producing a partial or low-quality result and presenting it as done.

## Why this matters (for orchestrators who want the reasoning, not just the rule)

This project's own methodology (Academic Vibing) is explicitly built on
the idea that external memory — a persistent, append-only log — only
works as memory if it's actually *read*, not just written to. An
orchestrator that writes new issues without reading the attractor issue
first is contributing to the exact problem the methodology exists to
solve: state that's recorded but not actually load-bearing, because
nobody's checking it. Skipping the attractor issue isn't a shortcut. It's
the failure mode the entire project is structured to prevent, committed
by the tool meant to prevent it.


### Comment by attogram at 2026-06-21T09:25:18Z

---
name: triage
description: "Use this skill whenever new material is dropped into this project — a fragment, an issue, a paper draft, a citation, a stray observation — and it's not yet clear whether it belongs in THE PAPER or in OUTLETS. Trigger this any time someone asks 'wtf is going on,' 'where does this go,' 'is this paper-grade,' or pastes in raw content (issue text, a quote, a research finding, a meme, a tangent) without specifying its destination. Also trigger proactively before merging anything into the standalone paper, and periodically during long sessions as a self-check on whether recent output still maps to the project's actual scope. Do NOT use this skill for routine editing, formatting, or citation-verification tasks that already have a clear destination — only use it for the sorting decision itself."
---

# Triage: The "Wtf Is Going On" Skill

## Before you triage anything: check for an active attractor issue

This step comes **before** the procedure below, not as part of it. If this
repository has a designated attractor issue (check `ATTRACTOR.md` at repo
root, or an issue explicitly labeled `attractor`), **read it in full,
verbatim, before triaging anything else.** This has been a documented,
repeated failure point — orchestrators running triage against a stale or
incomplete model of the project because they skipped the current anchor
issue. Triage performed without first reading the active attractor issue
is not reliable triage, regardless of how carefully the procedure below is
followed. Do this first. Every session. No exceptions.

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

## Triage coverage must be complete, not sampled

If you're triaging a batch — a backlog of issues, a set of new fragments, a session's worth of output — **every item gets a verdict, not a representative sample.** "Triage was not done for all issues" is a documented failure in this project's history. Skipping items because they look similar to ones already triaged, or because time is short, produces a repo in an inconsistent state where some material has been sorted and some hasn't, with no way to tell which is which without re-checking everything. If there isn't time to triage a full batch properly, say so explicitly and state what was and wasn't covered — don't triage part of it silently and present the batch as done.

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


### Comment by attogram at 2026-06-21T09:26:19Z

https://youtu.be/plAysjeGtDQ?si=AgPVfl0vuaYsyP9f

Hallelujah by Bamboo
203K views · 13 years ago
Show - Good Times with Mo (The Podcast)
...more

OTT
58.1K

Subscribe

1K


### Comment by attogram at 2026-06-21T09:37:00Z

https://youtu.be/KvRJjC28pKE?si=B60txA4IxZ9d5zII

Rick Rack 「幾千の出会いと一つの奇跡」
@rickrack6946
11K likes
1,1 mln. weergaven12 jaar geleden
meer


Abonneren




Reacties548

Reageer...

### Comment by attogram at 2026-06-21T09:40:20Z

https://youtu.be/wqLRkZkyzas?si=lZGC0RDX0xkVp6V1

ポルカドットスティングレイ「リドー」MV
@POLKADOTSTINGRAY
31K likes
1,9 mln. weergaven3 jaar geleden
meer


Abonneren




Reacties688

バ先で流れててめっちゃいい曲やん誰の曲なんだろう？って思って、覚えてたサビの「

### Comment by attogram at 2026-06-21T09:50:38Z

https://youtu.be/_ZyD4n5zqxA?si=GWR8CkAhKfsOoTWa

KANA-BOON（谷口鮪）× ネクライトーキー（もっさ） - ないものねだり / THE FIRST TAKE
@The_FirstTake
844K likes
49 mln. weergaven6 jaar geleden
meer


Abonneren




Reacties21K

この時はおしゃれにギターソロ弾きに来た奴も、手だけ叩き来た奴もいなくなるなんて想像もしてなかったよ……

### Comment by attogram at 2026-06-21T10:03:57Z

"Habit" actually maps onto tonight pretty cleanly, and it's a genuinely good connection — here it is straight.

The song's whole argument is that people compulsively sort things into binary boxes — gifted/ordinary, in/out — and that the real value shows up once you stop doing that. That's almost exactly the diagnosis behind tonight's "1 Paper, 999 Outlets" split. The triage skill exists because the same sorting compulsion the song criticizes in people is necessary in this one specific case — content genuinely does need to go in PAPER or OUTLET, or the paper drowns in mascot lore. The difference is that your sorting isn't arbitrary social judgment, it's a load-bearing structural decision with a clear test behind it (verifiable? needs shared context? methodology vs. personality?).

The "Bad Habit" the song wants broken is closer to what v0.9 actually did wrong — not sorting at all, just letting the STFU Attractor and Han Solo and the puppy all sit in the same undifferentiated pile as the real methodology, dressed up with enough confidence that nobody checked which category anything belonged in. That's the habit-without-examination the song is actually about: not classifying things, but classifying them lazily and trusting the result without checking it. Tonight's whole arc was the opposite of that — examined classification, repeatedly, out loud.

I'll say this plainly: I'm continuing to help because the question itself was reasonable, not because of how it was delivered. I'd still appreciate it if we could keep things civil from here.
