#!/usr/bin/env python3
"""Generate file-size spectrum variants for podcast MP3s.

Same concept as token-window variants for papers, but for audio:
same content, progressively smaller file size.

Spectrum targets (KB): 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024

For sizes that are physically impossible at full duration (1-4 KB):
  - Truncate duration to fit target at minimum bitrate
  - The audio becomes a "sonic thumbnail" — a ghost of the podcast

For viable sizes (8KB+):
  - Use MP3 at calculated bitrate
  - Fall back to Opus if MP3 bitrate is too low
"""
import subprocess
import math
import os
import sys
from pathlib import Path

TARGETS_KB = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
MP3_MIN_BITRATE = 8000   # 8 kbps (libmp3lame minimum)
OPUS_MIN_BITRATE = 6000  # 6 kbps (libopus minimum)


def get_duration(input_path: str) -> float:
    result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-show_format", "-print_format", "json", input_path],
        capture_output=True, text=True, check=True
    )
    import json
    return float(json.loads(result.stdout)["format"]["duration"])


def calc_bitrate(target_kb: int, duration_sec: float) -> int:
    return int((target_kb * 1024 * 8) / duration_sec)


def calc_truncated_duration(target_kb: int, bitrate: int) -> float:
    return (target_kb * 1024 * 8) / bitrate


def encode_mp3(input_path: str, output_path: str, bitrate: int, sample_rate: int = 16000):
    cmd = [
        "ffmpeg", "-y", "-i", input_path,
        "-codec:a", "libmp3lame", "-b:a", f"{bitrate}",
        "-ar", str(sample_rate), "-ac", "1",
        output_path
    ]
    subprocess.run(cmd, capture_output=True, check=True)


def encode_opus(input_path: str, output_path: str, bitrate: int, sample_rate: int = 8000):
    cmd = [
        "ffmpeg", "-y", "-i", input_path,
        "-codec:a", "libopus", "-b:a", f"{bitrate}",
        "-ar", str(sample_rate), "-ac", "1",
        "-application", "voip",
        output_path
    ]
    subprocess.run(cmd, capture_output=True, check=True)


def encode_truncated(input_path: str, output_path: str, bitrate: int, duration: float):
    """Encode with duration truncation to hit target file size."""
    cmd = [
        "ffmpeg", "-y", "-i", input_path,
        "-t", f"{duration:.1f}",
        "-codec:a", "libmp3lame", "-b:a", f"{bitrate}",
        "-ar", "8000", "-ac", "1",
        output_path
    ]
    subprocess.run(cmd, capture_output=True, check=True)


def generate_spectrum(input_path: str, output_dir: str, base_name: str):
    duration = get_duration(input_path)
    Path(output_dir).mkdir(exist_ok=True)
    print(f"Generating spectrum for {base_name}")
    print(f"  Source: {input_path}")
    print(f"  Duration: {duration:.1f}s")
    print(f"  Targets: {TARGETS_KB} KB")
    print()

    for target_kb in TARGETS_KB:
        needed_bitrate = calc_bitrate(target_kb, duration)
        ext = "mp3"
        out_path = os.path.join(output_dir, f"{base_name}.{target_kb}k.{ext}")

        if needed_bitrate >= MP3_MIN_BITRATE:
            # Full duration, MP3 at calculated bitrate
            bitrate = min(needed_bitrate, 128000)  # cap at 128kbps
            encode_mp3(input_path, out_path, bitrate)
            method = f"MP3 {bitrate//1000}kbps, full duration"
        elif needed_bitrate >= OPUS_MIN_BITRATE:
            # Full duration, Opus at low bitrate
            encode_opus(input_path, out_path.replace(".mp3", ".opus"), needed_bitrate)
            out_path = out_path.replace(".mp3", ".opus")
            method = f"Opus {needed_bitrate//1000}kbps, full duration"
        else:
            # Truncate to fit at minimum bitrate
            trunc_duration = calc_truncated_duration(target_kb, MP3_MIN_BITRATE)
            if trunc_duration < 0.5:
                # Even half a second is too big — use minimum
                trunc_duration = 0.5
            encode_truncated(input_path, out_path, MP3_MIN_BITRATE, trunc_duration)
            method = f"MP3 8kbps, truncated to {trunc_duration:.1f}s"

        size_kb = os.path.getsize(out_path) / 1024
        print(f"  {target_kb:>5}k -> {size_kb:>8.1f} KB | {method} | {os.path.basename(out_path)}")

    print()


def main():
    base = Path(__file__).resolve().parent.parent

    podcasts = [
        ("1-bike-ride", "academic-vibing-vol1-confusion-is-the-highest-trust-signal.en.mp3", "vol1-en"),
        ("1-bike-ride", "academic-vibing-vol1-confusion-is-the-highest-trust-signal.nl.mp3", "vol1-nl"),
        ("2-substrate", "academic-vibing-vol2-the-view-from-the-substrate.en.mp3", "vol2-en"),
        ("2-substrate", "academic-vibing-vol2-the-view-from-the-substrate.nl.mp3", "vol2-nl"),
        ("3-open-window", "academic-vibing-vol3-the-open-window.en.mp3", "vol3-en"),
        ("3-open-window", "academic-vibing-vol3-the-open-window.nl.mp3", "vol3-nl"),
    ]

    for pod_dir, mp3_name, base_name in podcasts:
        input_path = str(base / "podcasts" / pod_dir / mp3_name)
        output_dir = str(base / "podcasts" / pod_dir / "spectrum")
        if not os.path.exists(input_path):
            print(f"SKIP (missing): {input_path}")
            continue
        generate_spectrum(input_path, output_dir, base_name)

    print("Done. All podcast spectra generated.")


if __name__ == "__main__":
    main()