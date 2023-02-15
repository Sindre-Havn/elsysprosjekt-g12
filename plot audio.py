from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np
import wave
# https://www.tutorialspoint.com/read-and-write-wav-files-using-python-wave
# https://stackoverflow.com/questions/2060628/reading-wav-files-in-python
import struct

# https://doc.sagemath.org/html/en/reference/misc/sage/media/wav.html
# https://audioaudit.io/articles/podcast/sample-width



import os

cwd = os.getcwd()  # Get the current working directory (cwd)
os.chdir('C:\\Users\\Sindre\\Documents\\Elsys\\4 semester\\Elektronisk systemdesign prosjekt TTT4270\\kode')
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

vocals = read('Viva la Vida Vocals Mono.wav', 'rb')[1]
instrumental = read("Viva la Vida Instrumental Mono.wav")[1]
plt.plot(vocals[:1000_000])
plt.plot(instrumental[:1000_000])
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.show()

obj = wave.open('Viva La Vida 2zip.wav','w')
obj.setnchannels(1) # mono
obj.setsampwidth(2)
obj.setframerate(44100.0)

shortest = vocals if len(vocals) < len(instrumental) else instrumental
longest = vocals if len(vocals) > len(instrumental) else instrumental

merged = zip(vocals, instrumental)



for i in range(idx, len(longest)):
   value = longest[i]
   data = struct.pack('<h', value)
   obj.writeframesraw( data )

obj.close()