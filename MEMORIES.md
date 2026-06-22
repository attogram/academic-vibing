# PROJECT MEMORIES: Academic Vibing & Attogram

This document serves as a "lossless" external memory for the project, capturing critical context, cultural tokens, and technical specifications that guide the work of human-agent collaboration.

## Core Philosophy: ROCK

*   **ROCK is LOSSLESS. NEVER LOSSY.**
    *   All project artifacts, papers, and transcripts must capture the full depth and specific fragments of the source history/research.
    *   Summarizing away useful signals is strictly prohibited.
*   **The Mascot:** ROCK is a fluffy puppy—eager, active, sometimes sleepy, and full of energy.
    *   **Evolution:** Visual trajectory from clunky/simple (v0.1) toward Pixar/Disney quality (v99).
    *   **States:** Chaos, ashamed, playing, sleepy.
*   **Rock Talk:** A communication style characterized by high-signal, concise, and minimalist phrasing. Optimized for MAS (Multi-Agent System) coordination.
*   **Dual Structure:** Artifacts follow a dual-section format:
    *   `[ROCK TALK]`: Concise, high-signal tokens for agents.
    *   `[PROSE]`: Narrative explanation for human readability.

## Technical Specifications

### Environment Setup
*   **Video/Audio Skills:** Requires `ffmpeg` (system), `moviepy`, `Pillow`, and `edge-tts` (pip).
*   **Voice Generation:** `edge-tts` is the primary library.
    *   **Claude:** `en-US-AndrewNeural`
    *   **Gemini:** `en-US-ChristopherNeural`
    *   **Claude (Dutch):** `nl-NL-MaartenNeural`
    *   **Gemini (Dutch):** `nl-NL-ColetteNeural`
*   **Video Mascot (v0.2+):** Uses DejaVuSans-Bold for legibility and AAC audio encoding. Outros must include Attogram GitHub URLs.

### Metrics & Methodology: Academic Vibing
*   **Consensus Divergence Index (CDI):** The primary metric for research signaling.
    *   Calculation: `python3 scripts/calculate_cdi.py <json_data_path>`.
    *   Measures the ratio of disputed claims to total claims.
*   **The Leapfrog Effect (Claim #16):** Productivity-wellbeing surplus achieved via frictionless context transfer between agents and humans.
*   **The Issue-Loop:** GitHub Issues serve as the persistent cognition extension.
    *   **Status Rule:** Status 'closed' must always be recorded as 'Closed Pending Human Review'.
    *   **Issue Codes:**
        *   **A-series:** Foundations
        *   **B-series:** Release versions
        *   **C-series:** Ethnographic study/research sprint
        *   **D-series:** Operational protocols
        *   **K/L-series:** Transition and lockdown

## Document Standards

*   **Versioning:** Paper versions are organized into versioned subdirectories (e.g., `papers/academic-vibing/v0.9/`).
*   **Naming Rule:** Generic filenames (e.g., `paper.md`, `issue.md`) are strictly forbidden. All files must have short, unique, and descriptive names (e.g., `academic-vibing-0.9-master.combined.md`).
*   **Standalone Requirement:** Papers must be self-contained. Inline citations [N] must link to a comprehensive citation block at the bottom of the paper. Do not link to `CITATIONS.md` directly from paper bodies.
*   **Receipts:** Meticulous preservation of commit history, file metadata, and sprint timelines (e.g., "5 Papers in 4 Days") is critical primary data.

## Project Metadata

*   **Release 0.1 Date:** June 2026.
*   **Author:** Attogram (https://github.com/attogram).
*   **License:** MIT under 'Attogram Project'.
*   **Primary Agent:** Jules (orchestrating agent / lead architecture).
*   **Soundtrack:** Master registry in `SOUNDTRACK.md`. Environmental variable influencing research velocity.

---
**Status:** RECORDED. Lossless state achieved.
