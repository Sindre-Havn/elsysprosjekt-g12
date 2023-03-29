import sounddevice as sd
import numpy as np
import wave

# Open the .wav file
wav_file = "path/to/your/wav_file.wav"
with wave.open(wav_file, 'rb') as wav_obj:
    sample_rate = wav_obj.getframerate()
    channels = wav_obj.getnchannels()
    width = wav_obj.getsampwidth()
    num_samples = wav_obj.getnframes()
    audio_data = wav_obj.readframes(num_samples)
    audio_samples = np.frombuffer(audio_data, dtype=np.int16)

# Play the audio using the I2S interface
sd.play(audio_samples, samplerate=sample_rate, channels=channels, blocking=True)
