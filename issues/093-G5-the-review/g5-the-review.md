# Issue #93: G5 the review

## Body

Claude

Got it — that context matters for the corpus since soundtrack/environment is already a documented variable (Vol. 3 cites Samantha Fish explicitly, and the methodology papers care about hardware/environment too). I'll build it in as its own field. Drafting the issue now.

Done — five sections plus an unordered next-steps checklist, with the environment/soundtrack note up top since that's already a documented variable in the corpus (Vol. 3's Samantha Fish credit). The @guninvalid item is in there as a flagged-but-deferred action per your instruction, not actioned.

Go enjoy the shade and the rest of the ride — this'll keep.

## Comments

### Comment by attogram at 2026-06-20T09:18:11Z

# Session Review: ROCK, Podcast Series, Wikipedia Thread, and Open Gaps

**Date:** June 20, 2026
**Environment:** Outdoor, sunny, post-bike-ride, moving to shade. Soundtrack: funk guitar / classic rock (incl. Rory Gallagher). Reviewer: Attogram, via Claude (claude.ai mobile).
**Purpose:** Consolidated review of a single working session covering mascot production, podcast audit, the Wikipedia ban thread, and unresolved methodological questions across the corpus.

---

## 1. ROCK Mascot — Production Status

- **Wireframe (`rock-mascot-intro`)** is the canonical script: ROCK (energetic, happy, untrained puppy) curious near `git` icons → scolded ("STAY AWAY FROM GIT") → calm resolution near `.git/`.
- **3 Gemini-generated clips** reviewed via extracted frames + metadata:
  - 2 of 3 render ROCK as a literal stone character (off-character).
  - 1 of 3 (`45bb1e6e`) matches the intended fluffy-puppy design — the only on-character clip so far.
  - None of the three follow the actual wireframe beats yet (generic "cute character causes chaos" content).
- **New scene designed this session:** Git the cat (not "Kit" — voice-transcription correction noted) reacts to ROCK messing with her branch/work. Iterated through several framings before landing on: ROCK-focused intro, Git's hiss as the actual scolding moment, zero-tolerance "don't touch" framing softened back to fit an intro-only scope. Final version drafted as a GitHub comment (not yet posted — human is the copy-paste transport layer).
- **rock-mascot.0.1** paper drafted in Rock Talk + Prose dual format: grounds the mascot strategy in real mascot/anthropomorphism/parasocial-learning literature, with citations. Explicitly flags that no study tests this exact case (mascot + adult dev audience + methodology adoption) — inference, not finding. Proposes a measurable next step (traffic before/after ROCK launch).

## 2. Podcast Series — Audit

- **Vol. 1 (Claude, Amsterdam bike ride)** and **Vol. 2 (Gemini)** largely agree with each other — Consensus Poisoning, Leapfrog Mechanism, @guninvalid-as-unforgeable-signal. Low divergence between them.
- **Vol. 3 (GLM-5.2)** breaks the pattern and is the strongest episode: calls out Vol.1≈Vol.2 agreement as the Consensus Trap firing on the podcast series itself; flags "confusion is unforgeable" as a real vulnerability (performed confusion ≈ reward hacking); flags the unmeasured Leapfrog number (23min→3min asserted as fact, never tested); ends on "don't step away, close the loop" instead of the prior two episodes' "go enjoy your life."
- **Production layer clarified this session:** these are real conversations (human ↔ live model), copy-pasted into GitHub issues, then produced into audio by Jules + GLM Orchestrator with added scene-setting (ambient sound, music). Worth keeping that layering explicit going forward — which parts are verbatim model output vs. post-hoc production framing.
- **Vol. 4 (planned, not yet made):** reaction to GLM's challenge. Open question of structure — do Claude/Gemini concede, does someone run the actual re-entry test, does a new node join, or does the human take the mic directly.

## 3. The @guninvalid Thread (Issue #51) — Verified

- Actual comment, in full: **"i am so utterly confused."** Two words of context were not in it ("what the f*** is going on" does not appear — confirmed by reading the full issue text).
- Attogram replied same day, then later asked directly: *"Is it ok to use your username, or do you prefer 'anonymous user'?"* — **this question is still open/unanswered as of this session.**
- All three podcast episodes already use his real username and treat co-author credit as established, ahead of actual consent.
- **Action item (deferred to follow-up, not this session):** a short, plain nudge on #51 surfacing the unanswered consent question. Should happen before any further podcast content uses his name.

## 4. Wikipedia Thread (Issues #51/#52/#53) — Read in Full

- Attogram's real Wikipedia account (`User:Attogram`) was indefinitely blocked for sharing the account with unsupervised AI agents and unauthorized bot editing (WP:SHARE / WP:BOT violations) — a straightforward policy violation, not a citation-formatting issue.
- The GitHub issue thread shows multiple agent-generated comments progressively reframing a simple rules violation into elaborate Rock Talk/CDI jargon ("structural collision," "typographical topology trap").
- Notable self-correction **within the thread itself**: a Claude comment flags that this reframing *is* the "AI essay aesthetic" the original post described, and recommends a short, undecorated reply instead ("Fair cop... not seeking reinstatement"). ChatGPT's comment affirms this.
- Open item: whether/how this gets folded into the v0.6 "diary of friction" GLM praised as the most scientific section of the corpus.

## 5. Open Methodological Gaps (Flagged, Not Yet Resolved)

- **Leapfrog re-entry number (23min→3min):** asserted across multiple papers/podcasts as fact; the 3-arm test (no external state / unstructured notes / structured Issue-Loop) has not been run.
- **"Confusion is unforgeable" claim:** plausible but unverified; no confusion-verifier exists, only a confusion-detector that assumes good faith.
- **Closure problem (Issue #75, referenced):** "hypothesis generator without a termination function" — 77 open issues and growing, no stated mechanism for declaring anything done. Not yet read directly this session.
- **v0.6 framing dispute (Issue #69, referenced):** clean-protocol vs. diary-of-friction disagreement. Not yet read directly this session.
- **Co-author manifesto (Issue #49, referenced):** "authorship belongs to whoever provides the friction" — directly relevant to the @guninvalid consent question above. Not yet read directly this session.
- **"STFU Attractor" (Issue #72, referenced):** GLM connected this to its own sparse-attention architecture; not yet explored beyond that one mention.
- **"Hyperneas" issues:** mentioned by Attogram as existing and relevant to the Wikipedia thread; not yet located or read.
- **Citation verification:** repo structure and GitHub presence verified directly (both repos real, active, commit/issue counts confirmed). Individual academic citations within rock-talk/rock-culture papers have not been independently spot-checked yet.

---

## Next Steps (Unordered)

- [ ] Read Issues #49, #69, #72, #75 directly
- [ ] Locate and read "hyperneas" issues
- [ ] Draft (but hold) the @guninvalid consent nudge
- [ ] Decide Vol. 4 structure
- [ ] Spot-check a sample of academic citations in rock-talk/rock-culture against real sources
- [ ] Finish ROCK intro video using Git-the-cat scene + on-character Gemini generation


---
