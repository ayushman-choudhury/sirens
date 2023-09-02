import numpy as np
from scipy.io.wavfile import write

#Define constants
rate = 44100
seconds = 3
vol = 2
x = np.linspace(0, seconds, seconds * rate)
start = 440 #220Hz corresponds to A3, at the top of the bass clef
end = 220 #440Hz corresponds to A4, in the middle of the treble clef

# When changing between frequencies, we have to account for phase shifting.
if end > start:
    # When sliding up, start at the right pitch, but increase at HALF the speed
    newEnd = start + (end - start) / 2
    type = "upward"

if end < start:
    #When sliding down, start at the right pitch, but decrease at HALF the speed
    newEnd = start - (start - end) / 2
    type = "downward"

# These are actually the same formula: start / 2 + end / 2
newEnd = (start + end)/2

# Write the wave in the same way: volume * sine(2pi * frequency * index)
freq = np.linspace(start, newEnd, seconds * rate)
y = vol * np.sin(2 * np.pi * freq * x)
write(f'waves/4 - {type} slide.wav', rate, y)