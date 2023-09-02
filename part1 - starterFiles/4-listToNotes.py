import numpy as np
from scipy.io.wavfile import write

freqs = np.array([220, 220, 440, 440, 330, 880, 770, 440, 440])

# Define constants
rate = 44100
timePerGlide = 2 # Each glissando will last this many seconds
noteLength = int(rate * timePerGlide)
vol = 0.5

# Create a list to which we append all the glissandos
y = np.zeros(1)

# Iterate through freqs to make the glissandos
for i in range(len(freqs) - 1):

    # Same logic as explored in 3-makeSlide.py
    start = freqs[i]
    end = freqs[i + 1]
    if end != start:
        end = (start + end)/2
    
    # Same logic as explored in 1-makeWav.py
    x = np.linspace(0, timePerGlide, noteLength)
    rowFreqs = np.linspace(start, end, noteLength)
    this_y = vol * np.sin(2 * np.pi * rowFreqs * x)

    # Append this wave to our overall wave
    y = np.append(y, this_y)


write("waves/5 - list of notes.wav", rate, y)