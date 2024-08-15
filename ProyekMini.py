import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play
import os
import tempfile

# Tentukan jalur ffmpeg dan pastikan ini benar
ffmpeg_path = r"C:\Users\LENOVO\bin\ffmpeg-7.0.2-essentials_build\bin\ffmpeg.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(ffmpeg_path)
AudioSegment.converter = ffmpeg_path

# Debugging untuk memastikan ffmpeg terdeteksi dengan benar
print(f"ffmpeg path: {ffmpeg_path}")
print(f"Environment PATH: {os.environ['PATH']}")

# Set direktori sementara untuk file yang diproses oleh pydub
temp_dir = r'C:\Users\LENOVO\OneDrive\Dokumen\GitHub\multimedia-python\temp'
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)
tempfile.tempdir = temp_dir

# Debugging untuk melihat direktori sementara
print(f"Temporary directory: {tempfile.gettempdir()}")

# Membuat jendela utama
root = tk.Tk()
root.title("Music Player")

# Fungsi untuk memutar musik
def play_music():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav *.ogg")])
    if file_path:
        try:
            print(f"Selected file: {file_path}")  # Debugging
            # Memuat file audio
            audio = AudioSegment.from_file(file_path)
            # Memutar audio
            play(audio)
        except Exception as e:
            print(f"Error: {e}")

# Membuat tombol play
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack(pady=20)

# Menjalankan loop acara Tkinter
root.mainloop()
