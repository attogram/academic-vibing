#!/usr/bin/env python3
"""Generate podcast MP3s from a Vol. 3 transcript using edge-tts.

Strips [ROCK TALK] metadata block, voice markers, and parenthetical stage
directions from the [PROSE] section, then synthesizes speech.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

VOICES = {
    "en": "en-US-BrianMultilingualNeural",
    "nl": "nl-NL-MaartenNeural",
}


def extract_prose_speech(md: str) -> str:
    # Drop the [ROCK TALK] header block (everything up to and including [PROSE])
    m = re.search(r"\[PROSE\]\s*\n", md)
    body = md[m.end():] if m else md
    # Remove markdown headings
    body = re.sub(r"^#{1,6}\s+.*$", "", body, flags=re.MULTILINE)
    # Remove voice markers like **Jules:** or **Claude:**
    body = re.sub(r"^\*?\*?[A-Za-z]+:\*\*?\s*", "", body, flags=re.MULTILINE)
    # Remove parenthetical stage directions (possibly multiline)
    body = re.sub(r"\([^)]*\)", "", body)
    # Remove bold/italic markers
    body = re.sub(r"\*+([^*]+)\*+", r"\1", body)
    # Remove backtick code spans
    body = re.sub(r"`([^`]+)`", r"\1", body)
    # Remove blockquote markers
    body = re.sub(r"^\s*>\s*", "", body, flags=re.MULTILINE)
    # Collapse blank lines
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip() + "\n"


def synth(text_path: Path, voice: str, out_path: Path) -> None:
    cmd = [
        sys.executable, "-m", "edge_tts",
        "--voice", voice,
        "--file", str(text_path),
        "--write-media", str(out_path),
    ]
    print(f"Synthesizing {out_path.name} with voice {voice}...")
    subprocess.run(cmd, check=True)


def main() -> None:
    base = Path(__file__).resolve().parent
    jobs = [
        ("podcast-v3.en.md", "en", "podcast-v3.en.mp3"),
        ("podcast-v3.nl.md", "nl", "podcast-v3.nl.mp3"),
    ]
    for md_name, lang, mp3_name in jobs:
        md_path = base / md_name
        mp3_path = base / mp3_name
        prose = extract_prose_speech(md_path.read_text(encoding="utf-8"))
        with tempfile.NamedTemporaryFile(
            "w", suffix=".txt", delete=False, encoding="utf-8", dir=str(base)
        ) as tf:
            tf.write(prose)
            tmp_path = Path(tf.name)
        try:
            synth(tmp_path, VOICES[lang], mp3_path)
        finally:
            tmp_path.unlink(missing_ok=True)
    print("Done.")


if __name__ == "__main__":
    main()