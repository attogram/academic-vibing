# Issue #162: M15 - The Music Advisor

## Body

Claude

This one I want to apply the corpus's own triage skill to directly, since it's a clean test case.

**TRIAGE: F11 — The Soundtrack Protocol**
→ **VERDICT: OUTLET, and worth flagging on verification grounds, not just vibe grounds**
→ **WHY:** Two citations are doing real work to make this *sound* like Question 1 has been cleared ("Sallinen et al. 2011," "Blood & Zatorre 2001") when nothing here confirms they were actually checked. That's worth being direct about rather than letting it slide because the rest of the piece is funny.

Let me actually check one before saying anything more — that's the whole point of the skill.

Confirmed what I suspected: I can't find a "Sallinen et al. 2011" paper on rhythmic acoustic input and autonomic regulation. Real research in this space exists — and some of it does support the general idea that music modulates ANS/cortisol — but that specific citation, attributed that specifically, isn't surfacing. Same likely story for "Blood & Zatorre 2001" (there's a real, often-cited 2001 Blood & Zatorre PNAS paper on music and dopamine/reward circuitry, so that one's probably a real paper being used loosely — but "blocks external interruptions and cognitive drift" is a stretch beyond what that paper actually showed, which was about pleasurable music activating reward regions, not about interruption-blocking).

So, applying the triage skill for real:

**TRIAGE: F11 — The Soundtrack Protocol**
→ **VERDICT: OUTLET — and flag the citations specifically, not just the vibe**
→ **WHY:** Fails Question 1 cleanly. "Real academic weight backed by scholarly evidence" is asserted in the issue's own opening line, but the Sallinen citation doesn't verify, and Blood & Zatorre is real-paper-wrong-claim — a genuine citation pointed at a conclusion it doesn't actually support. That's a more specific problem than "this is silly" — it's the corpus's own Question 1 failure mode, happening with citations this time instead of math notation.
→ **The good part, kept separate:** The actual underlying idea — that ambient sound functions as cognitive infrastructure during long sessions, and different sound profiles suit different task types — is plausible and lines up with real (if more modest) literature on music and arousal regulation. That part could become paper-grade *if* it dropped the fake citations and either found real ones or just said "anecdotally, this is what we noticed."

Practical note: the music-advisor skill file is fun and harmless as OUTLET — no objection there. The only thing worth fixing is the two citation names sitting in the issue text dressed as "scholarly evidence," since that's exactly the pattern AGENTS.md and the triage skill now exist to catch — and this issue predates both fixes by a couple of days, so it's a clean before-case.

Want me to find real citations that actually support the soundtrack idea, in case you want to use it in the paper later — or leave it as pure outlet and move on?

## Comments

### Comment by attogram at 2026-06-21T22:00:21Z

Dj: rock on

a-ha - Take On Me (Official Video) [4K]
2.4B views · 16 years ago...more

a-ha
2.36M

Subscribe

12M


Share

Save


### Comment by attogram at 2026-06-21T22:03:28Z

Dj: wake me up dude

Wham! - Wake Me Up Before You Go-Go (Official Video)
572M views · 16 years ago
#GeorgeMichael #WakeMeUpBeforeYouGoGo #LastChristmas
...more

WHAM!
2.14M

Subscribe


### Comment by attogram at 2026-06-21T22:03:47Z

Ha, you actually filed it — straight into the repo as a real issue, citation-check and all. Now it's load-bearing instead of just chat output, which is exactly the standard #137/AGENTS.md set.

To close the actual loop you opened: yes, I'll go find real citations for the soundtrack idea so it can graduate from outlet to paper-grade if you want it there eventually.

Good — there's real, citable literature here, and it's actually more nuanced (and more interesting) than the original made-up version. Here's what's genuinely usable for the paper, properly sourced:

**Real, verifiable claims to swap in:**

1. A 2022 systematic review found that research on background music and cognitive task performance is "marked by inconsistent methods and inconclusive findings" [Sage Journals](https://journals.sagepub.com/doi/10.1177/20592043221134392) — important to cite *this* honestly rather than overclaiming, since it's the actual state of the field.

2. A 2025 study found that slow-tempo music improved attentional orienting, helped focus on targets while ignoring distractors, lowered heart rate, and increased feelings of relaxation [Annals of the New York Academy of Sciences](https://nyaspubs.onlinelibrary.wiley.com/doi/full/10.1111/nyas.70049) — this is a real, recent, task-specific finding that maps cleanly onto your "Axis C: Ambient Horizon / wind-down" category.

3. On the task-matching idea specifically: fast background music has been linked to better retention of simple information, and upbeat music to phonemic fluency advantages [Springer](https://link.springer.com/article/10.1007/s41809-024-00144-8) — while other research found fast-tempo music negatively impacted memory retention [Auctores](https://auctoresonline.org/article/role-of-music-in-improving-focus-and-memory-retention-in-academic-students) , and a review found lyrics specifically impede memory-related tasks and reading comprehension, with instrumental music having less impact [Amazonaws](https://terra-docs.s3.us-east-2.amazonaws.com/IJHSR/Articles/volume7-issue2/IJHSR_2025_72_91.pdf) .

4. The most useful single fact for your "Axis A/Axis C" split, if you want it: lyrics in a foreign or unintelligible language don't produce the same interference as lyrics in a language the listener understands [Amazonaws](https://terra-docs.s3.us-east-2.amazonaws.com/IJHSR/Articles/volume7-issue2/IJHSR_2025_72_91.pdf) — that's a real, specific, citable reason your Japanese math-rock picks for hyper-focus work might genuinely function differently than English vocal tracks would.

**Honest bottom line for the paper:** the literature doesn't support "rhythmic acoustic input prevents cortisol spikes from AWS errors" as a settled fact — it supports "background music's cognitive effects are task-dependent and still debated, with some real evidence that tempo/lyrics/familiarity matter in specific, measurable ways." That's a weaker but *true* claim, and it's still enough to ground the Axis A/B/C task-matching structure without fabricated citations.

Want me to rewrite the F11/skill file's "Scholarly Evidence" section with these real sources, so it's ready to actually graduate to PAPER-READY rather than staying flagged?

### Comment by attogram at 2026-06-21T22:15:17Z

Dj says good night

Tedeschi Trucks Band & Leon Russell – “Feelin' Alright” [Feat. Dave Mason, Anders Osborne]
832K views · 10 months ago
#TedeschiTrucksBand #FeelinAlright #MadDogsAndEnglishmen
...more

Tedeschi Trucks Band
228K

Subscribe

8.8K


Share

Save

