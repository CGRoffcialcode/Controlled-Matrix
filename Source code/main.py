"""CONTROLLED MATRIX - MATRIX ANIMATION USING PYTHON"""
""" * Copyright (C) 2025 CGRofficialcode * * This code is free software: you can redistribute it and/or modify * it under the terms of the GNU General Public License as published by * the Free Software Foundation, either version 3 of the License, or * (at your option) any later version. * * This code is distributed in the hope that it will be useful, * but WITHOUT ANY WARRANTY; without even the implied warranty of * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the * GNU General Public License for more details. * * You should have received a copy of the GNU General Public License * along with this code. If not, see <https://www.gnu.org/licenses/>. *// """

import random
import time
import os
import shutil
import keyboard
import sys
import imageio
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import requests
import tempfile
import subprocess

__version__ = "2.3.1"

GITHUB_RAW_URL = "https://raw.githubusercontent.com/CGRoffcialcode/Controlled-Matrix/main/Source%20code/main.py"

GITHUB_VERSION_URL = "https://raw.githubusercontent.com/CGRoffcialcode/Controlled-Matrix/main/version.txt"

def update_progress_bar(percent):
    bar_length = 40
    filled_length = int(bar_length * percent)
    bar = '=' * filled_length + '-' * (bar_length - filled_length)
    print(f"\rUpdating: [{bar}] {percent*100:5.1f}%", end='', flush=True)

def check_for_update():
    try:
        print("Checking for updates...")
        resp = requests.get(GITHUB_VERSION_URL, timeout=5)
        if resp.status_code != 200:
            print("Could not check for updates (version file not found).")
            input("Press Enter to continue...")
            return
        latest_version = resp.text.strip()
        if latest_version == __version__:
            print("You are running the latest version.")
            input("Press Enter to continue...")
            return
        if tuple(map(int, latest_version.split("."))) > tuple(map(int, __version__.split("."))):
            print(f"New version available: {latest_version}. Updating...")

            # If running as EXE, use updater method
            if getattr(sys, 'frozen', False):
                exe_url = "https://github.com/CGRoffcialcode/Controlled-Matrix/"
                tempdir = tempfile.gettempdir()
                new_exe_path = os.path.join(tempdir, "ControlledMatrix_new.exe")
                updater_path = os.path.join(tempdir, "matrix_updater.py")

                print("Downloading new version...")
                with requests.get(exe_url, stream=True) as r:
                    r.raise_for_status()
                    with open(new_exe_path, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)
                print("Writing updater script...")

                with open(updater_path, "w", encoding="utf-8") as f:
                    f.write(f"""
import os
import sys
import time
old_exe = r"{sys.executable}"
new_exe = r"{new_exe_path}"
final_exe = old_exe
time.sleep(1)
for i in range(10):
    try:
        os.remove(final_exe)
        break
    except Exception:
        time.sleep(1)
os.rename(new_exe, final_exe)
os.startfile(final_exe)
""")
                print("Launching updater...")
                subprocess.Popen([sys.executable, updater_path])
                print("Exiting for update...")
                sys.exit(0)
            else:
                # Running as script, do normal update
                code_resp = requests.get(GITHUB_RAW_URL, timeout=10, stream=True)
                if code_resp.status_code == 200:
                    shutil.copy(__file__, __file__ + ".bak")
                    total = int(code_resp.headers.get('content-length', 0))
                    downloaded = 0
                    code = ""
                    chunk_size = 8192
                    for chunk in code_resp.iter_content(chunk_size=chunk_size):
                        if chunk:
                            code += chunk.decode('utf-8')
                            downloaded += len(chunk)
                            percent = min(1.0, downloaded / total) if total else 1.0
                            update_progress_bar(percent)
                    print("\nWriting update...")
                    with open(__file__, "w", encoding="utf-8") as f:
                        f.write(code)
                    print("Update complete! Please restart Controlled Matrix.")
                    input("Press Enter to exit...")
                    sys.exit(0)
                else:
                    print("Failed to download the latest code.")
                    input("Press Enter to exit...")
                    sys.exit(0)
        else:
            print("Your version is newer than the latest release (dev build?).")
            input("Press Enter to exit...")
    except Exception as e:
        print(f"Update check failed: {e}")

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:'\",.<>?/`~"
array = list(characters)

