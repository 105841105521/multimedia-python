import tkinter as tk
from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx
from PIL import Image, ImageTk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play

# Membuat jendela utama
root = tk.Tk()
root.title("Multimedia Application")

# Memuat file video
video = VideoFileClip('video.mp4')
video.write_videofile('result.mp4')

# Memotong video 10 detik pertama
short_video = video.subclip(0, 10)
short_video.write_videofile('short_result.mp4')

# Menggabungkan video asli dan video potongan
combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('combined_result.mp4')

# Membalikkan video
reversed_video = short_video.fx(vfx.time_mirror)
reversed_video.write_videofile('reversed_result.mp4')

# Mempercepat video 2x
sped_up_video = short_video.fx(vfx.speedx, 2)
sped_up_video.write_videofile('sped_up_result.mp4')

# Memuat dan menampilkan gambar
image = Image.open('example.jpeg')
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.pack()

# Fungsi untuk memutar musik
def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        audio = AudioSegment.from_file(file_path)
        play(audio)

# Tombol untuk memutar musik
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

# Menjalankan loop Tkinter
root.mainloop()
