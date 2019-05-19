import numpy as np
import wave
import sys
from os.path import join
from scipy.io import wavfile
from matplotlib import pyplot as plt
from numpy.fft import fft, ifft, fftfreq
import scipy

samplerate, data = wavfile.read(join("records", "input_record.wav"))
times = np.arange(len(data))/float(samplerate)
data = np.array(data.T[0])

plt.figure(0)
plt.plot(data)

fftdata = fft(data)
fftabs = abs(fftdata)
freqs = fftfreq(len(data), 1/samplerate)

plt.figure(1)
plt.plot(freqs, fftabs)

filterfreq_upper = 100000
filterfreq_lower = 1000
for i in range(len(fftdata)):
    tempabs = abs(fftdata[i])
    if tempabs >= filterfreq_upper:
        fftdata[i] = 0
    if tempabs <= filterfreq_lower:
        fftdata[i] = 0

ifftdata = ifft(fftdata).flatten()
wavfile.write(join('outputs', 'output.wav'), samplerate, ifftdata.astype(data.dtype))

fftabs = abs(fftdata)
plt.figure(2)
plt.plot(freqs, fftabs)

plt.show()
#this is a test sound for cse three thousand and fourty eight introudction to signal and systems and my sound is loud and clear
