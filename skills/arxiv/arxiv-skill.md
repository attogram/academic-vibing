# Skill: arXiv Submission (v0.1)

## ROCK
Context: Submit core paper to arXiv as preprint.
Goal: One PDF. arXiv-stable. Citeable.
Method: arXiv submission system (web). LaTeX source required.
Rule: Paper must be self-contained. No external assets broken.
Timing: After Zenodo DOI assignment. After final vibe-check.

## PROSE

### 1. Prerequisites

- A complete `paper.tex` that compiles to `paper.pdf` via `pdflatex`
- All figures embedded (no external image dependencies)
- All references in a `.bib` file or inline `\bibitem`
- A verified Zenodo DOI for the paper (see `skills/zenodo/SKILL.md`)
- arXiv account registered at https://arxiv.org

### 2. arXiv Category

Academic Vibing fits multiple categories. Primary recommendation:
- **cs.HC (Human-Computer Interaction)** — primary: human-agent collaboration protocol
- **cs.AI (Artificial Intelligence)** — secondary: multi-agent systems, LLM methodology
- **cs.DL (Digital Libraries)** — secondary: open research methodology

### 3. Pre-Submission Checklist

Before submitting, verify:

- [ ] `paper.tex` compiles with zero errors (`pdflatex -interaction=nonstopmode paper.tex`)
- [ ] PDF is 4-15 pages (arXiv sweet spot for methodology papers)
- [ ] All citations resolve (no "Unknown reference" warnings)
- [ ] Abstract is self-contained (no dependencies on external links)
- [ ] Figures are vector or high-res (300+ DPI)
- [ ] No proprietary fonts (pdflatex embeds by default)
- [ ] Author name and affiliation present
- [ ] Zenodo DOI included in paper
- [ ] GitHub repo URL included
- [ ] License specified (MIT or CC-BY 4.0)

### 4. Submission Package

arXiv requires a single .zip or .tar.gz containing:
```
paper.tex
paper.bib (if using BibTeX) or inline \bibitem
figure1.pdf (if any figures)
figure2.pdf
...
```

Do NOT include:
- `paper.aux`, `paper.log`, `paper.out` (build artifacts)
- `paper.pdf` (arXiv compiles its own)
- `.DS_Store` or other OS junk

Create the package:
```bash
cd papers/academic-vibing
zip arxiv-submission.zip paper.tex paper.bib
```

### 5. Submission Process

1. Go to https://arxiv.org/submit
2. Select category: cs.HC (primary), cs.AI (secondary)
3. Upload `arxiv-submission.zip`
4. Title: "Academic Vibing: Consensus Poisoning and the Leapfrog Mechanism"
5. Abstract: copy from `paper.tex`
6. Authors: Attogram
7. License: MIT or CC-BY 4.0
8. Submit
9. arXiv assigns an identifier (e.g., 2606.XXXXX)

### 6. Post-Submission

- arXiv ID is permanent. Add to CITATIONS.md and README.md.
- Update Zenodo record to include the arXiv ID as a related identifier.
- Tweet/announce with the arXiv link.
- Update ISSUES.md: close the "arXiv submission" issue.

### 7. Versioning on arXiv

- v1: Initial submission
- v2: Post-feedback revisions (if any)
- Each version gets its own arXiv ID suffix (e.g., v1 = 2606.12345, v2 = 2606.12345v2)
- The base ID (2606.12345) always resolves to the latest version

### 8. Receipts Paper

The receipts paper (`papers/receipts/`) should be submitted as a companion:
- Separate arXiv submission
- Cross-reference the core paper's arXiv ID
- Include the arXiv ID in the receipts table

### 9. Verification

After submission:
```bash
# Verify the arXiv paper resolves
curl -s "http://export.arxiv.org/api/query?id_list=<ARXIV_ID>" | head -20

# Check it appears in search
curl -s "http://export.arxiv.org/api/query?search_query=ti:academic+vibing&max_results=5"
```

### 10. Timeline

- Compilation: 1 hour (pdflatex + fixes)
- arXiv submission: 30 minutes (web form)
- arXiv processing: 24-48 hours (moderation)
- Live: typically within 2 days of submission

Do not submit until:
1. Core paper is at v0.7+ and structurally clean
2. Section 8 (Institutional Trauma) is stripped (archived separately)
3. Leapfrog claim is framed as hypothesis, not assertion
4. All citations are verified
5. Zenodo DOI is assigned