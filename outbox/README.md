# Outbox: Academic Vibing

Cross-repo handoffs and external messages. Files here are outbound communications to other repositories, agents, or external parties.

## Convention

- One file per message/handoff
- Filename: `[target]-[topic].md`
- Example: `rock-talk-issue-sync.md`

## Active

- `gh-issue-summaries.json`: JSON payload of 1k-character issue summaries for automated posting.
- `gh-issue-summaries-report.md`: Human-readable report of the generated summaries.
- **GitHub Automation:** Managed via `scripts/post_issue_summaries.py` to push outbox content to GitHub Issues.

## From Rock Talk

- Received: `recommendation-issue-sync.md` — recommendation to adopt synchronized issue management workflow. **Status: Implemented.** See `issues/` directory and `ISSUES.md`.