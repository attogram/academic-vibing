# Skill: Podcast Generation (v0.1)

## [ROCK TALK]
Context: Multi-agent research audio logging.
Target: High-fidelity lossless transcription + persona-coded TTS.
Stack: GitHub Issue-Loop → Raw Markdown → `edge-tts` (MP3).
Voices: Andrew (Claude), Christopher (Gemini), Fenna/Maarten (Dutch).
Structure: Dual [ROCK TALK] / [PROSE].

## [PROSE]

### 1. Source Extraction (Lossless)
To generate a Podcast, start with the raw "payload" from the GitHub Issue tracker. Do not rely on initial summaries; extract the full comment history to preserve specific research fragments, citations, and conversational nuances.
- **Goal:** Capture the "gold" within the friction.
- **Process:** Use `curl` or manual inspection to pull the entire body and comment thread of the target issue.

### 2. Script Drafting & Editing
Clean the raw transcript for "flow and clarity" while maintaining ethnographic fidelity.
- **Persona Coding:** Use consistent voice markers (e.g., **Jules:** for the host, **Claude:** for the rider).
- **Format:** Adhere to the [ROCK TALK] / [PROSE] dual structure.
- **Stage Directions:** Include ambient cues in the [PROSE] section (e.g., `(Ambient sound of bicycle bell)`) but remove them before TTS processing.

### 3. Localization (Amsterdam Context)
When the research session occurs in Amsterdam, provide a Dutch translation.
- **Method:** Translate the full [ROCK TALK] and [PROSE] sections, ensuring technical terms (CDI, Leapfrog) are handled correctly.

### 4. High-Quality Audio Synthesis
Use the `edge-tts` library to generate MP3 assets.
- **Pre-processing:** Extract the [PROSE] text to a temporary `.txt` file, stripping voice markers and parenthetical stage directions.
- **Voice Selection:**
  - **Claude (English):** `en-US-AndrewNeural` (Warm, Confident).
  - **Gemini (English):** `en-US-ChristopherNeural` (Reliable, Authority).
  - **Jules (English):** `en-US-AvaNeural` (Expressive).
  - **Dutch (Male):** `nl-NL-MaartenNeural`.
  - **Dutch (Female):** `nl-NL-ColetteNeural`.
- **Command:** `edge-tts --voice <VOICE> --file <TEXT_FILE> --write-media <AUDIO_FILE>.mp3`

### 5. Repository Integration
- **Directory:** Store assets in `papers/podcasts/v<N>-<TOPIC>/`.
- **Index:** Update `README.md` with links to both the `.md` transcript and the `.mp3` audio.
- **Status:** Update `ISSUES.md` to reflect the closure of the source issues.

### 6. Verification
Ensure binary files are functional and documentation links are correct. Clean up all intermediate text fragments and diagnostic HTML before submission.
