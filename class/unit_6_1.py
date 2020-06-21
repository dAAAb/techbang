# -*- coding: utf-8 -*-

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(0, 1, 100, endpoint=False)
y = signal.square(2*np.pi*9*t)

plt.figure(figsize=(10, 4))
plt.plot(y, linewidth=4)
plt.ylim(-2, 2)
plt.xlabel('samples')
plt.ylabel('amp')
plt.show()


han_win = np.hanning(20)
plt.figure(figsize=(4, 4))
plt.plot(han_win)
plt.ylim(0, 1)
plt.ylabel('weighting')
plt.show()

new = np.zeros(100)

for m in range(9):
    begin = m*10
    finish = begin + 20  
    print(begin, finish)
    
    s_frame = y[begin:finish]
    s_hann = s_frame*han_win
    new[begin:finish] = new[begin:finish] + s_hann
    
    # plt.figure(figsize=(2, 4))
    # plt.plot(s_frame, '--', linewidth=2)
    # plt.plot(s_hann, linewidth=4)
    # plt.ylim(-2, 2)
    # plt.ylabel('amp')
    # plt.show()

plt.figure(figsize=(10, 4))
plt.plot(y, '--', linewidth=2)
plt.plot(new, linewidth=4)
plt.ylim(-2, 2)
plt.xlabel('samples')
plt.ylabel('amp')
plt.show()