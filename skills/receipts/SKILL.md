# Skill: Receipts Collection (v0.1)

## ROCK
Context: Gather raw receipt data from git, GitHub, and external platforms.
Goal: Hard numbers. No estimation. No rounding.
Output: JSON or markdown table of all artifacts, commits, issues, PRs.
Method: gh CLI + git log + curl APIs.
Rule: Every number in the receipts paper must be machine-verifiable.

## PROSE

### 1. Purpose
This skill collects verifiable receipt data from all sources — git history, GitHub issues/PRs, and external platforms (Wikipedia, Zenodo, arXiv). Used to populate the receipts paper with hard numbers, not estimates.

### 2. Git Receipts (Local)
```bash
# Commit count
git log --all --oneline | wc -l

# First and last commit dates
git log --all --format="%ai" --reverse | head -1   # first
git log --all --format="%ai" | head -1              # last

# Contributors
git log --all --format="%an" | sort -u

# All commits with dates
git log --all --format="%ai %s" --reverse
```

### 3. GitHub Receipts (via gh CLI)
```bash
# Issues (count + detail)
gh issue list --repo attogram/academic-vibing --state all --limit 200 --json number,title,state,comments,createdAt

# PRs
gh pr list --repo attogram/academic-vibing --state all --limit 200 --json number,title,state,createdAt

# Issue comment count (total across all issues)
gh issue list --repo <REPO> --state all --limit 200 --json number,comments | \
  python3 -c "import json,sys; issues=json.load(sys.stdin); print(sum(len(i['comments']) if isinstance(i['comments'],list) else i['comments'] for i in issues))"
```

### 4. Cross-Repo Receipts
Run the same queries for both repos:
- `attogram/academic-vibing`
- `attogram/rock-talk`

Aggregate totals:
```bash
# Total commits across both repos
echo $(($(git -C academic-vibing log --all --oneline | wc -l) + $(git -C rock-talk log --all --oneline | wc -l)))
```

### 5. File Artifact Counts
```bash
# Papers (combined + rock + prose)
find papers/ -name "paper.combined.md" -o -name "paper.rock.md" -o -name "paper.prose.md" | wc -l

# Podcasts (transcripts + audio)
find podcasts/ -name "podcast.en.md" | wc -l
find podcasts/ -name "*.mp3" | wc -l

# Skills
find skills/ -name "SKILL.md" | wc -l

# Issue dirs (local archive)
ls issues/ | wc -l

# Scripts
find scripts/ -name "*.py" | wc -l

# Token-window variants
find papers/ -name "*.1k.md" -o -name "*.128k.md" | wc -l

# LaTeX + PDF
find papers/ -name "paper.tex" -o -name "paper.pdf" | wc -l
```

### 6. External Platform Receipts
```bash
# Wikipedia user edit count
curl -s "https://en.wikipedia.org/w/api.php?action=query&list=users&ususers=Attogram&usprop=editcount|registration|groups&format=json"

# Zenodo DOI metadata
curl -s "https://doi.org/10.5281/zenodo.20709356" -L -o /dev/null -w "%{http_code}"

# arXiv submission status (once submitted)
curl -s "http://export.arxiv.org/api/query?id_list=<ARXIV_ID>"
```

### 7. Output Format
Generate a markdown table for direct inclusion in the receipts paper:
```markdown
| Receipt | Count | Source |
| :--- | :--- | :--- |
| Commits (AV) | 89 | git log |
| Commits (RT) | 120 | git log |
| Total commits | 209 | git log |
| Issues (AV) | 62 | gh issue list |
| Issues (RT) | 124 | gh issue list |
| PRs (AV) | 24 | gh pr list |
| PRs (RT) | 29 | gh pr list |
| Issue comments (AV) | 90 | gh issue list |
| Papers | 11 | find |
| Podcasts | 3 | find |
| Podcast MP3s | 6 | find |
| Skills | 4 | find |
| Issue dirs | 61 | ls |
| Scripts | 3 | find |
```

### 8. Verification Rule
Every number in the receipts paper must be reproducible by running this skill. No manual counting. No estimation. If a number can't be machine-verified, it doesn't go in the paper.