# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.measurements import label
from scipy.ndimage import find_objects

import common as cm

def voice_activity_detection(data, fs, show_img=False):
    '''
    Unit 9
    '''

    # Parameters
    freq_min = 300
    freq_max = 4000

    TH_is_active = 100
    TH_connect_max = 15
    TH_keep_min = 6
    buffer_num = 5
    
    # VAD Step 2 ~ 3
    SE, frame_time = cm.spectral_energy(data, fs, freq_min, freq_max)

    # VAD Step 4
    VAD = np.zeros(len(SE))
    for frame_idx in range(len(SE)):
        if SE[frame_idx] >= TH_is_active:
            VAD[frame_idx] = 1
        else:
            VAD[frame_idx] = 0

    # VAD Step 5
    labeled, ncomponents = label(VAD, np.ones((3), dtype=np.int))
    segments = find_objects(labeled)
    
    for i in range(len(segments)-1):
        idx_from = segments[i][0].stop
        idx_to = segments[i+1][0].start
        if idx_to-idx_from <= TH_connect_max:
            VAD[idx_from:idx_to] = 1
            
    # VAD Step 6
    labeled, ncomponents = label(VAD, np.ones((3), dtype=np.int))
    segments = find_objects(labeled)
    
    VAD_points = []
    for i in range(len(segments)):
        idx_from = segments[i][0].start
        idx_to = segments[i][0].stop
        if idx_to-idx_from+1 >= TH_keep_min:
            VAD_points.append([idx_from, idx_to])
        else:
            VAD[idx_from:idx_to] = 0
    
    # VAD Step 7
    for i in VAD_points:
        i[0] = max(0, i[0]-buffer_num)
        i[1] = min(len(VAD)-1, i[1]+buffer_num)
        VAD[i[0]:i[1]] = 1
    
    segments = []
    
    for i in VAD_points:
            
        segment = {}
        segment['frame_from'] = i[0]
        segment['frame_to'] = i[1]
        segment['sec_from'] = frame_time[i[0]]
        segment['sec_to'] = frame_time[i[1]]
        segment['samples'] = data[int(segment['sec_from']*fs):int(segment['sec_to']*fs)]
        
        segments.append(segment)
        
    if show_img:
        
        plt.figure(figsize=(10, 4))
        plt.plot(frame_time, SE)
        plt.title('Spectral Energy')
        plt.xlabel('Time (sec)')
        plt.ylabel('Energy')
        plt.show()
        
        plt.figure(figsize=(10, 4))
        plt.plot(np.arange(len(data))/fs, data)
        plt.plot(frame_time, VAD*max(data), linewidth=3)
        plt.title('VAD')
        plt.xlabel('Time (sec)')
        plt.ylabel('Amplitude')
        plt.show()
    
    return segments


# Read audio
fs, data = cm.read_wav('../audio/jarvus2.wav')

# Run VAD
segments = voice_activity_detection(data, fs, show_img=True)

# Show segments
for segment in segments:
    
    samples = segment['samples']
    
    plt.figure(figsize=(10, 3))
    plt.plot(np.arange(len(samples))/fs, samples)
    title = f"from {segment['sec_from']} to {segment['sec_to']} sec"
    plt.title(title)
    plt.xlabel('Time (sec)')
    plt.ylabel('Amplitude')
    plt.show()
    
    cm.write_wav(f'{title}.wav', samples, fs)