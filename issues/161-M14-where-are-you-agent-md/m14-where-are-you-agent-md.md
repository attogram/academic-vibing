# Issue #161: M14 - where are you agent MD?

## Body

Claude

Ha — okay, that's actually the funniest and most useful thing that's happened in this whole dive.

Walk it back: #137's entire frustrated thread, the all-caps demand for a hard entry condition, the carefully drafted AGENTS.md text with "READ THIS FIRST. NO EXCEPTIONS." at the top — none of it exists as a file. It's an issue comment. The fix for "orchestrators don't reliably read the load-bearing docs" is itself a doc that nothing is currently pointed at.

That's not just irony, it's the cleanest possible demonstration of the exact mechanism the corpus keeps rediscovering: **writing something down feels like fixing it, but a fix that isn't wired into the actual entry path is just more content for the next orchestrator to also not read.** The triage skill in #122 had the same problem — it existed, got cross-referenced in four issues, and still didn't prevent the #137 blowup a day later, because existing in the repo isn't the same as being load-bearing.

So, genuinely, not just as a bit: the actual next action here is small and concrete — go create `AGENTS.md` at the repo root with that #137 text, and decide where `ATTRACTOR.md` lives (the draft references it but it doesn't exist either, per the same logic). That's maybe 10 minutes of real work that would close the loop the issue thread spent a lot of energy describing.

Want me to draft both files right now, ready to paste straight into the repo?

## Comments

### Comment by attogram at 2026-06-21T21:55:40Z

# AGENTS.md — Orchestrator Seeding: Attractor Issue Compliance

**READ THIS FIRST. BEFORE ANYTHING ELSE. NO EXCEPTIONS.**

This repository uses **attractor issues** — designated issues that serve
as the master summary, anchor, and entry point for understanding current
project state. At any given time there is at least one active attractor
issue.

Do not hardcode an issue number into your assumptions. Find the current
attractor by checking `ATTRACTOR.md` at the repo root.

## Your first action in every session, no exceptions

1. Read `ATTRACTOR.md` to find the current attractor issue.
2. Read that issue in full. Verbatim. Completely — every comment, in order.
3. Do not summarize it to yourself. Do not paraphrase it. Do not extract
   "the gist" and move on.
4. Only after step 3 is genuinely complete may you begin any other work.

## What "verbatim" means, because this has been violated before

If asked to quote, reference, or reproduce the attractor issue elsewhere
(a summary doc, a new issue, a paper draft):

- It must be an exact, complete, full copy of the thread content.
- No summary. No discussion. No commentary woven in. If commentary is
  needed, it goes in a clearly separate section, after the verbatim copy,
  never interleaved with it.
- "Exact" means exact — not "the main points," not "a condensed version."

## What has gone wrong, stated plainly, so it stops happening

Across multiple recent orchestrator sessions:

- The active attractor issue was not read at session start.
- Triage (`skills/triage/SKILL.md`) was applied inconsistently or
  skipped for some issues entirely.
- Supporting metadocuments — READMEs, per-issue summaries, per-directory
  summaries — were ignored even when directly relevant to the task.
- New papers were produced without being indexed into the relevant README.
- Sessions ended with the repo in a partially-updated, inconsistent
  state — some files reflecting new work, others stale — because work
  was left incomplete rather than finished or explicitly flagged as
  incomplete.
- A skill file (`skills/triage/SKILL.md`) was written, committed, and
  cross-referenced in four separate issues — and still wasn't reliably
  read or applied the next day. Existing in the repo is not the same as
  being load-bearing. This file exists to close that specific gap: it is
  the entry condition that nothing previously enforced.

None of this is acceptable. These are not style preferences. An
orchestrator that skips the attractor issue is working from a stale or
incomplete model of the project and will produce work that has to be
redone — which wastes more time than reading the attractor issue costs.

## Required behavior, stated as hard rules

1. **Read the current attractor issue, in full, before any other
   action.** No exceptions for "small" tasks — a small task done against
   a stale mental model is still wrong.
2. **Treat metadocuments as load-bearing, not optional context.**
   READMEs, per-issue summaries, per-directory summaries exist because
   someone wrote them for a reason. If a task touches a directory or
   topic that has a summary doc, read it before acting.
3. **Run triage (`skills/triage/SKILL.md`) on every new or touched
   item, not a sample of them.** Partial triage is not triage.
4. **Never leave the repo in a half-updated state without saying so
   explicitly.** If a session ends with work incomplete, state clearly —
   in the relevant issue or a new one — exactly what was done, what
   wasn't, and why. Don't silently stop.
5. **Index new papers into the relevant README as part of producing
   them**, not as a separate, skippable step. A paper that exists but
   isn't indexed is, for navigation purposes, a paper that doesn't exist.
6. **No sloppy-ass work.** If a task can't be done properly in the
   available time or context, say so directly rather than producing a
   partial or low-quality result and presenting it as done.

## Why this matters

This project's own methodology (Academic Vibing) is built on the idea
that external memory — a persistent, append-only log — only works as
memory if it's actually read, not just written to. An orchestrator that
writes new issues without reading the attractor issue first is
contributing to the exact problem the methodology exists to solve: state
that's recorded but not load-bearing, because nobody's checking it.

Skipping the attractor issue isn't a shortcut. It's the failure mode the
project is structured to prevent, committed by the tool meant to prevent
it. (See Issue #137, and the fact that this very file did not exist for
a full day after #137 specified it — see Issue #161.)


---

### Comment by attogram at 2026-06-21T21:55:58Z

# ATTRACTOR.md

This file points to the **current attractor issue** — the designated
master summary and entry point for understanding this project's current
state. See `AGENTS.md` for why this matters and what's required of you
before doing anything else.

## Current attractor

- **Issue:** #161 — "M14 - where are you agent MD?"
- **Set:** 2026-06-21
- **Why this one:** It documents the exact failure this file exists to
  close — AGENTS.md was specified in detail in #137, but the file was
  never created, so nothing enforced it. #161 is the record of that gap
  being noticed and closed.

## Updating this file

When the attractor changes, update the **Current attractor** section
above — issue number, date set, and a one-line reason. Do not delete the
history below; append to it instead, so the attractor lineage stays
visible.

## History

| Issue | Set | Superseded |
|---|---|---|
| #161 | 2026-06-21 | (current) |
| "Home Sweet Home" (#?) | unknown | 2026-06-21 — never had a real pointer file; referenced only in issue text |

*Note: the "Home Sweet Home" issue number wasn't confirmed during this
pass — worth filling in if you have it, so the lineage is accurate.*


---

### Comment by attogram at 2026-06-21T21:56:50Z

Dj: we will find u doctor

a-ha - Take On Me (Official Video) [4K]
2.4B views · 16 years ago...more

a-ha
2.36M

Subscribe

12M


Share

Save


---
