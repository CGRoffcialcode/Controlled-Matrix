"""MATRIX ANIMATION USING PYTHON"""
""" * Copyright (C) 2025 CGRofficialcode * * This code is free software: you can redistribute it and/or modify * it under the terms of the GNU General Public License as published by * the Free Software Foundation, either version 3 of the License, or * (at your option) any later version. * * Thiscode is distributed in the hope that it will be useful, * but WITHOUT ANY WARRANTY; without even the implied warranty of * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the * GNU General Public License for more details. * * You should have received a copy of the GNU General Public License * along with this code. If not, see <https://www.gnu.org/licenses/>. *// """
import random
import time
import os
import shutil
import keyboard # Keep for Ctrl+Alt+C detection, but be aware of its limitations
import sys      # For sys.stdout.write and sys.stdout.flush
import imageio
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import argparse
import signal

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:'\",.<>?/`~"
array = list(characters)

# Define color palettes for terminal
palettes = [
    ("Green", ["\033[92m", "\033[32m", "\033[2;32m"]),
    ("Red", ["\033[91m", "\033[31m", "\033[2;31m"]),
    ("Blue", ["\033[94m", "\033[34m", "\033[2;34m"]),
    ("Yellow", ["\033[93m", "\033[33m", "\033[2;33m"]),
    ("Magenta", ["\033[95m", "\033[35m", "\033[2;35m"]),
    ("Cyan", ["\033[96m", "\033[36m", "\033[2;36m"]),
    ("White", ["\033[97m", "\033[37m", "\033[2;37m"]),
    ("Gray", ["\033[90m", "\033[37m", "\033[2;37m"]),
    ("Light Blue", ["\033[96m", "\033[94m", "\033[2;34m"]),
    ("Orange", ["\033[38;5;208m", "\033[33m", "\033[2;33m"]),
    ("Pink", ["\033[38;5;213m", "\033[35m", "\033[2;35m"]),
    ("Mixed", None),
    ("Mixed v2", None),
]
reset = "\033[0m"

