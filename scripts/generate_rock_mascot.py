import os
import asyncio
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from moviepy import VideoClip, AudioFileClip, concatenate_videoclips
from edge_tts import Communicate

# Constants
WIDTH, HEIGHT = 1280, 720
FPS = 24
ROCK_COLOR = (240, 220, 180)  # Creamy fluffy color
EYE_COLOR = (40, 30, 20)
BG_COLOR = (255, 255, 255)
DIR_OUTPUT = "papers/vibe-blogs/"

# Font handling
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
try:
    FONT_LARGE = ImageFont.truetype(FONT_PATH, 80)
    FONT_MEDIUM = ImageFont.truetype(FONT_PATH, 50)
    FONT_SMALL = ImageFont.truetype(FONT_PATH, 30)
    FONT_URL = ImageFont.truetype(FONT_PATH, 25)
except:
    FONT_LARGE = ImageFont.load_default()
    FONT_MEDIUM = ImageFont.load_default()
    FONT_SMALL = ImageFont.load_default()
    FONT_URL = ImageFont.load_default()

def draw_rock(draw, x, y, scale=1.0, state="happy", rotation=0):
    """Draws Rock the puppy at (x, y)."""
    # Body (fluffy)
    body_rect = [x - 60 * scale, y - 40 * scale, x + 60 * scale, y + 60 * scale]
    draw.ellipse(body_rect, fill=ROCK_COLOR)

    # Fluff bits
    for i in range(12):
        angle = i * (360/12)
        fx = x + 60 * scale * np.cos(np.radians(angle))
        fy = y + 10 * scale + 50 * scale * np.sin(np.radians(angle))
        draw.ellipse([fx-15*scale, fy-15*scale, fx+15*scale, fy+15*scale], fill=ROCK_COLOR)

    # Head
    head_y = y - 60 * scale
    draw.ellipse([x - 50 * scale, head_y - 50 * scale, x + 50 * scale, head_y + 50 * scale], fill=ROCK_COLOR)

    # Ears
    ear_offset = 40 * scale
    if state == "ashamed" or state == "sleeping":
        # Droopy ears
        draw.ellipse([x - ear_offset - 20*scale, head_y - 10*scale, x - ear_offset + 10*scale, head_y + 60*scale], fill=ROCK_COLOR)
        draw.ellipse([x + ear_offset - 10*scale, head_y - 10*scale, x + ear_offset + 20*scale, head_y + 60*scale], fill=ROCK_COLOR)
    else:
        # Perky ears
        draw.ellipse([x - ear_offset - 15*scale, head_y - 60*scale, x - ear_offset + 15*scale, head_y + 10*scale], fill=ROCK_COLOR)
        draw.ellipse([x + ear_offset - 15*scale, head_y - 60*scale, x + ear_offset + 15*scale, head_y + 10*scale], fill=ROCK_COLOR)

    # Eyes
    eye_y = head_y - 10 * scale
    eye_size = 8 * scale
    if state == "ashamed":
        # Small sad eyes
        draw.ellipse([x - 20*scale - eye_size, eye_y, x - 20*scale + eye_size, eye_y + eye_size], fill=EYE_COLOR)
        draw.ellipse([x + 20*scale - eye_size, eye_y, x + 20*scale + eye_size, eye_y + eye_size], fill=EYE_COLOR)
    elif state == "sleeping":
        # Closed eyes
        draw.line([x-25*scale, eye_y, x-10*scale, eye_y], fill=EYE_COLOR, width=int(3*scale))
        draw.line([x+10*scale, eye_y, x+25*scale, eye_y], fill=EYE_COLOR, width=int(3*scale))
        # Zzz
        draw.text((x+30*scale, head_y - 40*scale), "z", fill=EYE_COLOR, font=FONT_SMALL)
        draw.text((x+45*scale, head_y - 60*scale), "Z", fill=EYE_COLOR, font=FONT_MEDIUM)
    else:
        # Big eager eyes
        draw.ellipse([x - 25*scale, eye_y - 15*scale, x - 5*scale, eye_y + 15*scale], fill=EYE_COLOR)
        draw.ellipse([x + 5*scale, eye_y - 15*scale, x + 25*scale, eye_y + 15*scale], fill=EYE_COLOR)
        # Pupils/Highlights
        draw.ellipse([x - 15*scale, eye_y - 10*scale, x - 10*scale, eye_y - 5*scale], fill=(255, 255, 255))
        draw.ellipse([x + 15*scale, eye_y - 10*scale, x + 20*scale, eye_y - 5*scale], fill=(255, 255, 255))

    # Nose
    draw.ellipse([x - 8*scale, head_y + 10*scale, x + 8*scale, head_y + 25*scale], fill=(0,0,0))

    # Mouth
    if state == "happy":
        draw.arc([x-15*scale, head_y + 20*scale, x+15*scale, head_y + 40*scale], 0, 180, fill=(0,0,0), width=3)
    elif state == "ashamed" or state == "sleeping":
        draw.arc([x-10*scale, head_y + 35*scale, x+10*scale, head_y + 45*scale], 180, 0, fill=(0,0,0), width=3)

