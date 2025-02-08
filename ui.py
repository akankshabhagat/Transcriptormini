import warnings
import torch
import tkinter as tk
from tkinter import filedialog, ttk
import logging
import os
import whisper
from tkinterdnd2 import TkinterDnD, DND_FILES
import subprocess
import json

# Suppress warnings
warnings.filterwarnings("ignore", message="You are using `torch.load` with `weights_only=False`.*")
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

# Default save directory
save_directory = os.getcwd()
logging.info(f"Default save directory set to: {save_directory}")

class TextBoxLogHandler(logging.Handler):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def emit(self, record):
        msg = self.format(record)
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.insert(tk.END, msg + '\n')
        self.text_widget.config(state=tk.DISABLED)
        self.text_widget.see(tk.END)

class DropZone(tk.Label):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(relief="groove", borderwidth=3, font=("Arial", 12), height=8, bg="#444", fg="white")
        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self.handle_drop)

    def handle_drop(self, event):
        file_path = event.data.strip("{}")  # Remove brackets if wrapped
        handle_dropped_file(file_path)

def handle_dropped_file(file_path):
    if not os.path.exists(file_path):
        logging.error(f"File or folder not found: {file_path}")
        return
    process_audio_file(file_path)

def process_audio_file(file_path):
    valid_extensions = ('.wav', '.mp3', '.m4a', '.flac', '.mp4', '.mkv', '.avi')
    if file_path.lower().endswith(valid_extensions):
        logging.info(f"Processing file: {file_path}")
        transcribe_audio(file_path, save_directory, file_format_var.get())
    else:
        logging.warning(f"Skipping non-audio file: {file_path}")

def browse_directory():
    global save_directory
    directory = filedialog.askdirectory(title="Select Save Directory")
    if directory:
        save_directory = directory
        logging.info(f"Save directory selected: {save_directory}")

def browse_file():
    file_path = filedialog.askopenfilename(title="Select an Audio/Video File",
                                           filetypes=[("Audio/Video Files", "*.wav;*.mp3;*.m4a;*.flac;*.mp4;*.mkv;*.avi")])
    if file_path:
        transcribe_audio(file_path, save_directory, file_format_var.get())

def check_ffmpeg():
    try:
        result = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info("FFmpeg is installed and working.")
            return True
    except FileNotFoundError:
        pass
    logging.error("FFmpeg is not installed or not in PATH.")
    return False

def transcribe_audio(filepath, save_directory=None, file_format="txt"):
    try:
        if not os.path.exists(filepath):
            error_msg = f"Audio file not found at: {filepath}"
            logging.error(error_msg)
            return

        logging.info(f"Loading audio file: {filepath}")
        if not check_ffmpeg():
            logging.error("FFmpeg is required but not found.")
            return

        model = whisper.load_model("tiny")  # Using tiny model for speed
        logging.info("Starting transcription...")
        result = model.transcribe(filepath)
        text_content = result.get("text", "").strip()

        if not text_content:
            logging.error("No speech detected in the audio file.")
            return

        if save_directory:
            file_name = "output_transcription.{}".format(file_format)
            file_path = os.path.join(save_directory, file_name)
        else:
            file_path = "output_transcription.{}".format(file_format)

        if file_format == "txt":
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(text_content)
        elif file_format == "json":
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump({"transcription": text_content}, f, ensure_ascii=False, indent=4)

        logging.info(f"Transcription saved to {file_path}")
        log_box.config(state=tk.NORMAL)
        log_box.insert(tk.END, f"Transcription completed. Saved as {file_format}\n")
        log_box.config(state=tk.DISABLED)
        log_box.see(tk.END)
        root.update()
    
    except Exception as e:
        logging.error(f"Error during transcription: {str(e)}")
        log_box.config(state=tk.NORMAL)
        log_box.insert(tk.END, f"Error: {str(e)}\n")
        log_box.config(state=tk.DISABLED)
        log_box.see(tk.END)
        root.update()

def clear_log():
    log_box.config(state=tk.NORMAL)
    log_box.delete(1.0, tk.END)
    log_box.config(state=tk.DISABLED)

def submit():
    logging.info("Submit button clicked. Implement logic here.")

# GUI Setup
root = TkinterDnD.Tk()
root.title("Media Transcription Tool")
root.geometry("600x450")

log_box = tk.Text(root, height=8, width=70, wrap=tk.WORD, state=tk.DISABLED, bg="#222", fg="white")
log_box.pack(pady=5)
log_handler = TextBoxLogHandler(log_box)
logging.getLogger().addHandler(log_handler)

drop_zone = DropZone(root, text="Drag and drop audio/video files here", width=50, height=6)
drop_zone.pack(fill=tk.X, padx=10, pady=5)

browse_file_button = tk.Button(root, text="Browse File", command=browse_file, width=15)
browse_file_button.pack(pady=2)

browse_dir_button = tk.Button(root, text="Select Save Directory", command=browse_directory, width=20)
browse_dir_button.pack(pady=2)

file_format_var = tk.StringVar(value="txt")
format_dropdown = ttk.Combobox(root, textvariable=file_format_var, values=["txt", "json"], state="readonly")
format_dropdown.pack(pady=2)

clear_button = tk.Button(root, text="Clear Log", command=clear_log, width=15)
clear_button.pack(pady=2)

submit_button = tk.Button(root, text="Submit", command=submit, width=15, bg="#4CAF50", fg="white")
submit_button.pack(pady=2)

root.mainloop()
