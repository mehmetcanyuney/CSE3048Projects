import numpy as np
import wave
import sys
from os.path import join
from scipy.io import wavfile
from matplotlib import pyplot as plt
from numpy.fft import fft, ifft, fftfreq, fftshift
from matplotlib.widgets import Slider
import scipy

samplerate, data = wavfile.read("allthree.wav")
times = np.arange(len(data))/float(samplerate)

fftdata = fft(data)
fftabs = abs(fftdata)
freqs = fftfreq(len(data), 1/samplerate)

plt.figure(1)
plt.plot(freqs, fftabs)

plt.figure(2)
plt.plot(fftabs)

# 1. sound
fftdata1 = fft(data)
filter_size = 160000
for i in range(filter_size + 1):
    fftdata1[176400 + i] = 0
    fftdata1[176400 - i] = 0

fftabs1 = abs(fftdata1)
plt.figure(3)
plt.plot(freqs, fftabs1)

ifftdata1 = ifft(fftdata1).flatten()
wavfile.write(join('outputs', 'output1.wav'), samplerate, ifftdata1.astype(data.dtype))

# 2.sound
fftdata2 = fft(data)
for i in range(len(fftdata2)):
    if (i >= 32800 and i <= 92800) or (i >= 260000 and i <= 320000):
        continue
    fftdata2[i] = 0

fftabs2 = abs(fftdata2)
plt.figure(4)
plt.plot(freqs, fftabs2)

ifftdata2 = ifft(fftdata2)
modulator2 = np.sin(2.0 * np.pi * 9140630 * times)
# modulator2 = np.sin(2.0 * np.pi * 7000 * times)
res2 = []
for i in range(len(ifftdata2)):
    res2.append(ifftdata2[i] * modulator2[i])
retfftdata2 = fft(res2)

retfftabs2 = abs(retfftdata2)
fig = plt.figure(5)
a_plot, = plt.plot(freqs, retfftabs2)

filter_size = 160000
for i in range(filter_size + 1):
    retfftdata2[176400 + i] = 0
    retfftdata2[176400 - i] = 0

ifftdata2 = ifft(retfftdata2).flatten()
wavfile.write(join('outputs', 'output2.wav'), samplerate, ifftdata2.astype(data.dtype))


# 3.sound
fftdata3 = fft(data)
for i in range(len(fftdata3)):
    if (i >= 93800 and i <= 151800) or (i >= 201000 and i <= 259000):
        continue
    fftdata3[i] = 0

fftabs3 = abs(fftdata3)
plt.figure(6)
plt.plot(freqs, fftabs3)

ifftdata3 = ifft(fftdata3)
modulator3 = np.sin(2.0 * np.pi * 64070 * times)
# modulator3 = np.sin(2.0 * np.pi * 7000 * times)
res3 = []
for i in range(len(ifftdata3)):
    res3.append(ifftdata3[i] * modulator3[i])
retfftdata3 = fft(res3)

retfftabs3 = abs(retfftdata3)
fig = plt.figure(7)
a_plot, = plt.plot(freqs, retfftabs3)

# slider_ax = plt.axes([0.1, 0.2, 0.4, 0.3])
# a_slider = Slider(slider_ax,      # the axes object containing the slider
#                   'a',            # the name of the slider parameter
#                   10,          # minimal value of the parameter
#                   400000 ,          # maximal value of the parameter
#                   valinit=100  # initial value of the parameter
#                  )
#
# def update(a):
#     ifftdata3 = ifft(fftdata3)
#     modulator3 = np.sin(2.0 * np.pi * a * times)
#     res3 = []
#     for i in range(len(ifftdata3)):
#         res3.append(ifftdata3[i] * modulator3[i])
#     retfftdata3 = fft(res3)
#
#     retfftabs3 = abs(retfftdata3)
#
#     a_plot.set_ydata(retfftabs3)
#     fig.canvas.draw_idle()
#
# a_slider.on_changed(update)

filter_size = 160000
for i in range(filter_size + 1):
    retfftdata3[176400 + i] = 0
    retfftdata3[176400 - i] = 0

ifftdata3 = ifft(retfftdata3).flatten()
wavfile.write(join('outputs', 'output3.wav'), samplerate, ifftdata3.astype(data.dtype))



plt.show()
