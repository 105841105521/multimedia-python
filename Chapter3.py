import tkinter as tk
from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx
from pydub import AudioSegment
from pydub.playback import play
from tkinter import filedialog

root = tk.Tk()
root.title("Multimedia Application")

video = None
short_video = None
combined_video = None
reversed_video = None
sped_up_video = None

def load_video():
    global video
    file_path = 'video.MP4' 
    video = VideoFileClip(file_path)
    print("Video loaded:", file_path)

def save_video():
    global video
    if video:
        save_path = filedialog.asksaveasfilename(defaultextension=".mp4")
        video.write_videofile(save_path)
        print("Video saved as:", save_path)

def cut_video():
    global short_video
    if video:
        short_video = video.subclip(0, 10)  # Mendapatkan 10 detik pertama
        short_video.write_videofile('video.mp4')
        print("Short video saved as 'short_result.mp4'")

def combine_video():
    global combined_video
    if video and short_video:
        combined_video = concatenate_videoclips([video, short_video])
        combined_video.write_videofile('video.mp4')
        print("Combined video saved as 'combined_result.mp4'")

def add_effect():
    global reversed_video
    if short_video:
        reversed_video = short_video.fx(vfx.time_mirror)  # Membalikkan video
        reversed_video.write_videofile('video.mp4')
        print("Reversed video saved as 'reversed_result.mp4'")

def speed_up_video():
    global sped_up_video
    if short_video:
        sped_up_video = short_video.fx(vfx.speedx, 2)  # Mempercepat video 2x
        sped_up_video.write_videofile('video.mp4')
        print("Sped-up video saved as 'sped_up_result.mp4'")

def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        audio = AudioSegment.from_file(file_path)
        play(audio)
        print("Playing audio:", file_path)

load_button = tk.Button(root, text="Load Video", command=load_video)
save_button = tk.Button(root, text="Save Video", command=save_video)
cut_button = tk.Button(root, text="Cut Video", command=cut_video)
combine_button = tk.Button(root, text="Combine Video", command=combine_video)
effect_button = tk.Button(root, text="Add Effect", command=add_effect)
speed_button = tk.Button(root, text="Speed Up Video", command=speed_up_video)
music_button = tk.Button(root, text="Play Music", command=play_music)

load_button.pack()
save_button.pack()
cut_button.pack()
combine_button.pack()
effect_button.pack()
speed_button.pack()
music_button.pack()

root.mainloop()