def make_frame(t, scene_type):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    if scene_type == "chaos":
        # Rock running around frantically
        x = WIDTH/2 + 300 * np.sin(t * 10)
        y = HEIGHT - 200 + 50 * np.abs(np.sin(t * 15))
        draw_rock(draw, x, y, scale=1.8, state="happy")
        # Draw some "git" papers flying
        for i in range(5):
            px = (100 + i * 250 + t * 500) % WIDTH
            py = (100 + i * 100 + t * 200) % HEIGHT
            draw.rectangle([px, py, px+80, py+100], outline=(100, 100, 100), width=4)
            draw.text((px+10, py+30), "git", fill=(100,100,100), font=FONT_SMALL)

        draw.text((WIDTH/2 - 200, 50), "CHAOS!", fill=(255, 0, 0), font=FONT_LARGE)

    elif scene_type == "ashamed":
        # Rock looking sad in center
        draw_rock(draw, WIDTH/2, HEIGHT - 200, scale=1.8, state="ashamed")
        # Bigger red text
        draw.text((WIDTH/2 - 350, 100), "NO ROCK! NO!", fill=(200, 0, 0), font=FONT_LARGE)
        draw.text((WIDTH/2 - 500, 200), "STAY AWAY FROM GIT!", fill=(200, 0, 0), font=FONT_LARGE)

    elif scene_type == "playing":
        # Rock jumping on a repo folder
        jump = 150 * np.abs(np.sin(t * 8))
        draw_rock(draw, WIDTH/2, HEIGHT - 250 - jump, scale=1.8, state="happy")
        # Draw folder
        draw.rectangle([WIDTH/2 - 150, HEIGHT - 200, WIDTH/2 + 150, HEIGHT - 50], fill=(200, 180, 100))
        draw.text((WIDTH/2 - 60, HEIGHT - 140), ".git/", fill=(255, 255, 255), font=FONT_MEDIUM)

    elif scene_type == "outro":
        # Rock jumps in and then falls asleep
        if t < 2.5:
            progress = min(1.0, t / 1.5)
            x = WIDTH + 200 - (progress * (WIDTH/2 + 200))
            draw_rock(draw, x, HEIGHT - 200, scale=2.5, state="happy")
        else:
            draw_rock(draw, WIDTH/2, HEIGHT - 200, scale=2.5, state="sleeping")

        draw.text((150, 80), "Meet ROCK (v0.2) .....", fill=(0,0,0), font=FONT_LARGE)

        # Attogram URLs
        draw.text((150, 200), "github.com/attogram/academic-vibing", fill=(50, 50, 150), font=FONT_URL)
        draw.text((150, 240), "github.com/attogram/rock-talk", fill=(50, 50, 150), font=FONT_URL)

    return np.array(img)

async def generate_voice():
    text = "No rock! No! Stay away from git!"
    communicate = Communicate(text, "en-US-AndrewNeural")
    await communicate.save("human_voice.mp3")

def main():
    print("Generating voice...")
    asyncio.run(generate_voice())

    print("Creating clips...")
    clip_chaos = VideoClip(lambda t: make_frame(t, "chaos"), duration=4)

    audio_voice = AudioFileClip("human_voice.mp3")
    clip_ashamed = VideoClip(lambda t: make_frame(t, "ashamed"), duration=4)
    clip_ashamed = clip_ashamed.with_audio(audio_voice)

    clip_playing = VideoClip(lambda t: make_frame(t, "playing"), duration=4)

    clip_outro = VideoClip(lambda t: make_frame(t, "outro"), duration=8)

    print("Concatenating...")
    final_video = concatenate_videoclips([clip_chaos, clip_ashamed, clip_playing, clip_outro])

    output_path = os.path.join(DIR_OUTPUT, "rock-mascot-v0.2.mp4")
    print(f"Rendering to {output_path}...")
    final_video.write_videofile(output_path, fps=FPS, codec="libx264", audio_codec="aac")

    # Cleanup
    if os.path.exists("human_voice.mp3"):
        os.remove("human_voice.mp3")
    print("Done!")

if __name__ == "__main__":
    main()
