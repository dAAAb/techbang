import pyaudio
import mouse
import numpy as np
import matplotlib.pyplot as plt

'''
遊戲頁面
https://flappybird.io/
'''

''' Realtime recording '''

FS = 16000
DETECTION_SEC = 120

chunk = 512
p = pyaudio.PyAudio()
stream = p.open( format=pyaudio.paFloat32, channels=1, rate=FS, input=True, frames_per_buffer=chunk)
han_win = np.hanning(chunk+2)[1:-1]


print('Start')
samples = []
for i in range(int(DETECTION_SEC*FS/chunk)):
    reading_samples = np.frombuffer(stream.read(chunk), dtype = np.float32).tolist()
    samples.extend(reading_samples)
    
    ''' Process STE and show its amplitude'''
    s_frame = np.asarray(reading_samples)
    # Write your code here
    # 
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # Write your code here
    
stream.stop_stream()
stream.close()
p.terminate()
print('End')
