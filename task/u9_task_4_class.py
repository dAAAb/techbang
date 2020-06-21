import pyaudio
import datetime
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

''' Realtime recording '''

FS = 16000
DETECTION_SEC = 20

chunk = 512
p = pyaudio.PyAudio()
stream = p.open( format=pyaudio.paFloat32, channels=1, rate=FS, input=True, frames_per_buffer=chunk)
han_win = np.hanning(chunk+2)[1:-1]

print('Start')

samples = []
now = datetime.datetime.now()
for i in range(int(DETECTION_SEC*FS/chunk)):
    reading_samples = np.frombuffer(stream.read(chunk), dtype = np.float32).tolist()
    samples.extend(reading_samples)
    
    ''' Process Voice Avtivity Detection'''
    display_sec = 2
    
    # Write your code here
    #
    # [現在時間] 和 now 差距幾秒 ( 使用 .total_seconds() )
    #
    # 若差距大於 display_sec 秒，則做下面事情
    #
        # 將 samples 轉成 numpy 矩陣
        #
        # 取出最新的 2 秒鐘 (2*16000個取樣點)
        #
        # 將取出的訊號，執行 voice_activity_detection()，可得到 segments list
        #
        # 若 len(segments) > 0 以及 segments[0]起點大於0.3秒、終點小於 1.7秒，則做下面事情
        #
            # 因確認語音有活動且有效，可更新變數 now 至 [現在時間]
            #
            # 繪製時域波型
            #
            # 儲存音檔
            #

stream.stop_stream()
stream.close()
p.terminate()
print('End')