ascii_art_list = [
    r"""
   _____            _             _ _          _   _   __       _  
  / ____|          | |           | | |        | | |  \/  |     |_|         
 | |     ___  _ __ | |_ _ __ ___ | | | ___  __| | | \  / | __ _| |_ _ __ ___  __
 | |    / _ \| '_ \| __| '__/ _ \| | |/ _ \/ _` | | |\/| |/ _` | __| '__| \ \/ /
 | |___| (_) | | | | |_| | | (_) | | |  __/ (_| | | |  | | (_| | |_| |  | |>  < 
  \_____\___/|_| |_|\__|_|  \___/|_|_|\___|\__,_| |_|  |_|\__,_|\__|_|  |_/_/\_\                                                                    
    """,
    r"""
   _____            _             _ _          _   _   __       _  
  / ____|          | |           | | |        | | |  \/  |     |_|         
 | |     ___  _ __ | |_ _ __ ___ | | | ___  __| | | \  / | __ _| |_ _ __ ___  __
 | |    / _ \| '_ \| __| '__/ _ \| | |/ _ \/ _` | | |\/| |/ _` | __| '__| \ \/ /
 | |___| (_) | | | | |_| | | (_) | | |  __/ (_| | | |  | | (_| | |_| |  | |>  < 
  \_____\___/|_| |_|\__|_|  \___/|_|_|\___|\__,_| |_|  |_|\__,_|\__|_|  |_/_/\_\                                        
    """,
    r"""
   _____            _             _ _          _   _   __       _  
  / ____|          | |           | | |        | | |  \/  |     |_|         
 | |     ___  _ __ | |_ _ __ ___ | | | ___  __| | | \  / | __ _| |_ _ __ ___  __
 | |    / _ \| '_ \| __| '__/ _ \| | |/ _ \/ _` | | |\/| |/ _` | __| '__| \ \/ /
 | |___| (_) | | | | |_| | | (_) | | |  __/ (_| | | |  | | (_| | |_| |  | |>  < 
  \_____\___/|_| |_|\__|_|  \___/|_|_|\___|\__,_| |_|  |_|\__,_|\__|_|  |_/_/\_\                                                            
    """,
]

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
    # New palette: Purple
    ("Purple", ["\033[38;5;93m", "\033[35m", "\033[2;35m"]),
    ("Glitch", None),
    ("Mixed", None),
    ("Mixed v2", None),
]
reset = "\033[0m"

def print_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(random.choice(ascii_art_list))
    print("="*60)
    print("        Controlled Matrix")
    print("="*60)
    print("  [v] Save video")
    print("  [t] Terminal animation")
    print("  [q] Quit")
    print("="*60)

