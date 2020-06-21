# -*- coding: utf-8 -*-

import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt


def short_time(ns, fs):

    def round_p(x):
        return int(x+0.5)
    
    # pre
    ns_length = ns.shape[0]
    frame_size = round_p(0.032*fs)
    han_win = np.hanning(frame_size+2)[1:-1]
    
    plt.plot(han_win)
    plt.show()
    
    # main
    shift_pct = 0.5
    overlap = round_p((1-shift_pct)*frame_size)
    offset = frame_size - overlap
    max_m = int(np.floor((ns_length - frame_size)/offset)) + 1
    output = np.zeros(ns_length)
    
    for m in range(max_m):
        
        begin = m*offset
        finish = m*offset + frame_size  
        s_frame = ns[begin:finish]

        s_frame_win = s_frame*han_win
        
        # do something here
        #
        # 
        
        plt.plot(s_frame)
        plt.ylim([min(s_frame), max(s_frame)])
        plt.show()
        
        plt.plot(s_frame_win)
        plt.ylim([min(s_frame), max(s_frame)])
        plt.show()
        
        output[begin:finish] = output[begin:finish] + s_frame_win

    return output


# Read audio
audio_path = '../audio/jarvus.wav'
fs, data = wavfile.read(audio_path)
data = data/32768

# Original
plt.plot(np.arange(len(data))/fs, data)
plt.title('Original speech')
plt.show()

# After framing and windowing
output = short_time(data, fs)
plt.plot(np.arange(len(output))/fs, output)
plt.title('After framing and windowing')
plt.show()
