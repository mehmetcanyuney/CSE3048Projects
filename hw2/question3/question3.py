import numpy as np
import wave
import sys
from os.path import join
from scipy.io import wavfile
from matplotlib import pyplot as plt
from numpy.fft import fft, ifft, fftfreq, fftshift
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

filter_size = 205000
for i in range(filter_size + 1):
    fftdata[220500 + i] = 0
    fftdata[220500 - i] = 0


ifftdata = ifft(fftdata).flatten()
wavfile.write(join('outputs', 'output.wav'), samplerate, ifftdata.astype(data.dtype))

fftabs = abs(fftdata)
plt.figure(2)
plt.plot(freqs, fftabs)

plt.show()

# Even though we trim the frequency we can still hear the voice
# because high and low frequency are most likely either the voices
# that we are not able to hear or the voices that we call as noices
# so after trim operation, that is why we can still the message that
# is in the given wav file. However the low and high filter frequncies
# depends on the signal, also depends on the voice level and gender.
# However voice became more and more flat as we delete the data
# because we're losing information although we can still hear what
# is being said in the record.

# if we set filter_size to 21800 voice is still hearable but not understandable
# if we set filter_size to 21700 voice is hearable and understanable for a bit
# if we set filter size to 21200 voice is both hearable and understanable
# last 3 digit of filter_size is most likely to effect the voice's flatness

# Wav file contains following text :
# this is a test sound for cse three thousand and fourty eight introudction to signal and systems and my sound is loud and clear
