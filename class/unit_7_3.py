# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


f1 = 2
f2 = 3

fs = 256
t = np.linspace(0, 4, fs*4)

x1 = np.sin(2*np.pi*t*f1);
x2 = np.sin(2*np.pi*t*f2);


# figure
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, x1)
plt.subplot(2, 1, 2)
plt.plot(t, x2)
plt.show()

y = x1+x2;
plt.figure()
plt.plot(t, y)
plt.show()

# FFT
x_fft = np.fft.fft(y)
x_mag = abs(x_fft)

plt.figure()
plt.plot(x_mag, linewidth=3)
plt.show()
