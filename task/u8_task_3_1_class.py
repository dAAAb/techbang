import pyaudio
import numpy as np
import matplotlib.pyplot as plt


def play_raw(speech, fs):
    ''' Play audio raw data '''

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)
    stream.write(np.asarray(speech).astype(np.float32).tostring())
    stream.stop_stream()
    stream.close()
    p.terminate()



''' Realtime recording '''

FS = 16000
DETECTION_SEC = 3

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

plt.plot(samples)
plt.show()

play_raw(samples, FS)
