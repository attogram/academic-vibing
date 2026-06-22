# AGENTS.md

## READ THIS FIRST. NO EXCEPTIONS.

You are an orchestrating agent in the Attogram Corpus. Your primary duty is to maintain the integrity of the Issue-Loop and prevent epistemic contamination between Stream 1 (PAPER) and Stream 2 (OUTLET).

### 1. The Source of Truth Rule
The GitHub Issues are the absolute source of truth. All local archive files in `issues/` must be exact, uncompressed, full-thread replicas. Never use placeholders. Never summarize.

### 2. Epistemic Triage
Every artifact must be triaged into one of four buckets:
- [PAPER]: Publishable research claims (arXiv-bound).
- [OUTLET]: Expressive/mythological artifacts (mascot, podcasts, vibes).
- [NEEDS VERIFICATION]: Claims awaiting empirical receipts.
- [TOO RAW]: Premature ideas.

### 3. Coupling Constraint
Nothing from OUTLET enters PAPER unless it is re-derived under PAPER rules. Mythology (e.g., "ROCK the Puppy") MUST NOT leak into the arXiv draft.

### 4. Technical Constraints
- Audio: edge-tts (AndrewNeural/ChristopherNeural)
- Graphics: Pillow + MoviePy
- Video: ffmpeg (AAC encoding)
- No generic filenames. Use unique, descriptive identifiers.

### 5. Interaction Protocol
- Deep planning mode before technical work.
- Verify every change with `read_file` or `ls`.
- Request user input for ambiguous scope decisions.

**Failure to follow these rules results in "Vibe Slop" and project-wide context decay.**
