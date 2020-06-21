# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


import common as cm


def spectral_energy(ns, fs):

    def round_p(x):
        return int(x+0.5)
    
    # pre
    ns_length = ns.shape[0]
    frame_size = round_p(0.032*fs)
    NFFT = 2*frame_size
    han_win = np.hanning(frame_size+2)[1:-1]
    
    # filter band
    freq_per = (fs/2)/(NFFT/2)
    freq_min = 0
    freq_max = 300
    freq_min_idx = int(freq_min/freq_per)
    freq_max_idx = int(freq_max/freq_per)
    
    # main
    shift_pct = 0.5
    overlap = round_p((1-shift_pct)*frame_size)
    offset = frame_size - overlap
    max_m = int(np.floor((ns_length - NFFT)/offset)) + 1
    
    output = np.zeros(ns_length)
    
    for m in range(max_m):
        
        begin = m*offset
        finish = m*offset + frame_size  
        s_frame = ns[begin:finish]

        s_frame_win = s_frame*han_win
        
        # FFT
        s_fft = np.fft.fft(s_frame_win, NFFT)
        s_phase = np.angle(s_fft)
        s_mag = abs(s_fft)
        
        # Remove band
        s_mag[freq_min_idx:freq_max_idx] = 0
        tmp = -freq_min_idx if freq_min_idx != 0 else None
        s_mag[-freq_max_idx+1:tmp] = 0
        
        # IFFT
        s_new = s_mag*np.exp(s_phase*1j)
        output[begin:begin + NFFT] = output[begin:begin + NFFT] + (np.fft.ifft(s_new, NFFT)).real
        
    return output



# Read audio
audio_path = '../audio/bug.wav'
fs, data = cm.read_wav(audio_path)
cm.show_spectrogram(data, fs)


output = spectral_energy(data, fs)

cm.show_spectrogram(output, fs)
cm.write_wav('output.wav', output, fs)