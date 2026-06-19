# Skill: TeX/PDF Generation (v0.1)

## [ROCK TALK]
Context: Convert paper.tex to paper.pdf for arXiv submission.
Tool: pdflatex (TeX Live, pre-installed on macOS).
Command: pdflatex -interaction=nonstopmode paper.tex
Output: paper.pdf
Clean: remove .aux .log .out after compile.

## [PROSE]

### 1. Prerequisites
- `pdflatex` installed (TeX Live). Verify: `which pdflatex`
- A `paper.tex` file in the paper directory.

### 2. Compile
```bash
cd papers/[paper-name]
pdflatex -interaction=nonstopmode paper.tex
```
Run twice for cross-references and TOC:
```bash
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

### 3. Clean Up
Remove LaTeX build artifacts after successful compile:
```bash
rm -f paper.aux paper.log paper.out paper.toc paper.bbl paper.blg
```
Keep only: `paper.tex` and `paper.pdf`.

### 4. Verification
```bash
ls -la paper.pdf  # should exist and be > 0 bytes
```

### 5. arXiv Preparation
For arXiv submission:
- Ensure `\documentclass{article}` or compatible class.
- Use `\usepackage[utf8]{inputenc}`.
- Embed all fonts (pdflatex does this by default).
- Run pdflatex twice to resolve references.
- Submit the `.tex` + `.pdf` + any figures as a single .zip.

### 6. Paper Directory Structure
Each paper directory should contain:
```
papers/[paper-name]/
  paper.combined.md   # Rock + Prose combined
  paper.rock.md       # Rock Talk version
  paper.prose.md      # Prose version
  paper.tex           # LaTeX source
  paper.pdf           # Compiled PDF
  paper.1k.md         # Token-window variants (1k-128k)
  paper.2k.md
  paper.4k.md
  ...
  paper.128k.md
```