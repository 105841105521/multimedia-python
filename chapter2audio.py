from pydub import AudioSegment
import pygame

# Memuat file audio
audio = AudioSegment.from_file('AUDIO.mp3')

# Mengonversi ke format WAV
audio.export('result.wav', format='wav')

# Memotong audio menjadi 10 detik pertama
clipped_audio = audio[:10000]
clipped_audio.export('clipped_result.mp3', format='mp3')

# Menggabungkan audio asli dengan hasil potongan
combined_audio = audio + clipped_audio
combined_audio.export('combined_result.mp3', format='mp3')

# Mengubah volume audio sebesar 10dB
louder_audio = audio + 10
louder_audio.export('louder_result.mp3', format='mp3')

# Memutar file audio hasil konversi dengan pygame
pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('result.wav')
sound.play()

# Menunggu sampai audio selesai diputar
pygame.time.wait(int(sound.get_length() * 1000))  