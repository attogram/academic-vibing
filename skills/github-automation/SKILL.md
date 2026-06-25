# Skill: GitHub Issue Automation (v1.0)

## ROCK
Context: Sovereign-to-GitHub bridge.
Goal: Automate posting triage buckets and 1k summaries to GitHub issues.
Method: `scripts/post_issue_summaries.py` + `GH_TOKEN`.
Rule: Never assume success. Verify with `--dry-run` first.
Constraint: Triage state derived from `TRIAGE_FULL.md`.

## PROSE

### 1. Purpose
This skill provides the mechanism for a sovereign orchestrator to push research state (triage classifications and compressed summaries) back to the GitHub Issue-Loop. It prevents the "Mailman" bottleneck by automating the propagation of the 1k-character summaries generated in the `outbox/`.

### 2. Prerequisites
- `requests` Python library installed (`pip install requests`)
- `GH_TOKEN` or `GITHUB_TOKEN` environment variable with `repo` scope.
- `outbox/gh-issue-summaries.json` populated with summaries.
- `TRIAGE_FULL.md` updated with the latest bucket classifications.

### 3. Workflow

#### Step 1: Verification (Dry Run)
Before committing to public posts, always verify the payload and mapping.
```bash
python3 scripts/post_issue_summaries.py --dry-run
```

#### Step 2: Execution
Push the summaries to GitHub.
```bash
export GH_TOKEN=your_token_here
python3 scripts/post_issue_summaries.py
```

### 4. Logic & Mapping
The script `scripts/post_issue_summaries.py`:
1. Parses `TRIAGE_FULL.md` to map issue numbers to buckets: `[PAPER]`, `[OUTLET]`, `[NEEDS VERIFICATION]`, `[TOO RAW]`.
2. Reads compressed 1k summaries from `outbox/gh-issue-summaries.json`.
3. Posts a formatted comment to each GitHub issue containing both the triage bucket and the summary.

### 5. Error Handling
- If an issue is missing from `TRIAGE_FULL.md`, it defaults to `NEEDS VERIFICATION`.
- Failed requests are logged to the console with the response status and body.
- The script follows the "Assumed Failure" mandate: it does not mark the task as complete until all API responses are confirmed.
