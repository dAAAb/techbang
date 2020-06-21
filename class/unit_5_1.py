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

audio_path = '../audio/music2.wav'
fs, data = wavfile.read(audio_path)
data = data/32768

show_signal(data, fs)
show_spectrogram(data, fs)

# data_part = data[10000:26000]
# data_part = data[int(1.5*fs):int(2.5*fs)]

# show_signal(data_part, fs)
# show_spectrogram(data_part, fs)


''' Demo 2 '''


# audio_path = '../audio/tiger.wav'
# fs, data = wavfile.read(audio_path)
# data = data/32768

# data_left = data[:, 0]
# data_right = data[:, 1]

# show_spectrogram(data_left, fs, 'tiger_left')
# show_spectrogram(data_right, fs)
#
#show_signal(data_left, fs)
#show_signal(data_right, fs)

''' Demp 3 '''

# audio_path = '../audio/hello1.wav'
# fs, data = wavfile.read(audio_path)
# data = data/32768


# data_part = data[int(1.5*fs):int(2.5*fs)]
# show_signal(data_part, fs)


# data_louder = data_part*20
# show_signal(data_louder, fs)

# data_quiter = data_part*0.5
# show_signal(data_quiter, fs)

# wavfile.write('louder.wav', fs, data_louder)
# wavfile.write('quiter.wav', fs, data_quiter)

