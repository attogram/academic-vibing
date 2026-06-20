# Skill: Video Mascot Generation (v0.1)

## ROCK
Context: Mascot development & procedural animation.
Target: Cute, lo-fi cartoon mascot for repo vibes.
Stack: Pillow (Graphics) → MoviePy (Sequencing) → edge-tts (Voice-over) → MP4.
Persona: ROCK - Fluffy, eager, slightly chaotic puppy.
Mechanism: Procedural frame generation + synchronized audio triggers.

## PROSE

### 1. Conceptual Design
ROCK is a fluffy puppy, the mascot of the Attogram project. He represents the eager, active, and sometimes "sleepy" nature of AI agents in a high-velocity research environment.
- **Visuals:** Simple shapes, expressive eyes, "git-aware" behavior.
- **Audio:** High-energy human interactions contrasted with puppy soundscapes (procedural).

### 2. Procedural Animation (The Script)
Unlike traditional video editing, mascot videos are generated via script.
- **Graphics Engine:** `Pillow` is used to draw frames from scratch. This allows for dynamic adjustment of "Rock's" expression and pose based on script parameters.
- **Assembly:** `MoviePy` handles the stitching of frames into clips, managing duration, transitions, and audio layering.

### 3. Voice-over Integration
Use `edge-tts` for any human or "narrator" roles within the mascot clips.
- **Default Human Voice:** `en-US-AndrewNeural` or `en-GB-SoniaNeural`.
- **Command:** `edge-tts --text "No rock! No!" --write-media human_voice.mp3`

### 4. Rendering & Output
- **Target Format:** H.264 MP4 (Web compatible).
- **Directory:** Store final assets in `papers/vibe-blogs/`.
- **Naming Convention:** `rock-mascot-<topic>.mp4`.

### 5. Verification
Generated videos should be checked for:
- Frame-rate consistency (default 24fps).
- Audio-Visual synchronization.
- Character consistency (Does Rock look like Rock?).
