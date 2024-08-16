import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx
import pygame
from PIL import Image, ImageTk
import os

# Inisialisasi pygame untuk audio
pygame.mixer.init()

# Fungsi untuk memutar musik menggunakan pygame
def play_music():
    file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3 *.wav")])
    if file_path:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

# Fungsi untuk memuat dan memutar video
def load_video():
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi")])
    if file_path:
        video = VideoFileClip(file_path)
        video.preview()  # Memutar video

# Fungsi untuk memotong video
def cut_video():
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi")])
    if file_path:
        start_time = 0  # Mulai dari detik ke-0
        end_time = 10   # Sampai detik ke-10
        output_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
        if output_path:
            video = VideoFileClip(file_path).subclip(start_time, end_time)
            video.write_videofile(output_path, codec="libx264")
            print(f"Video saved to {output_path}")

# Fungsi untuk menggabungkan video
def merge_videos():
    file_paths = filedialog.askopenfilenames(filetypes=[("Video files", "*.mp4 *.avi")])
    if file_paths:
        clips = [VideoFileClip(fp) for fp in file_paths]
        final_clip = concatenate_videoclips(clips)
        output_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
        if output_path:
            final_clip.write_videofile(output_path, codec="libx264")
            print(f"Videos merged and saved to {output_path}")

# Fungsi untuk mempercepat video
def speed_up_video():
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi")])
    if file_path:
        video = VideoFileClip(file_path).fx(vfx.speedx, 2)
        output_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
        if output_path:
            video.write_videofile(output_path, codec="libx264")
            print(f"Video sped up and saved to {output_path}")

# Fungsi untuk memuat dan menampilkan gambar
def load_image():
    image_path = 'example.jpeg'  
    if os.path.exists(image_path):
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
    else:
        print(f"Image not found: {image_path}")

# Membuat jendela utama
root = tk.Tk()
root.title("Multimedia Application")

# Tombol untuk memutar video
play_video_button = tk.Button(root, text="Play Video", command=load_video)
play_video_button.pack(pady=5)

# Tombol untuk memotong video
cut_video_button = tk.Button(root, text="Cut Video", command=cut_video)
cut_video_button.pack(pady=5)

# Tombol untuk menggabungkan video
merge_video_button = tk.Button(root, text="Merge Videos", command=merge_videos)
merge_video_button.pack(pady=5)

# Tombol untuk mempercepat video
speed_up_video_button = tk.Button(root, text="Speed Up Video", command=speed_up_video)
speed_up_video_button.pack(pady=5)

# Tombol untuk memutar musik
play_music_button = tk.Button(root, text="Play Music", command=play_music)
play_music_button.pack(pady=5)

# Tombol untuk memuat dan menampilkan gambar
load_image_button = tk.Button(root, text="Load Image", command=load_image)
load_image_button.pack(pady=5)

# Label untuk menampilkan gambar
image_label = tk.Label(root)
image_label.pack(pady=10)

# Memuat gambar 
load_image()

# Menjalankan loop acara Tkinter
root.mainloop()

# Hentikan pygame setelah loop utama berhenti
pygame.mixer.music.stop()
pygame.quit()
