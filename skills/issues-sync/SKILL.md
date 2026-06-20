# Skill: Issues Sync (v0.1)

## ROCK
Context: Janitorial agent task. Run periodically or on demand.
Goal: Local issues/ = exact replica of GitHub source of truth.
Method: gh CLI → JSON → write raw body per issue. No reformatting. No headers. No metadata.
Output: issues/[NNN]-[Code]-[Summary]/issue.md + ISSUES.md TOC.

## PROSE

### 1. Purpose
This skill synchronizes the local `issues/` directory with the GitHub Issues source of truth. Every `issue.md` file must be a **byte-for-byte exact replica** of the GitHub issue body — no headers, no metadata, no reformatting, no summarization. Lossless.

### 2. Prerequisites
- `gh` CLI installed and authenticated (`gh auth login`)
- Repository: `attogram/academic-vibing`
- Python 3 (for JSON parsing and file writing)

### 3. Pull All Issues from GitHub
```bash
gh issue list --repo attogram/academic-vibing --limit 200 --state all --json number,title,state,body,createdAt > /tmp/av_issues.json
```

### 4. Write Issue Files (Lossless)
For each issue, write the raw `body` field directly to `issues/[NNN]-[Code]-[Summary]/issue.md`.

**Critical rules:**
- The file content is EXACTLY the `body` field from the GitHub API — nothing added, nothing removed.
- No metadata header. No `# Issue #N:` title. No state, code, or timestamp lines.
- No summarization. No translation. No reformatting.
- If the body is empty, write `(no body)`.

**Directory naming:** `issues/[NNN]-[Code]-[Concise-Summary]/`
- `NNN`: zero-padded issue number (e.g. `071`)
- `Code`: the leading code from the title (e.g. `F9`), or `-` if none
- `Concise-Summary`: slugified title minus the code prefix

**File naming:** Always `issue.md` inside the directory.

### 5. Rebuild ISSUES.md
Rebuild `ISSUES.md` as a linked index, grouped by phase:
- Use the **exact GitHub title** verbatim — no rewriting.
- Link to `issues/[NNN]-[Code]-[Summary]/issue.md`.
- Group by phase letter (A, B, C, D, E, F).
- List ghost issues (deleted on GitHub) in a separate section at the bottom.

### 6. Verification
After sync, verify a sample of issues match byte-for-byte:
```bash
gh issue view 71 --repo attogram/academic-vibing --json body | python3 -c "import json,sys; sys.stdout.write(json.load(sys.stdin)['body'])" > /tmp/gh_71.txt
diff /tmp/gh_71.txt issues/071-*/issue.md && echo "IDENTICAL" || echo "DIFFERENT"
```

### 7. Handling Deleted Issues (Ghosts)
If a local issue dir exists but the issue is no longer on GitHub:
- Keep the local dir and file (do not delete).
- Move entry to the "Ghost Issues" section of `ISSUES.md`.
- Mark as `closed (deleted on GitHub)`.

### 8. Handling New Issues
If an issue exists on GitHub but has no local dir:
- Create the dir and write `issue.md` with the exact body.
- Add to the appropriate phase section of `ISSUES.md`.

### 9. Outbox
The `outbox/` directory holds cross-repo handoffs. See `outbox/README.md` for convention.

### 10. Cross-Repo
For `rock-talk` issues, the same workflow applies. See `rock-talk/issues/` and `rock-talk/ISSUES.md` for the existing implementation.