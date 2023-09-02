import numpy as np
from scipy.io.wavfile import write

# Define constants
rate = 44100    # The sampling rate of modern audio is 44,100 samples per second
freq = 440      # A = 440Hz is a standard tuning note
vol = 1         # Volumes between 1-10 tend to adjust the timbre. Beyond 10, the volume increases
seconds = 3     # This script will create a 3-second wav file
x = np.linspace(0, seconds, seconds * rate)   # Create a list of indices, from which to build the wave

# Create wave: formula = volume * sine(2pi * frequency * index)
wave = vol * np.sin(2 * np.pi * freq * x)
write('waves/1 - sine wave.wav', rate, wave)