# -*- coding: utf-8 -*-

import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

import common as cm


def zero_cross_rate(ns, fs):

    def round_p(x):
        return int(x+0.5)
    
    def sign(x):
        if x < 0:
            return -1
        elif x == 0:
            return 0
        elif x > 0:
            return 1
    
    # pre
    ns_length = ns.shape[0]
    frame_size = round_p(0.032*fs)
    NFFT = 2*frame_size
    han_win = np.hanning(frame_size+2)[1:-1]
    
    # main
    shift_pct = 0.5
    overlap = round_p((1-shift_pct)*frame_size)
    offset = frame_size - overlap
    max_m = int(np.floor((ns_length - NFFT)/offset)) + 1
    
    frame_time = np.zeros(max_m)
    output = np.zeros(max_m)
    
    for m in range(max_m):
        
        begin = m*offset
        finish = m*offset + frame_size  
        s_frame = ns[begin:finish]

        s_frame_win = s_frame*han_win
        
        '''
        Method 1
        '''
        zcr = 0
        for i in range(2, frame_size):
            zcr = zcr + 0.5*abs(sign(s_frame_win[i])-sign(s_frame_win[i-1]))
        '''
        Method 2
        '''
        zcr2 = 0
        # do something here
        #
        # do something above
        
        # print(zcr, zcr2)
        
        output[m] = zcr
        frame_time[m] = ((begin+finish)/2)/fs

    return output, frame_time


# Read audio
audio_path = '../audio/jarvus.wav'
fs, data = cm.read_wav(audio_path)

# Main
zcr, frame_time = zero_cross_rate(data, fs)
zcr_nor = (zcr/max(zcr))*max(data)*0.2

ste, frame_time = cm.short_time_energy(data, fs)
ste_nor = (ste/max(ste))*max(data)

plt.figure(figsize=(10, 4))
plt.plot(np.arange(len(data))/fs, data, label='signal')
plt.plot(frame_time, zcr_nor, linewidth=3, label='ZCR')
plt.plot(frame_time, ste_nor, linewidth=3, label='STE', color='r')
plt.legend()
plt.show()

cm.show_spectrogram(data, fs)

