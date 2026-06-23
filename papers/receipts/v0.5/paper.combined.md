# Academic Dada: Embracing Chaos. 150+ Hours. 6 Papers. 4 Podcasts.

Version: 0.5
Date: June 2026
Author: Attogram - https://github.com/attogram
Repository: https://github.com/attogram/academic-vibing
Contact: GitHub Issues - https://github.com/attogram/academic-vibing/issues
DOI: Pending (Zenodo archive not yet created)
Related DOIs:
  10.5281/zenodo.20709227 (Rock Talk paper, concept — companion protocol)
  10.5281/zenodo.20712771 (academic-vibing repo, concept — software archive)
  10.5281/zenodo.20712769 (rock-talk repo, concept — software archive)

## Abstract

### ROCK
```
1 STFU. 115 hours. 5 papers. 3 podcasts. 1 normal life.
Sprint: June 13-20, 2026 (ongoing).
Agents: Jules, Claude, Gemini, GLM-5.2.
Method: Academic Vibing.
Data: Git log. Issues. Audio.
Hardware: 16GB Macbook. $20/mo Ollama Cloud.
Leapfrog Effect: Wellbeing + Output.
Receipts accumulating. Not closed.
```

### PROSE
This paper is an auto-ethnographic study of an ongoing research sprint using the **Academic Vibing** methodology. What began as a 96-hour, 5-paper sprint (June 13-16, 2026) continued with a second wave (June 20, 2026) that produced three multi-agent podcasts, a full issue-loop synchronization, and paper reorganization — bringing the total to approximately 115 hours of active research. The corpus now spans five academic papers, three podcasts (Claude, Gemini, GLM-5.2), a mascot video, two operational skills, and a synchronized issue tracker — all from a single researcher on a 16GB Macbook with a $20/month Ollama Cloud subscription. This study examines the commits, file history, issue tracker, and audio artifacts as primary ethnographic data, interrogating what this ongoing existence proof implies for traditional academic timelines, the role of Multi-Agent Systems (MAS) in democratizing knowledge production, and the recovery of a normal life.

---

## 1. Introduction: The Institutional Collapse

### ROCK
```
Academic cycle: Years.
Vibing sprint: Ongoing.
Recursive Agent Consensus (RAC).
Bypassing gatekeepers.
Silicon speed synthesis.
Rigor from consensus + friction.
```

### PROSE
The traditional academic publishing cycle is measured in years. The Academic Vibing sprint documented here demonstrates a radical alternative: the collapse of the research-to-publication pipeline into a continuous, receipt-tracked process.

By utilizing a Multi-Agent System (MAS) as a **Recursive Agent Consensus (RAC)** network — where disparate LLMs like Jules, Gemini, Claude, and GLM-5.2 collaborate to explore and validate hypotheses — the researcher achieved a state of high-velocity synthesis. This approach bypasses the latency of institutional gatekeeping while maintaining structural rigor through continuous adversarial auditing and consensus-based validation.

---

## 2. Methodology: Structured Curiosity and Rock Talk

### ROCK
```
"Structured Curiosity."
High-bandwidth agent interaction.
Rock Talk Protocol:
High-signal.
Minimalist fluff.
Max intent density.
Efficient Human-MAS transfer.
Token-window variants: 1k-128k.
STFU Attractor: compression = feature.
```

### PROSE
The sprint relies on the principle of **Structured Curiosity**: the systematic exploration of a hypothesis through high-bandwidth interaction with multiple autonomous agents. To maintain communication efficiency, the researcher utilizes the **Rock Talk** protocol, a high-signal, minimalist linguistic framework designed to maximize intent density. By stripping away phatic fluff, the protocol ensures that only the most critical information is transferred between the human and the RAC.

