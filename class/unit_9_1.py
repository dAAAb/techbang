# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.measurements import label
from scipy.ndimage import find_objects

import common as cm


# Parameters
TH_is_active = 100
TH_connect_max = 15
TH_keep_min = 6
buffer_num = 5

# VAD Step 1
fs, data = cm.read_wav('../audio/jarvus2.wav')
cm.show_signal(data, fs)
cm.show_spectrogram(data, fs)
#cm.play_raw(data, fs)


# VAD Step 2 ~ 3
SE, frame_time = cm.spectral_energy(data, fs, 300, 4000)

plt.figure(figsize=(10, 3))
plt.plot(frame_time, SE)
plt.title('After Step 3')
plt.show()

# VAD Step 4
VAD_step_4 = np.zeros(len(SE))
for frame_idx in range(len(SE)):
#    print(frame_time[frame_idx], SE[frame_idx])
    if SE[frame_idx] >= TH_is_active:
        VAD_step_4[frame_idx] = 1
    else:
        VAD_step_4[frame_idx] = 0

plt.figure(figsize=(10, 3))
plt.plot(frame_time, VAD_step_4)
plt.title('After Step 4')
plt.show()

# VAD Step 5
VAD_step_5 = np.array(VAD_step_4)
labeled, ncomponents = label(VAD_step_4, np.ones((3), dtype=np.int))
segments = find_objects(labeled)

for i in range(len(segments)-1):
    
    idx_from = segments[i][0].stop
    idx_to = segments[i+1][0].start
#    print(idx_from, idx_to)
    if idx_to-idx_from <= TH_connect_max:
        VAD_step_5[idx_from:idx_to] = 1

plt.figure(figsize=(10, 3))
plt.plot(frame_time, VAD_step_5)
plt.title('After Step 5')
plt.show()

# VAD Step 6
VAD_step_6 = np.array(VAD_step_5)
labeled, ncomponents = label(VAD_step_6, np.ones((3), dtype=np.int))
segments = find_objects(labeled)

VAD = []
for i in range(len(segments)):
    
    idx_from = segments[i][0].start
    idx_to = segments[i][0].stop
#    print(idx_from, idx_to)
    if idx_to-idx_from+1 >= TH_keep_min:
        VAD.append([idx_from, idx_to])
    else:
        VAD_step_6[idx_from:idx_to] = 0
        
print(VAD)
plt.figure(figsize=(10, 3))
plt.plot(np.arange(len(data))/fs, data)
plt.plot(frame_time, VAD_step_6*max(data), linewidth=3)
plt.title('After Step 6')
plt.show()

# VAD Step 7
VAD_step_7 = np.zeros(len(VAD_step_6))
for i in VAD:
    i[0] = max(0, i[0]-buffer_num)
    i[1] = min(len(VAD_step_7), i[1]+buffer_num)
    VAD_step_7[i[0]:i[1]] = 1
    
print(VAD)
plt.figure(figsize=(10, 3))
plt.plot(np.arange(len(data))/fs, data)
plt.plot(frame_time, VAD_step_7*max(data), linewidth=3)
plt.title('After Step 7, Done VAD')
plt.show()

for i in VAD:
    print(frame_time[i[0]], frame_time[i[1]])