def matrix():
    palette_index = 0
    columns, rows = shutil.get_terminal_size((80, 24))
    drops = [random.randint(0, rows) for _ in range(columns)]
    min_length = 2
    max_length = max(min_length, rows // 2)
    lengths = [random.randint(min_length, max_length) for _ in range(columns)]
    col_palettes = [random.randint(0, len(palettes)-3) for _ in range(columns)] # exclude Mixed/Mixed v2

    mixed_v2_cycle = 2
    if palettes[palette_index][0] == "Mixed v2":
        try:
            mixed_v2_cycle = float(input("How many seconds per color for Mixed v2? (e.g. 2): "))
        except ValueError:
            mixed_v2_cycle = 2

    # --- Cursor hiding starts here ---
    sys.stdout.write("\033[?25l") # Hide cursor
    sys.stdout.flush() # Ensure it's applied immediately
    # --- Cursor hiding ends here ---

    try:
        start_time = time.time()
        while True:
            # Palette switching with Ctrl+Alt+C
            if keyboard.is_pressed('ctrl+alt+c'):
                palette_index = (palette_index + 1) % len(palettes)
                time.sleep(0.3) # Debounce
                if palettes[palette_index][0] == "Mixed":
                    col_palettes = [random.randint(0, len(palettes)-3) for _ in range(columns)]
                elif palettes[palette_index][0] == "Mixed v2":
                    try:
                        mixed_v2_cycle = float(input("How many seconds per color for Mixed v2? (e.g. 2): "))
                    except ValueError:
                        mixed_v2_cycle = 2

            palette_name = palettes[palette_index][0]

            # Move cursor to top left - use sys.stdout.write
            sys.stdout.write("\033[H")
            sys.stdout.flush() # Flush after cursor movement

            # Palette info at top left
            info_line = ""
            if palette_name == "Mixed v2":
                info_line = f"Color: Mixed v2 (cycling)"
            elif palette_name != "Mixed":
                info_line = f"Color: {palette_name}"
                info_line = palettes[palette_index][1][0] + info_line + reset
            else:
                info_line = f"Color: Mixed"

            sys.stdout.write(info_line.ljust(columns) + "\n") # Add newline and ensure flush
            sys.stdout.flush()


            # For Mixed v2, determine which palette to use
            if palette_name == "Mixed v2":
                elapsed = time.time() - start_time
                v2_palette_idx = int(elapsed // mixed_v2_cycle) % (len(palettes)-2)
            else:
                v2_palette_idx = None

            # Render matrix
            # Use a list of lines, then print all at once to minimize redraw issues
            output_buffer = []
            for row in range(1, rows): # Start from row 1, as row 0 is for info_line
                line = ""
                for col in range(columns):
                    head = drops[col]
                    length = lengths[col]
                    if head - length < row <= head:
                        depth = head - row
                        # Choose palette
                        if palette_name == "Mixed":
                            pal = palettes[col_palettes[col]][1]
                        elif palette_name == "Mixed v2":
                            pal = palettes[v2_palette_idx][1]
                        else:
                            pal = palettes[palette_index][1]

                        if depth == 0:
                            color = pal[0]
                        elif depth < 4:
                            color = pal[1]
                        else:
                            color = pal[2]
                        line += color + random.choice(array) + reset
                    else:
                        line += " "
                output_buffer.append(line.ljust(columns))

            # Print all buffered lines
            sys.stdout.write("\n".join(output_buffer) + "\033[J") # Clear rest of screen below cursor
            sys.stdout.flush()


            # Update drops and lengths
            for i in range(columns):
                drops[i] += 1
                if drops[i] - lengths[i] > rows:
                    drops[i] = random.randint(0, rows // 4)
                    lengths[i] = random.randint(6, rows // 2)
                    if palette_name == "Mixed":
                        col_palettes[i] = random.randint(0, len(palettes)-3)
            time.sleep(0.035)

    except KeyboardInterrupt:
        # User pressed Ctrl+C
        pass
    finally:
        # --- Cursor showing starts here ---
        sys.stdout.write("\033[?25h") # Show cursor
        sys.stdout.flush() # Ensure it's applied immediately
        print(reset) # Ensure terminal colors are reset
        # --- Cursor showing ends here ---


# The save_matrix_video function remains unchanged as it's for video generation.
def save_matrix_video(
    frames=3000,
    fps=60,
    width=3840,
    height=2160,
    font_size=36,
    output="matrix_animation_4k.mp4",
    palette_index=0,
    mixed_v2_cycle=2,
    show_watermark=True
):
    video_palettes = [
        [(0,255,0), (0,180,0), (0,100,0)], # Green
        [(255,0,0), (180,0,0), (100,0,0)], # Red
        [(0,0,255), (0,0,180), (0,0,100)], # Blue
        [(255,255,0), (180,180,0), (100,100,0)],# Yellow
        [(255,0,255), (180,0,180), (100,0,100)],# Magenta
        [(0,255,255), (0,180,180), (0,100,100)],# Cyan
        [(255,255,255), (180,180,180), (100,100,100)], # White
        [(128,128,128), (100,100,100), (60,60,60)], # Gray
        [(128,200,255), (80,160,200), (40,100,150)], # Light Blue
        [(255,128,0), (180,90,0), (100,50,0)], # Orange
        [(255,0,128), (180,0,90), (100,0,50)], # Pink
    ]

    columns = width // font_size
    rows = height // font_size

    try:
        font = ImageFont.truetype("consola.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    drops = [random.randint(0, rows) for _ in range(columns)]
    lengths = [random.randint(6, rows // 2) for _ in range(columns)]
    col_palettes = [random.randint(0, len(video_palettes)-1) for _ in range(columns)]

    writer = imageio.get_writer(output, fps=fps)
    print("Press 'q' to stop the capture early.")

    try:
        import keyboard
    except ImportError:
        print("The 'keyboard' module is not installed. Video capture cannot be stopped early with 'q'.")
        keyboard = None


    for frame in range(frames):
        if keyboard and keyboard.is_pressed('q'):
            print("Capture stopped by user.")
            break

        img = Image.new("RGB", (width, height), (0, 0, 0))
        draw = ImageDraw.Draw(img)

        elapsed = frame / fps
        timer_str = time.strftime('%H:%M:%S', time.gmtime(elapsed))

        if show_watermark:
            try:
                brand_font = ImageFont.truetype("consola.ttf", font_size)
            except IOError:
                brand_font = font

            color_names_for_display = [p[0] for p in palettes] + ["Mixed", "Mixed v2"]
            current_palette_name = color_names_for_display[palette_index]
            # Remove timer from watermark
            # timer_text = f"Timer: {timer_str} Color: {current_palette_name}"
            color_text = f"Color: {current_palette_name}"

            bbox_color = draw.textbbox((0, 0), color_text, font=brand_font)
            draw.text((20, 10), color_text, font=brand_font, fill=(255,255,255))

            text_top_right = "@CGRofficialcode"
            bbox_tr = draw.textbbox((0, 0), text_top_right, font=brand_font)
            w_tr, h_tr = bbox_tr[2] - bbox_tr[0], bbox_tr[3] - bbox_tr[1]
            draw.text((width - w_tr - 20, 10), text_top_right, font=brand_font, fill=(255,255,255))

            text_bl = "@cgrcodeyt"
            bbox_bl = draw.textbbox((0, 0), text_bl, font=brand_font)
            w_bl, h_bl = bbox_bl[2] - bbox_bl[0], bbox_bl[3] - bbox_bl[1]
            draw.text((20, height - h_bl - 20), text_bl, font=brand_font, fill=(255,255,255))

            w_br, h_br = w_bl, h_bl
            draw.text((width - w_br - 20, height - h_br - 20), text_bl, font=brand_font, fill=(255,255,255))


        for col in range(columns):
            head = drops[col]
            length = lengths[col]

            if palette_index == len(video_palettes):
                pal = video_palettes[col_palettes[col]]
            elif palette_index == len(video_palettes)+1:
                elapsed = frame / fps
                v2_palette_idx = int(elapsed // mixed_v2_cycle) % (len(video_palettes))
                pal = video_palettes[v2_palette_idx]
            else:
                pal = video_palettes[palette_index]

            for row in range(rows):
                if head - length < row <= head:
                    depth = head - row
                    if depth == 0:
                        color = pal[0]
                    elif depth < 4:
                        color = pal[1]
                    else:
                        color = pal[2]
                    char = random.choice(characters)
                    x = col * font_size
                    y = row * font_size
                    draw.text((x, y), char, font=font, fill=color)

        for i in range(columns):
            drops[i] += 1
            if drops[i] - lengths[i] > rows:
                drops[i] = random.randint(0, rows // 4)
                lengths[i] = random.randint(6, rows // 2)
                if palette_index == len(video_palettes):
                    col_palettes[i] = random.randint(0, len(video_palettes)-1)

        if frame % fps == 0 or frame == frames - 1:
            print(f"Video Timer: {timer_str} / {time.strftime('%H:%M:%S', time.gmtime(frames/fps))}", end='\r')
        writer.append_data(np.array(img))

    writer.close()
    print(f"\nSaved {output}")


if __name__ == "__main__":
    intro = r"""             
  / ____|          | |           | | |        | | |  \/  |     | |          
 | |     ___  _ __ | |_ _ __ ___ | | | ___  __| | | \  / | __ _| |_ _ __ ___  __
 | |    / _ \| '_ \| __| '__/ _ \| | |/ _ \/ _` | | |\/| |/ _` | __| '__| \ \/ /
 | |___| (_) | | | | |_| | | (_) | | |  __/ (_| | | |  | | (_| | |_| |  | |>  < 
  \_____\___/|_| |_|\__|_|  \___/|_|_|\___|\__,_| |_|  |_|\__,_|\__|_|  |_/_/\_\
                                                                                 """
    print(intro)
    choice = input("Type 'v' to save video, anything else for terminal animation: ").strip().lower()

    color_names_for_display = [p[0] for p in palettes]

if choice == 'v':
    print("Available colors:")
    for idx, name in enumerate(color_names_for_display):
        print(f"{idx}: {name}")
    while True:
        try:
            color_idx = int(input("Choose the color number for the Matrix animation: "))
            if 0 <= color_idx < len(color_names_for_display):
                break
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")

    mixed_v2_cycle = 2
    if color_idx == len(color_names_for_display)-1:
        try:
            mixed_v2_cycle = float(input("How many seconds per color for Mixed v2? (e.g. 2): "))
        except ValueError:
            mixed_v2_cycle = 2

    while True:
        try:
            minutes = float(input("How many minutes do you want the animation to be? (e.g. 1 for 1 minute): "))
            if minutes > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            fps = int(input("How many frames per second? (e.g. 60): "))
            if fps > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")

    while True:
        watermark_choice = input("Do you want to keep the watermark? (y/n): ").strip().lower()
        if watermark_choice in ("y", "n"):
            break
        else:
            print("Please enter 'y' or 'n'.")

    if watermark_choice == "n":
        print("Reminder: Removing the watermark is for personal use only. Do not share videos without the watermark. The watermark is there for attribution.")


    frames = int(minutes * 60 * fps)

    # --- Estimate video size and display to user ---
    duration_sec = minutes * 60
    mb_per_sec = 4  # 4 MB/sec for 4K (rough estimate)
    estimated_size_mb = duration_sec * mb_per_sec
    estimated_size_gb = estimated_size_mb / 1024
    print(f"\nEstimated video size: {estimated_size_mb:.1f} MB ({estimated_size_gb:.2f} GB) for {minutes} minute(s) at 4K {fps}fps.\n")

    save_matrix_video(
            frames=frames,
            fps=fps,
            palette_index=color_idx,
            mixed_v2_cycle=mixed_v2_cycle,
            show_watermark=(watermark_choice == "y")
        )
else:
        matrix()