def matrix():
    palette_index = 0
    columns, rows = shutil.get_terminal_size((80, 24))
    drops = [random.randint(0, rows) for _ in range(columns)]
    min_length = 2
    max_length = max(min_length, rows // 2)
    lengths = [random.randint(min_length, max_length) for _ in range(columns)]
    col_palettes = [random.randint(0, len(palettes)-4) for _ in range(columns)]

    mixed_v2_cycle = 2
    if palettes[palette_index][0] == "Mixed v2":
        try:
            mixed_v2_cycle = float(input("How many seconds per color for Mixed v2? (e.g. 2): "))
        except ValueError:
            mixed_v2_cycle = 2

    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    try:
        start_time = time.time()
        frame_count = 0
        while True:
            if keyboard.is_pressed('ctrl+alt+c'):
                palette_index = (palette_index + 1) % len(palettes)
                time.sleep(0.3)
                if palettes[palette_index][0] == "Mixed":
                    col_palettes = [random.randint(0, len(palettes)-4) for _ in range(columns)]
                elif palettes[palette_index][0] == "Mixed v2":
                    try:
                        mixed_v2_cycle = float(input("How many seconds per color for Mixed v2? (e.g. 2): "))
                    except ValueError:
                        mixed_v2_cycle = 2

            palette_name = palettes[palette_index][0]
            sys.stdout.write("\033[H")
            sys.stdout.flush()

            info_line = ""
            if palette_name == "Mixed v2":
                info_line = f"Color: Mixed v2 (cycling)"
            elif palette_name == "Glitch":
                info_line = f"Color: Glitch"
            elif palette_name != "Mixed":
                info_line = f"Color: {palette_name}"
                info_line = palettes[palette_index][1][0] + info_line + reset
            else:
                info_line = f"Color: Mixed"

            sys.stdout.write(info_line.ljust(columns) + "\n")
            sys.stdout.flush()

            if palette_name == "Mixed v2":
                elapsed = time.time() - start_time
                v2_palette_idx = int(elapsed // mixed_v2_cycle) % (len(palettes)-3)
            else:
                v2_palette_idx = None

            output_buffer = []
            for row in range(1, rows):
                line = ""
                for col in range(columns):
                    head = drops[col]
                    length = lengths[col]
                    if head - length < row <= head:
                        depth = head - row
                        if palette_name == "Mixed":
                            pal = palettes[col_palettes[col]][1]
                        elif palette_name == "Mixed v2":
                            pal = palettes[v2_palette_idx][1]
                        elif palette_name == "Glitch":
                            glitch_colors = [
                                "\033[92m", "\033[97m", "\033[96m", "\033[95m", "\033[93m"
                            ]
                            color = random.choice(glitch_colors)
                            style = random.choice(["\033[1m", "\033[2m", ""])
                            char = random.choice(array)
                            line += style + color + char + reset
                            continue
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

            sys.stdout.write("\n".join(output_buffer) + "\033[J")
            sys.stdout.flush()

            for i in range(columns):
                drops[i] += 1
                if drops[i] - lengths[i] > rows:
                    drops[i] = random.randint(0, rows // 4)
                    lengths[i] = random.randint(min_length, max_length)
                    if palette_name == "Mixed":
                        col_palettes[i] = random.randint(0, len(palettes)-4)
            time.sleep(0.035)
            frame_count += 1

    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()
        print(reset)

def save_matrix_video(
    frames=3000,
    fps=60,
    width=3840,
    height=2160,
    font_size=36,
    output="matrix_animation_4k.mp4",
    palette_index=0,
    mixed_v2_cycle=2,
    show_watermark=True,
    font_path="consola.ttf"
):
    video_palettes = [
        [(0,255,0), (0,180,0), (0,100,0)],      # Green
        [(255,0,0), (180,0,0), (100,0,0)],      # Red
        [(0,0,255), (0,0,180), (0,0,100)],      # Blue
        [(255,255,0), (180,180,0), (100,100,0)],# Yellow
        [(255,0,255), (180,0,180), (100,0,100)],# Magenta
        [(0,255,255), (0,180,180), (0,100,100)],# Cyan
        [(255,255,255), (180,180,180), (100,100,100)], # White
        [(128,128,128), (100,100,100), (60,60,60)],    # Gray
        [(128,200,255), (80,160,200), (40,100,150)],   # Light Blue
        [(255,128,0), (180,90,0), (100,50,0)],         # Orange
        [(255,0,128), (180,0,90), (100,0,50)],         # Pink
        [(148,0,211), (104,34,139), (75,0,130)],       # Purple (NEW: deep, medium, dark)
    ]

    columns = width // font_size
    rows = height // font_size

    try:
        font = ImageFont.truetype(font_path, font_size)
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
        keyboard = None

    watermark_texts = ["MATRIX", "CGRofficialcode"]
    watermark_colors = [(0,255,0), (255,255,255)]

    for frame in range(frames):
        if keyboard and keyboard.is_pressed('q'):
            print("Capture stopped by user.")
            break

        img = Image.new("RGB", (width, height), (0, 0, 0))
        draw = ImageDraw.Draw(img)

        watermark_idx = (frame // (fps // 2)) % 2
        watermark = watermark_texts[watermark_idx]
        watermark_color = watermark_colors[watermark_idx]

        if show_watermark:
            try:
                brand_font = ImageFont.truetype(font_path, font_size)
            except IOError:
                brand_font = font

            color_names_for_display = [p[0] for p in palettes] + ["Mixed", "Mixed v2"]
            current_palette_name = color_names_for_display[palette_index]
            color_text = f"Color: {current_palette_name}"

            bbox_color = draw.textbbox((0, 0), color_text, font=brand_font)
            draw.text((20, 10), color_text, font=brand_font, fill=(255,255,255))

            slide_width = width - 200
            max_shift = max(1, slide_width // (font_size // 2))
            shift = frame % max_shift
            x_pos = 20 + shift * (font_size // 2)
            draw.text((x_pos, 60), watermark, font=brand_font, fill=watermark_color)

            text_bl = "@cgrcodeyt"
            bbox_bl = draw.textbbox((0, 0), text_bl, font=brand_font)
            w_bl, h_bl = bbox_bl[2] - bbox_bl[0], bbox_bl[3] - bbox_bl[1]
            draw.text((20, height - h_bl - 20), text_bl, font=brand_font, fill=(255,255,255))

            w_br, h_br = w_bl, h_bl
            draw.text((width - w_br - 20, height - h_br - 20), text_bl, font=brand_font, fill=(255,255,255))

        for col in range(columns):
            head = drops[col]
            length = lengths[col]

            for row in range(rows):
                if head - length < row <= head:
                    depth = head - row
                    if palette_index == 11:
                        glitch_colors = [
                            (0,255,0), (255,255,255), (0,255,255), (255,0,255), (255,255,0)
                        ]
                        color = random.choice(glitch_colors)
                        rand_font_size = font_size + random.randint(-6, 8)
                        try:
                            rand_font = ImageFont.truetype(font_path, max(8, rand_font_size))
                        except Exception:
                            rand_font = font
                        char = random.choice(characters)
                        x = col * font_size
                        y = row * font_size
                        draw.text((x, y), char, font=rand_font, fill=color)
                    else:
                        if palette_index == len(video_palettes):
                            pal = video_palettes[col_palettes[col]]
                        elif palette_index == len(video_palettes)+1:
                            elapsed = frame / fps
                            v2_palette_idx = int(elapsed // mixed_v2_cycle) % (len(video_palettes))
                            pal = video_palettes[v2_palette_idx]
                        else:
                            pal = video_palettes[palette_index]

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

        if frame % max(1, fps // 2) == 0 or frame == frames - 1:
            percent = (frame + 1) / frames
            bar_length = 40
            filled_length = int(bar_length * percent)
            bar = '=' * filled_length + '-' * (bar_length - filled_length)
            print(
                f"\r[{'=' * filled_length}{'-' * (bar_length - filled_length)}] "
                f"{percent*100:5.1f}% | Frame {frame+1}/{frames}",
                end='',
                flush=True
            )
        writer.append_data(np.array(img))

    writer.close()
    print(f"\nSaved {output}")

if __name__ == "__main__":
    intro = r"""
   _____            _             _ _          _   _   __       _  
  / ____|          | |           | | |        | | |  \/  |     |_|         
 | |     ___  _ __ | |_ _ __ ___ | | | ___  __| | | \  / | __ _| |_ _ __ ___  __
 | |    / _ \| '_ \| __| '__/ _ \| | |/ _ \/ _` | | |\/| |/ _` | __| '__| \ \/ /
 | |___| (_) | | | | |_| | | (_) | | |  __/ (_| | | |  | | (_| | |_| |  | |>  < 
  \_____\___/|_| |_|\__|_|  \___/|_|_|\___|\__,_| |_|  |_|\__,_|\__|_|  |_/_/\_\
                                                                                 """
    print(intro)
    check_for_update()
    while True:
        print_menu()
        choice = input("Select an option: ").strip().lower()
        if choice == 'q':
            print("Goodbye!")
            break
        elif choice == 'v':
            color_names_for_display = [p[0] for p in palettes]
            print("\nAvailable colors:")
            for idx, name in enumerate(color_names_for_display):
                print(f"  {idx}: {name}")
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

            font_path = input("Enter font path (leave blank for default 'consola.ttf'): ").strip()
            if not font_path:
                font_path = "consola.ttf"

            while True:
                try:
                    width = int(input("Video width (e.g. 3840): ") or "3840")
                    height = int(input("Video height (e.g. 2160): ") or "2160")
                    if width > 0 and height > 0:
                        break
                    else:
                        print("Please enter positive integers for width and height.")
                except ValueError:
                    print("Please enter valid integers.")

            while True:
                watermark_choice = input("Do you want to keep the watermark? (y/n): ").strip().lower()
                if watermark_choice in ("y", "n"):
                    break
                else:
                    print("Please enter 'y' or 'n'.")

            if watermark_choice == "n":
                print("Reminder: Removing the watermark is for personal use only. Do not share videos without the watermark. The watermark is there for attribution.")

            frames = int(minutes * 60 * fps)
            duration_sec = minutes * 60
            mb_per_sec = 4
            estimated_size_mb = duration_sec * mb_per_sec
            estimated_size_gb = estimated_size_mb / 1024
            print(f"\nEstimated video size: {estimated_size_mb:.1f} MB ({estimated_size_gb:.2f} GB) for {minutes} minute(s) at {width}x{height} {fps}fps.\n")

            save_matrix_video(
                frames=frames,
                fps=fps,
                width=width,
                height=height,
                palette_index=color_idx,
                mixed_v2_cycle=mixed_v2_cycle,
                show_watermark=(watermark_choice == "y"),
                font_path=font_path
            )
            input("\nPress Enter to return to menu...")
        elif choice == 't':
            matrix()
            input("\nPress Enter to return to menu...")
        else:
            print("Invalid option. Please try again.")