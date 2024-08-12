from pydub import AudioSegment

# Load audio file
try:
    audio = AudioSegment.from_file('AUDIO.mp3')
    print("✅ Audio loaded successfully.")
except Exception as e:
    print(f"❌ An error occurred while loading audio: {e}")
    exit()

# Save audio file
try:
    audio.export('result.mp3', format='mp3')
    print("✅ Audio saved as result.mp3.")
except Exception as e:
    print(f"❌ An error occurred while saving audio: {e}")

# Audio clipping
try:
    clipped_audio = audio[:10000]  # Get the first 10 seconds
    clipped_audio.export('clipped_result.mp3', format='mp3')
    print("✅ Audio clipped and saved as clipped_result.mp3.")
except Exception as e:
    print(f"❌ An error occurred while clipping audio: {e}")

# Audio merging
try:
    combined_audio = audio + clipped_audio
    combined_audio.export('combined_result.mp3', format='mp3')
    print("✅ Audio merged and saved as combined_result.mp3.")
except Exception as e:
    print(f"❌ An error occurred while merging audio: {e}")

# Audio format conversion
try:
    audio.export('result.wav', format='wav')
    print("✅ Audio converted and saved as result.wav.")
except Exception as e:
    print(f"❌ An error occurred while converting audio format: {e}")

# Audio volume adjustment
try:
    louder_audio = audio + 10  # Increase volume by 10dB
    louder_audio.export('louder_result.mp3', format='mp3')
    print("✅ Audio volume increased and saved as louder_result.mp3.")
except Exception as e:
    print(f"❌ An error occurred while adjusting audio volume: {e}")