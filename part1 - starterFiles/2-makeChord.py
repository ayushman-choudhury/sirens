import numpy as np
from scipy.io.wavfile import write

# Define constants
rate = 44100
freq = 256
seconds = 3
vol = 0.5
x = np.linspace(0, seconds, seconds * rate)

# Create multiple notes, using interval ratios
root =  (1 * vol) * np.sin(2 * np.pi * freq * x)
third = (2 * vol) * np.sin(2 * np.pi * freq * 5/4 * x)
fifth = (3 * vol) * np.sin(2 * np.pi * freq * 3/2 * x)
top =   (4 * vol) * np.sin(2 * np.pi * freq * 2 * x)

# To stack notes, add their respective arrays
y = root + third + fifth + top
write("waves/2 - sine chord.wav", rate, y)