

# 🎙️ Transcriptormini

## 📌 Overview  
**Transcripto Mini** is a lightweight, user-friendly **media transcription tool** that converts audio and video files into text using OpenAI's **Whisper** model. It provides an intuitive **drag-and-drop** interface, supports multiple file formats, and allows users to save transcriptions in **TXT** or **JSON** formats.  

## 🚀 Features  
✅ **Drag & Drop Support** – Simply drop audio/video files into the app  
✅ **Multiple File Formats** – Supports `.wav`, `.mp3`, `.m4a`, `.flac`, `.mp4`, `.mkv`, `.avi`  
✅ **AI-Powered Transcription** – Uses OpenAI’s **Whisper Tiny** model for fast speech-to-text conversion  
✅ **FFmpeg Integration** – Ensures smooth processing of various media formats  
✅ **User-Friendly GUI** – Built with **Tkinter**, with real-time logging  
✅ **Save Transcriptions** – Choose where to store your transcribed files  

## 🖥️ Screenshots  
![image](https://github.com/user-attachments/assets/f7e1a713-faf9-43e5-a9dd-525a3415a13c)


## 🛠️ Installation  

### 1️⃣ Prerequisites  
Make sure you have:  
- **Python 3.8+** installed  
- **FFmpeg** (required for media processing)  

#### Install FFmpeg:  
- **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/) and add it to your system PATH.  
- **macOS**:  
  ```bash
  brew install ffmpeg
  ```  
- **Linux**:  
  ```bash
  sudo apt-get install ffmpeg
  ```

### 2️⃣ Install Dependencies  
Clone the repository and install required packages:  
```bash
git clone https://github.com/your-repo/transcripto-mini.git
cd transcripto-mini
pip install -r requirements.txt
```

## 📂 Usage  

### Run the Application  
```bash
python main.py
```

### How to Transcribe Media Files  
1. **Drag & Drop** an audio/video file into the window **OR** click **Browse File**.  
2. Choose the **output format** (`txt` or `json`).  
3. Click **Submit** to start transcription.  
4. The transcription will be saved in the **selected directory**.  

## ⚙️ Supported Formats  
| Media Type  | Extensions                      |
|-------------|--------------------------------|
| Audio       | `.wav`, `.mp3`, `.m4a`, `.flac` |
| Video       | `.mp4`, `.mkv`, `.avi`          |

## 📜 Requirements  
**Python Packages:**  
```txt
torch
whisper
tk
tkinterdnd2
ffmpeg-python
```

## 🎥 Demo  
📹 _(https://youtu.be/NpxjdWnK4BM)_  

## 🛠️ Troubleshooting  
- **FFmpeg Not Found**: Ensure it's installed and added to your system PATH.  
- **No Speech Detected**: Try using a different Whisper model (`base`, `small`, etc.).  
- **Application Not Opening**: Run `python main.py` from the terminal and check for errors.  

## 📌 Contributing  
Feel free to submit **issues** or **pull requests** to improve Transcripto Mini.  

## 📜 License  
This project is licensed under the **MIT License**.  

---
