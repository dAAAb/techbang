# -*- coding: utf-8 -*-


import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt


def show_spectrogram(data, fs, save_name=None):
    '''Only accept mono channel'''
    
    plt.figure(figsize=(10, 6))
    plt.specgram(data, Fs=fs, cmap='jet', 
                 NFFT=int(fs*0.064),
                 noverlap=int(fs*0.032),
                 mode='magnitude')
    plt.xlabel('Time (sec)')
    plt.ylabel('Freq (Hz)')
    plt.title('Spectrogram')
    plt.colorbar()
    if save_name is not None:
        plt.savefig(f'spectrogram_{save_name}.png', dpi=150)
    plt.show()

def show_signal(data, fs, save_name=None):
    '''Only accept mono channel'''
    
    plt.figure(figsize=(10, 4))
    plt.plot(np.arange(len(data))/fs, data)
    plt.xlabel('Time (sec)')
    plt.ylabel('Amplitude')
    plt.title('Time domain')
    plt.ylim([-1, 1])
    if save_name is not None:
        plt.savefig(f'time_{save_name}.png', dpi=150)
    plt.show()



''' Demo 1 '''

audio_path = '../Unit 5/music.wav'
fs, data = wavfile.read(audio_path)
data = data/32768

show_signal(data, fs)
show_spectrogram(data, fs, 'test')

