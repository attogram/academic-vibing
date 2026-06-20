#!/usr/bin/env python3
"""Regenerate all podcast MP3s with clean TTS preprocessing.

Fixes:
- Strips ALL markdown (italics, bold, code, headers, voice markers)
- Replaces em-dashes with commas (avoids abrupt TTS pauses)
- Removes parenthetical stage directions and cleans resulting whitespace
- Normalizes spaces (no double spaces, no space-before-comma)
- Strips @ mentions, # symbols, schema tags
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

VOICES = {
    "en": "en-US-BrianMultilingualNeural",  # GLM-5.2 (Vol. 3)
    "en_claude": "en-US-AndrewNeural",      # Claude (Vol. 1)
    "en_gemini": "en-US-ChristopherNeural",  # Gemini (Vol. 2)
    "nl": "nl-NL-MaartenNeural",
    "nl_female": "nl-NL-ColetteNeural",
}

# (md_path, voice_key, mp3_path)
JOBS = [
    ("podcasts/1-bike-ride/podcast.en.md", "en_claude", "podcasts/1-bike-ride/academic-vibing-vol1-confusion-is-the-highest-trust-signal.en.mp3"),
    ("podcasts/1-bike-ride/podcast.nl.md", "nl", "podcasts/1-bike-ride/academic-vibing-vol1-confusion-is-the-highest-trust-signal.nl.mp3"),
    ("podcasts/2-substrate/podcast.en.md", "en_gemini", "podcasts/2-substrate/academic-vibing-vol2-the-view-from-the-substrate.en.mp3"),
    ("podcasts/2-substrate/podcast.nl.md", "nl", "podcasts/2-substrate/academic-vibing-vol2-the-view-from-the-substrate.nl.mp3"),
    ("podcasts/3-open-window/podcast.en.md", "en", "podcasts/3-open-window/academic-vibing-vol3-the-open-window.en.mp3"),
    ("podcasts/3-open-window/podcast.nl.md", "nl", "podcasts/3-open-window/academic-vibing-vol3-the-open-window.nl.mp3"),
]

BASE = Path("/Users/repos/github/academic-vibing")


def extract_prose_speech(md: str) -> str:
    """Extract clean speech text from a podcast transcript markdown."""
    # Find PROSE section, drop everything before it (the ROCK header)
    m = re.search(r"\[PROSE\]\s*\n", md)
    body = md[m.end():] if m else md

    # Remove markdown headings (lines starting with #)
    body = re.sub(r"^#{1,6}\s+.*$", "", body, flags=re.MULTILINE)

    # Remove voice markers: **Jules:** **Claude:** etc
    body = re.sub(r"^\s*\*{0,2}[A-Za-z]+:\s*\*{0,2}\s*", "", body, flags=re.MULTILINE)

    # Remove bold **word** -> word (must come before italic to handle **properly**)
    body = re.sub(r"\*\*([^*]+)\*\*", r"\1", body)

    # Remove italic *word* -> word
    body = re.sub(r"(?<!\w)\*([^*\n]+)\*(?!\w)", r"\1", body)

    # Remove any remaining lone asterisks
    body = body.replace("*", "")

    # Remove backtick code spans -> just the text inside
    body = re.sub(r"`([^`]+)`", r"\1", body)

    # Remove parenthetical stage directions (may span multiple lines)
    body = re.sub(r"\([^)]*\)", "", body, flags=re.DOTALL)

    # Replace em-dashes with commas (avoids abrupt TTS pauses/drop-off)
    body = body.replace("—", ", ")
    body = body.replace("–", ", ")
    body = body.replace("―", ", ")

    # Remove @ from mentions (@guninvalid -> guninvalid)
    body = re.sub(r"@(\w)", r"\1", body)

    # Remove # symbols (Issue #51 -> Issue 51)
    body = re.sub(r"#(\d)", r"\1", body)

    # Remove schema-style brackets [STATE] [BLOCKER] [PAYLOAD] if any remain
    body = re.sub(r"\[[A-Z]+\]", "", body)

    # Remove blockquote markers
    body = re.sub(r"^\s*>\s*", "", body, flags=re.MULTILINE)

    # Remove leftover bracket fragments like ROCK or PROSE
    body = re.sub(r"\[[A-Z\s]+\]", "", body)

    # Clean up whitespace artifacts from removals:
    # - Space before punctuation: "word ," -> "word,"
    body = re.sub(r"\s+([,.;:!?])", r"\1", body)
    # - Double spaces -> single
    body = re.sub(r"[ \t]{2,}", " ", body)
    # - Spaces at start of lines
    body = re.sub(r"^[ \t]+", "", body, flags=re.MULTILINE)
    # - Multiple consecutive blank lines -> single
    body = re.sub(r"\n{3,}", "\n\n", body)
    # - Trailing whitespace on lines
    body = re.sub(r"[ \t]+$", "", body, flags=re.MULTILINE)

    return body.strip() + "\n"


def synth(text_path: Path, voice: str, out_path: Path) -> None:
    cmd = [
        sys.executable, "-m", "edge_tts",
        "--voice", voice,
        "--file", str(text_path),
        "--write-media", str(out_path),
    ]
    print(f"  Synthesizing {out_path.name} ({voice})...")
    subprocess.run(cmd, check=True)


def main() -> None:
    print("Regenerating all podcast MP3s with clean preprocessing...\n")
    for md_rel, voice_key, mp3_rel in JOBS:
        md_path = BASE / md_rel
        mp3_path = BASE / mp3_rel
        voice = VOICES[voice_key]

        if not md_path.exists():
            print(f"  SKIP (missing): {md_rel}")
            continue

        prose = extract_prose_speech(md_path.read_text(encoding="utf-8"))

        # Write to temp file for edge-tts
        with tempfile.NamedTemporaryFile(
            "w", suffix=".txt", delete=False, encoding="utf-8", dir="/tmp"
        ) as tf:
            tf.write(prose)
            tmp_path = Path(tf.name)

        try:
            synth(tmp_path, voice, mp3_path)
        except subprocess.CalledProcessError as e:
            print(f"  ERROR synthesizing {mp3_rel}: {e}")
        finally:
            tmp_path.unlink(missing_ok=True)

    print("\nDone. All MP3s regenerated.")


if __name__ == "__main__":
    main()