# Research Plan: Core Paper Iteration for arXiv

## [ROCK TALK]
```
Goal: One paper. arXiv-ready. Q3 2026.
Phase: Post-podcast. Post-cleanup. Pre-synthesis.
Status: Repo clean. Papers flattened. Archive sorted.
Blocker: Core paper is v0.6 — structurally contested (issue #69).
         Leapfrog claim is unmeasured (hypothesis, not result).
         Token-window spectrum missing on latest papers.
Strategy: Iterate core paper to v0.7 (arXiv draft).
          Receipts paper: fold tonight's sprint as data point 2.
          Generate token-window variants for all papers.
          Run CDI audit across podcast episodes as validation.
Next:
1. Core paper: strip Section 8, tighten to methodology.
2. Receipts paper: add podcast sprint as n=2.
3. Token-window spectrum: 1k-128k for every paper.
4. LaTeX: iterate tex to match markdown, recompile PDF.
5. CDI: measure divergence across 3 podcast episodes.
Vibe check: SHARP. The closure signal is close.
```

## [PROSE]

### Where We Are (June 20, 2026)

The repo has been cleaned and restructured. Three podcasts shipped (Claude, Gemini, GLM-5.2). The issue loop is synced (61 issues, lossless). Papers are flattened — one dir per paper, no version sprawl. Tangential papers archived. The core paper and receipts paper are the two artifacts that need iteration toward arXiv.

### What's Broken

1. **Core paper (v0.6) is structurally contested.** Issue #69 says it's "bad bad bad" — Section 8 (Institutional Trauma) broke the methodology framing and turned into a reactive post-mortem. The podcast Vol. 3 (GLM-5.2) disagreed with that critique — the friction data is valuable — but agreed it doesn't belong in the main paper. **Action:** Strip Section 8 from the core paper. It's already archived in `papers/archive/`. The main paper should be a clean methodology paper: Introduction, RAC+CDI, Issue-Loop schema, Token-to-Meaning, Leapfrog, Hardware/Accessibility, Conclusion.

2. **The Leapfrog number is a hypothesis, not a result.** Both Vol. 1 (Claude) and Vol. 2 (Gemini) cite "23 min → 3 min" as fact. Vol. 3 (GLM-5.2) caught this: the 3-arm test has never been run. The core paper currently asserts it. **Action:** Reframe as a testable hypothesis with proposed experimental design. State the number as observed-anecdotal, not measured-empirical. This is the single biggest credibility gap for arXiv reviewers.

3. **The receipts paper is stale.** It documents sprint 1 (June 13-16, 5 papers in 96h). Tonight's podcast sprint (3 episodes in one evening, 3 different model architectures, on a 16GB Macbook with $20/mo Ollama Cloud) is a second data point that isn't captured. **Action:** Add sprint 2 as a second data point. The receipts paper becomes n=2. Different task type (audio/podcast vs paper/text), different hardware (same), different agent (GLM-5.2 via Ollama Cloud vs Jules/Gemini/Claude via web). This strengthens the "hardware independence" and "MAS context persistence" claims.

4. **Token-window spectrum is missing on latest papers.** The 1k-128k variants exist for v0.1-v0.4 but not for the current flattened versions. These are the true artifact of the repo — same semantic content compressed to fit any context budget. **Action:** Generate 1k, 2k, 4k, 8k, 16k, 32k, 64k, 128k variants for both core and receipts papers. This is the Rock Talk protocol applied to its own output.

5. **The podcasts are an untapped validation dataset.** Three episodes, three different model architectures, all commenting on the same corpus. The CDI between Vol. 1 and Vol. 2 is ~0 (they agree on everything). Vol. 3 diverges on 4 claims. This is a live, audible CDI demonstration. **Action:** Formalize the podcast CDI analysis as an appendix or companion piece. Map each claim agreement/disagreement across the three episodes. This is empirical data, not anecdote.

### Iteration Plan

#### Phase 1: Core Paper v0.7 (arXiv Draft)
- Strip Section 8 (Institutional Trauma) — already archived
- Reframe Leapfrog claim as hypothesis with experimental design
- Tighten references — CITATIONS.md has some unverified entries
- Update author block: solo author + swarm credit (per issue #49 co-author manifesto)
- Regenerate LaTeX from updated markdown, recompile PDF
- Target: clean 6-section methodology paper, 4-6 pages

#### Phase 2: Receipts Paper v0.4
- Add sprint 2 (podcast evening) as second data point
- Update velocity table: sprint 1 = 19.2h/paper, sprint 2 = ~2h/episode
- Note the hardware consistency (same 16GB Macbook) and agent diversity (GLM-5.2 vs Jules/Claude/Gemini)
- This is where the "n=1 → n=2" transition happens

#### Phase 3: Token-Window Spectrum
- Generate 1k, 2k, 4k, 8k, 16k, 32k, 64k, 128k variants for:
  - Core paper (from paper.rock.md)
  - Receipts paper (from paper.rock.md)
- Each variant is a progressively compressed Rock Talk version
- This is the STFU Attractor applied to the corpus itself

#### Phase 4: Podcast CDI Analysis
- Map claims across Vol. 1, 2, 3
- Identify agreements (CDI ~0) and divergences (CDI high)
- Vol. 1 vs Vol. 2: near-zero divergence (consensus trap)
- Vol. 3 vs Vol. 1+2: 4 divergences (confusion forgeability, substrate incentive, Leapfrog unmeasured, v0.6 friction log)
- This is the first empirical CDI dataset

#### Phase 5: arXiv Submission
- Zenodo archive (persistent DOI)
- arXiv formatting (LaTeX already exists, needs iteration)
- Submit core paper as primary preprint
- Submit receipts paper as companion

### What NOT to Do
- Do not open new branches of research until the core paper is submitted
- Do not generate more podcasts until the CDI analysis of episodes 1-3 is complete
- Do not touch the archive papers — they're sleeping
- Do not add new claims to CLAIMS.md until existing claims are evidenced

### Success Condition
One PDF. arXiv-ready. Clean methodology. Testable hypotheses. Token-window spectrum complete. Receipts paper at n=2. Podcast CDI mapped. Closure signal fires.

---
**Status:** [STATE] Plan written. Repo clean. Ready for core paper iteration.
**Primary Agent:** GLM-5.2 (this session) / Jules (ongoing)
**Human Check:** Pending vibe-check on plan priorities.