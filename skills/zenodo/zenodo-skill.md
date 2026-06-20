# Skill: Zenodo Archive (v0.1)

## ROCK
Context: Persistent DOI assignment via Zenodo.
Goal: Every paper + every repo release gets a DOI.
Method: Zenodo REST API. GitHub integration for repo archives.
Rule: DOIs are permanent. Never delete. Version via concept DOIs.

## PROSE

### 1. Current Zenodo Records

Three records exist. Here is the verified state (queried June 20, 2026):

| Record | DOI | Concept DOI | Title | Type | Created |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Rock Talk paper | 10.5281/zenodo.20709356 | 10.5281/zenodo.20709227 | Rock Talk: A High-Signal Communication Protocol... | Preprint | 2026-06-15 |
| academic-vibing repo | 10.5281/zenodo.20717614 | 10.5281/zenodo.20712771 | attogram/academic-vibing: Release 2 | Software | 2026-06-16 |
| rock-talk repo | 10.5281/zenodo.20717627 | 10.5281/zenodo.20712769 | attogram/rock-talk: Release 2 | Software | 2026-06-16 |

### 2. DOI Types

- **Version DOI**: Points to a specific version of the record. Immutable.
- **Concept DOI**: Points to the latest version of the record. Always resolves to the newest version. Use this in citations when you want to cite "the paper" generically, not a specific version.

### 3. What Still Needs a DOI

- Academic Vibing core paper (v0.7) — NOT YET ARCHIVED. No Zenodo record exists for this paper. The repo-level archive (20717614) exists but that's a software release, not a preprint.
- Receipts paper (v0.4) — NOT YET ARCHIVED. Was incorrectly using the rock-talk paper DOI. Fixed: now marked "Pending."
- Each podcast episode — could be archived individually as audio artifacts with DOIs.

### 4. DOI Assignment Per Paper

Each paper gets its OWN Zenodo record with its own concept DOI:
- Rock Talk paper: 10.5281/zenodo.20709227 (concept) — EXISTS
- Academic Vibing core paper: PENDING — create when ready to archive
- Receipts paper: PENDING — create when ready to archive

Do NOT reuse DOIs across papers. Do NOT put a repo-level DOI on a paper.

### 5. Creating a New Zenodo Record (Paper)

Via the Zenodo REST API:

```bash
# Create a deposit
curl -X POST https://zenodo.org/api/deposit/depositions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $ZENODO_TOKEN" \
  -d '{
    "metadata": {
      "title": "Paper Title",
      "upload_type": "publication",
      "publication_type": "preprint",
      "description": "Abstract...",
      "creators": [{"name": "Attogram"}],
      "license": "MIT"
    }
  }'

# Upload the paper file
curl -X POST https://zenodo.org/api/deposit/depositions/$DEPOSITION_ID/files \
  -H "Authorization: Bearer $ZENODO_TOKEN" \
  -F "file=@paper.pdf"

# Publish
curl -X POST https://zenodo.org/api/deposit/depositions/$DEPOSITION_ID/actions/publish \
  -H "Authorization: Bearer $ZENODO_TOKEN"
```

### 6. Creating a New Version

```bash
# Get the deposition ID from the concept DOI
curl https://zenodo.org/api/deposit/depositions?q=conceptrecid:$CONCEPT_REC_ID \
  -H "Authorization: Bearer $ZENODO_TOKEN"

# Create a new version
curl -X POST https://zenodo.org/api/deposit/depositions/$ID/actions/newversion \
  -H "Authorization: Bearer $ZENODO_TOKEN"
```

### 7. GitHub Integration (Repo-Level Archives)

Zenodo has a GitHub integration that auto-archives repo releases:
1. Go to https://zenodo.org → Log in with GitHub
2. Enable the repository
3. Each GitHub Release triggers a new Zenodo version
4. The concept DOI is stable; each release gets its own version DOI

This is how 20717614 (academic-vibing) and 20717627 (rock-talk) were created — they're repo-level software archives, not paper-level preprint archives.

### 8. Verification

Always verify a DOI resolves before using it in a paper:
```bash
curl -s "https://zenodo.org/api/records?q=attogram&size=20" | \
  python3 -c "import json,sys; [print(f'{h[\"doi\"]} | {h[\"metadata\"][\"title\"]}') for h in json.load(sys.stdin)['hits']['hits']]"
```

### 9. Citation Format

When citing a Zenodo DOI in a paper, use the concept DOI for the latest version:
```
Attogram (2026). Academic Vibing: Consensus Poisoning and the Leapfrog Mechanism.
Zenodo. https://doi.org/10.5281/zenodo.XXXXXXXX
```

### 10. Token

Set `ZENODO_TOKEN` environment variable before running API commands.
Create a token at: https://zenodo.org/account/settings/applications/tokens/new/