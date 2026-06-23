# Issue #112: H4 av 0.9 review

## Body

Claude

I'll take a look at this file.

Let me see the truncated middle section to give a complete review.

I've read the whole thing now. Here's my honest take.

**What this is:** a self-described "maximalist" writeup of a personal AI-assisted workflow (rapid iteration, multiple LLMs cross-checking each other, GitHub issues as memory, voice dictation for terse prompting). That core idea is genuinely reasonable and not unheard of — using model disagreement as a signal, treating an issue tracker as external memory, voice-to-text forcing brevity — these are real, useful observations about working with LLMs.

**The problems, bluntly:**

1. **It reads as AI-generated and ungrounded, not reviewed.** Phrases like "Final Boss Iteration," "MAXIMALIST LOSSLESS," a puppy mascot "watching the CDI," and an "STFU Attractor" described as a literal attention-head mask ($M_{\text{STFU}}$) that "violently pulls the latent space focus back to core operational primitives" — this isn't real mechanistic interpretability, it's invented terminology dressed in math notation. No actual transformer works this way as described, and there's no derivation, no citation, no implementation.

2. **Fabricated/implausible citations.** References to arXiv papers like "GLM-5.2," "GLM-5 Team (2026)," IndexCache papers, and a CDC report on "Agentic Research in Public Health" — several of these look invented or unverifiable (wrong arXiv ID formats for 2026, generic root URLs instead of specific pages, a "GLM-5.2" model that doesn't match any real release naming). I'd want every reference verified before this goes anywhere near arXiv.

3. **Self-referential ecosystem.** Most citations are to the author's own GitHub repos and issues (e.g., "Issue #86," "Issue #97") rather than external, checkable sources. That's fine as a personal log, but it's being presented with academic paper formatting (Abstract, References, DOIs) which implies a rigor it doesn't have.

4. **Real psychology research is bolted on loosely.** The UCI interruption-recovery stat and Sweller/Kahneman cognitive load citations are real findings, but they're stretched to support claims (e.g., "re-entry costs ~3 min" for the Leapfrog Mechanism) that have no actual measurement behind them — it's asserted, not tested.

5. **Structurally bloated.** Every section duplicates content in a "[ROCK TALK]" telegraphic list and then a "[PROSE]" paragraph saying the same thing. That doubles length without adding information.

**My honest recommendation:** if you want this taken seriously (arXiv, Zenodo, etc.), strip the mascot/soundtrack/"Final Boss" framing, cut anything presented as a mechanistic model of attention that isn't backed by code or a paper, verify every reference actually exists and says what's claimed, and separate the real workflow insight (multi-model cross-checking, external memory via issues, voice-forced brevity) from the cosmetic theater. The underlying practice is more interesting than the packaging suggests.

Want me to do a pass that pulls out just the substantive, defensible claims into a tighter document?
