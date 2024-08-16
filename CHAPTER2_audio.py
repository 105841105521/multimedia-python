from pydub import AudioSegment
import pygame

# 2.2.1 Memuat File Audio
audio = AudioSegment.from_file('Example.mp3')

# 2.2.2 Pemotongan Audio
clipped_audio = audio[:10000]  # 10 detik pertama
clipped_audio.export('clipped_result.mp3', format='mp3')

# 2.2.3 Penggabungan Audio
audio2 = AudioSegment.from_file('Example.wav')
combined_audio = audio + audio2
combined_audio.export('combined_result.mp3', format='mp3')

# 2.2.4 Pengubahan Format Audio
audio.export('converted_result.wav', format='wav')

# 2.2.5 Pengaturan Volume
louder_audio = audio + 5  # Meningkatkan volume sebesar 5dB
louder_audio.export('louder_result.mp3', format='mp3')

# 2.2.6 Memutar Audio Menggunakan Pygame
pygame.mixer.init()  # Inisialisasi pygame mixer
pygame.mixer.music.load('converted_result.wav')  # Memuat file audio
pygame.mixer.music.play()  # Memutar audio

# Menunggu sampai audio selesai diputar
while pygame.mixer.music.get_busy():
    continue