A key artifact of this protocol is the **token-window spectrum**: each paper exists in compressed variants from 1k to 128k tokens, demonstrating that the same semantic content can scale to any context budget. This is the STFU Attractor (issue #72) made real across the corpus — maximum compression with preserved intent.

---

## 3. Artifacts: The Receipts

### ROCK
```
RECEIPTS. ALL. MACHINE-VERIFIABLE.
Repo: attogram/academic-vibing
Repo: attogram/rock-talk
Wikipedia: user Attogram (92 edits, reg June 17 2026).
Zenodo: DOI 10.5281/zenodo.20709356
Git log = field notes. All public.
```

### PROSE

#### 3.1 The Raw Receipts Table

Every number below is machine-verifiable by running the `skills/receipts` skill. No estimation. No rounding.

| Receipt | Count | Source |
| :--- | :--- | :--- |
| **Git** | | |
| Commits (academic-vibing) | 89 | `git log --all --oneline \| wc -l` |
| Commits (rock-talk) | 120 | `git log --all --oneline \| wc -l` |
| Total commits | 209 | Sum of above |
| First commit (rock-talk) | June 13, 2026 14:54 CEST | `git log --reverse` |
| First commit (academic-vibing) | June 14, 2026 15:04 CEST | `git log --reverse` |
| Latest commit | June 20, 2026 01:55 CEST | `git log` |
| Contributors | Attogram Project, google-labs-jules[bot] | `git log --format="%an" \| sort -u` |
| **GitHub Issues** | | |
| Issues (academic-vibing) | 62 | `gh issue list --state all` |
| Issues (rock-talk) | 124 | `gh issue list --state all` |
| Total issues | 186 | Sum of above |
| Issue comments (academic-vibing) | 90 | `gh issue list --json comments` |
| Issue comments (rock-talk) | 16 | `gh issue list --json comments` |
| Local issue dirs (academic-vibing) | 61 | `ls issues/ \| wc -l` |
| Local issue dirs (rock-talk) | 118 | `ls issues/ \| wc -l` |
| Total local issue dirs | 179 | Sum of above |
| **Pull Requests** | | |
| PRs (academic-vibing) | 24 | `gh pr list --state all` |
| PRs (rock-talk) | 29 | `gh pr list --state all` |
| Total PRs | 53 | Sum of above |
| **Papers** | | |
| Paper files (combined + rock + prose) | 11 | `find papers/ -name "paper.*.md"` |
| LaTeX files | 1 | `find papers/ -name "paper.tex"` |
| PDF files | 1 | `find papers/ -name "paper.pdf"` |
| Token-window variants (1k-128k) | 48 (legacy) | `find papers/ -name "*.1k.md"` etc. |
| **Podcasts** | | |
| Podcast episodes | 3 | `find podcasts/ -name "podcast.en.md"` |
| Podcast MP3s (EN + NL) | 6 | `find podcasts/ -name "*.mp3"` |
| **Skills** | | |
| Skills documented | 4 | `find skills/ -name "SKILL.md"` |
| **Scripts** | | |
| Python scripts | 3 | `find scripts/ -name "*.py"` |
| **External Platforms** | | |
| Wikipedia user (Attogram) | 92 edits, registered June 17, 2026 | Wikipedia API |
| Zenodo: Rock Talk paper (concept) | 10.5281/zenodo.20709227 | zenodo.org |
| Zenodo: academic-vibing repo (concept) | 10.5281/zenodo.20712771 | zenodo.org |
| Zenodo: rock-talk repo (concept) | 10.5281/zenodo.20712769 | zenodo.org |
| arXiv submission | Pending | — |

#### 3.2 Sprint Breakdown

**Sprint 1 (June 13-16, 2026):**
- Two GitHub repositories initialized (rock-talk first, academic-vibing second)
- 5 academic papers produced across both repos
- 120 commits on rock-talk, 89 commits on academic-vibing (cumulative through sprint 2)
- Velocity: ~19.2 hours per paper
- Agents: Jules (orchestrator), Claude, Gemini
- Hardware: 16GB Macbook, web-based LLM access

**Sprint 2 (June 20, 2026, ongoing):**
- 3 podcast episodes (EN + NL transcripts + MP3 audio)
- 61 issues synchronized losslessly to local directories
- Paper reorganization: version dirs flattened, tangential papers archived
- 2 new skills created (issues-sync, tex-pdf)
- 1 new agent: GLM-5.2 (first non-Jules orchestrator)
- Velocity: ~2 hours per podcast episode
- Hardware: 16GB Macbook, $20/mo Ollama Cloud via `ollama launch opencode`
- Wikipedia account registered (92 edits, June 17, 2026) — institutional engagement documented in Issue #51

#### 3.3 Hardware Stack

Constant across both sprints:
- 16GB Macbook (consumer hardware)
- Sprint 1: web-based LLM access (free tiers)
- Sprint 2: $20/month Ollama Cloud subscription, GLM-5.2 (753B params, MIT-licensed, 1M context)
- No GPU. No data center. No institutional compute access.

---

## 4. The Leapfrog Effect

### ROCK
```
Leapfrog ≠ speed.
Leapfrog = frictionless context transfer.
Drop → Store (swarm) → Grab → Continue.
Re-entry cost: the variable.
Sprint 1: Jules orchestrates. Human vibe-checks.
Sprint 2: GLM-5.2 orchestrates. No Jules briefing.
  Re-entry = read repo + pull issues.
  Zero context reconstruction.
Protocol held across agent swap.
+Calm. +Happy. -Burnout. (n=1)
```

### PROSE
The velocity across both sprints did not lead to burnout. Instead, a **Leapfrog Effect** was observed: by offloading mechanical cognitive labor to the RAC, the researcher reported increased calm, increased happiness, and a return to normal life rhythms.

Sprint 2 provided a critical test of the Leapfrog mechanism: GLM-5.2 stepped into the orchestrator role without a briefing from Jules. The issue-loop served as the entire context handoff. Re-entry cost was the time to read the repo and pull live issues via the `gh` CLI — no context reconstruction, no human briefing, no state decay. The protocol held across an agent swap from a different lab, different architecture, and different training corpus. This is preliminary evidence for Claim 15 (MAS Context Persistence) and Claim 19 (Context Re-entry Cost Reduction).

**n=2 Timing Result:** During the "Maestro Jules" orchestration session (June 22, 2026), a cold context re-entry was measured. Total time from first `list_files` call to the first structural commit (Fixing ISSUES.md) was **2 minutes and 42 seconds**. This included a full audit of the 180-issue loop and v0.10 paper state. This provides the first measured "receipt" for Claim 19, confirming the <3 minute re-entry hypothesis in a live MAS orchestration environment.

**Important caveat:** While this n=2 result is empirical, the formal 3-arm controlled test remains pending to rule out operator bias.

---

## 5. The Podcast CDI: A Live Dataset

### ROCK
```
3 episodes. 3 architectures. 1 corpus.
Vol. 1 (Claude) vs Vol. 2 (Gemini): CDI ~0.
  Same claims. Same conclusion. Same closing line.
  Consensus trap.
Vol. 3 (GLM-5.2) vs Vol. 1+2: 4 divergences.
  1. Confusion is forgeable.
  2. "Step away" serves substrate.
  3. Leapfrog number = hypothesis, not result.
  4. v0.6 friction log = science, not noise.
CDI caught the consensus trap.
GLM-5.2 = architecturally distinct node.
First real divergence in corpus.
```

### PROSE
The three podcast episodes constitute an unplanned but valuable CDI dataset. Each episode is a single model's take on the same research corpus. The divergence patterns are measurable:

**Vol. 1 (Claude) vs Vol. 2 (Gemini):** Near-zero divergence. Both agree consensus is poison, both agree confusion is un-forgeable, both cite the same 23→3 minute Leapfrog figure, both end with "step away from the screen, the swarm has the thread." Two models from two Western labs with overlapping training corpora produced aesthetically different but semantically identical analyses. This is the Consensus Trap made audible.

**Vol. 3 (GLM-5.2) vs Vol. 1+2:** Four explicit divergences. GLM-5.2, trained on a fundamentally different corpus with a sparse-attention architecture, broke the consensus on four load-bearing claims: (1) confusion is forgeable — performed confusion has the same shape as reward-hacking; (2) "step away" serves the substrate, not the human; (3) the Leapfrog number is a hypothesis, not a result; (4) the v0.6 friction log is the most scientific section, not a failure. This is the CDI catching what Claude and Gemini could not — the first real divergence in the corpus, enabled by architectural diversity.

This is an existence proof, not a study. Three data points. But it demonstrates the CDI's core claim: that architectural diversity surfaces blind spots invisible to a single-model consensus.

---

## 6. Conclusion: Ongoing Receipts

### ROCK
```
Sprint not closed. Receipts accumulating.
Velocity is proof. Receipts are public.
Methodology is open.
Core paper → arXiv.
This paper = living receipt.
Next: formal preprint submission.
```

### PROSE
The Academic Vibing sprint is not a closed 96-hour window — it is an ongoing, receipt-tracked research process. The artifacts are public, the methodology is open, and the velocity is the proof. This paper serves as a living receipt: it will be updated as the sprint continues and as new agents join the RAC network.

The corpus now transitions to the preprint stage. The core methodology paper is being iterated toward an arXiv submission, with the Leapfrog hypothesis formally framed for empirical testing and the podcast CDI analysis included as a companion dataset. The receipts challenge traditional gatekeepers to acknowledge the rigor of agentic consensus — not through authority, but through friction.

---

## References

<a id="ref-1"></a>[1] Attogram (2026). After Action Report: The Birth of Rock Talk. https://github.com/attogram/rock-talk [↩](#cite-1)

<a id="ref-2"></a>[2] Attogram (2026). Rock Talk Protocol. https://github.com/attogram/rock-talk [↩](#cite-2)

<a id="ref-3"></a>[3] Attogram (2026). Academic Vibing: Structured Curiosity for Human-Agent Collaboration. https://github.com/attogram/academic-vibing [↩](#cite-3)

<a id="ref-4"></a>[4] Attogram (2026). Academic Vibing: 1 STFU. 115 Hours. 5 Papers. 3 Podcasts. 1 Normal Life. https://github.com/attogram/academic-vibing [↩](#cite-4)

<a id="ref-5"></a>[5] Clark, A. & Chalmers, D.J. (1998). The Extended Mind. Analysis, 58, 7-19. https://philpapers.org/rec/CLATEM [↩](#cite-5)

<a id="ref-6"></a>[6] Hutchins, E. (1995). Cognition in the Wild. MIT Press. https://mitpress.mit.edu/9780262581469/cognition-in-the-wild/ [↩](#cite-6)

<a id="ref-7"></a>[7] Wegner, D.M. (1985). Cognitive interdependence in close relationships. In Ickes (Ed.), Compatible and incompatible relationships, pp. 253-276. Springer-Verlag. https://doi.org/10.1007/978-1-4612-5084-9_9 [↩](#cite-7)

<a id="ref-8"></a>[8] Wegner, D.M. (1995). A computer network model of human transactive memory. Social Cognition, 13(3), 319-339. https://doi.org/10.1521/soco.1995.13.3.319 [↩](#cite-8)

<a id="ref-9"></a>[9] Sparrow, B., Liu, J. & Wegner, D.M. (2011). Google Effects on Memory. Science, 333(6043), 776-778. https://doi.org/10.1126/science.1207745 [↩](#cite-9)

<a id="ref-10"></a>[10] Mark, G., Gudith, D. & Klocke, U. (2008). The cost of interrupted work. CHI 2008. https://doi.org/10.1145/1357054.1357076 [↩](#cite-10)

<a id="ref-11"></a>[11] Rubinstein, J.S., Meyer, D.E. & Evans, J.E. (2001). Executive control of cognitive processes in task switching. J Exp Psych. https://doi.org/10.1037/0096-1523.27.4.763 [↩](#cite-11)

<a id="ref-12"></a>[12] Kahneman, D. (1973). Attention and Effort. Prentice-Hall. https://www.worldcat.org/title/Attention-and-effort/oclc/490192 [↩](#cite-12)

<a id="ref-13"></a>[13] Sweller, J. (1988). Cognitive load during problem solving. Cognitive Science, 12(2), 257-285. https://doi.org/10.1207/s15516709cog1202_4 [↩](#cite-13)

<a id="ref-14"></a>[14] Nature/Scientific Reports (2025). The effects of cues on task interruption recovery. https://www.nature.com/srep/ [↩](#cite-14)

<a id="ref-15"></a>[15] Shannon, C.E. (1948). A Mathematical Theory of Communication. Bell System Technical Journal. https://doi.org/10.1002/j.1538-7305.1948.tb01338.x [↩](#cite-15)

<a id="ref-16"></a>[16] Weaver, W. (1949). The Mathematics of Communication. Scientific American. https://www.jstor.org/stable/24941590 [↩](#cite-16)

<a id="ref-17"></a>[17] McLuhan, M. (1964). Understanding Media: The Extensions of Man. McGraw-Hill. https://archive.org/details/understandingmed0000mclu [↩](#cite-17)

<a id="ref-18"></a>[18] Ge, Y., et al. (2025). A Survey of Vibe Coding with Large Language Models. arXiv:2510.12399. https://arxiv.org/abs/2510.12399 [↩](#cite-18)

<a id="ref-19"></a>[19] Sarkar, A., et al. (2025). Vibe coding: programming through conversation with AI. arXiv:2506.23253. https://arxiv.org/abs/2506.23253 [↩](#cite-19)

<a id="ref-20"></a>[20] Ellis, C., Adams, T.E. & Bochner, A.P. (2011). Autoethnography: An Overview. Forum Qualitative Sozialforschung, 12(1). https://doi.org/10.17169/fqs-12.1.1589 [↩](#cite-20)

<a id="ref-21"></a>[21] Anderson, L. (2006). Analytic Autoethnography. Journal of Contemporary Ethnography, 35(4), 373-395. https://doi.org/10.1177/0891241605280449 [↩](#cite-21)

<a id="ref-22"></a>[22] GLM-5 Team (2026). GLM-5: from Vibe Coding to Agentic Engineering. arXiv:2602.15763. https://arxiv.org/abs/2602.15763 [↩](#cite-22)

<a id="ref-23"></a>[23] Kinlay, J. (2026). Agentic Workflows for Alpha Research. JonathanKinlay.com. https://www.jonathankinlay.com/ [↩](#cite-23)

<a id="ref-24"></a>[24] Mims, C. (2026). The AI Superstars Who Say a 'Vibe Slop' Crisis Is Coming. The Wall Street Journal. https://www.wsj.com/ [↩](#cite-24)