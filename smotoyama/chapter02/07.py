import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randint

fs = 100
t = np.arange(fs)/fs
f = 1

signal = np.sin(2*np.pi*f*t)
noise = np.zeros(fs)
num_pulses = 5
for i in range(num_pulses):
    noise[np.random.randint((len(noise)))] = 2*np.round(np.random.rand())-1

noise = noise/np.sqrt(np.sum(noise**2))
noise = noise*np.sqrt(np.sum(signal**2))
noise = noise*10**(-snr/20)

x = signal + noise
y = np.zeros(len(x))

for i in range(M+1,len(y)-M+1):
    y[i] = np.median(x[i-M:i+M])


plt.subplot(3,1,1)
plt.plot(t,signal)
plt.title('signal')
plt.grid()
plt.ylim(-2,2)

plt.subplot(3,1,2)
plt.plot(t,x)
plt.title('signal+noise')
plt.grid()
plt.ylim(-2,2)

plt.subplot(3,1,3)
plt.plot(t,y)
plt.title('estimated')
plt.grid()
plt.ylim(-2,2)

plt.show()

#print('inputSNR[dB]:'+ str(10*np.log10(np.sum(signal**2)/np.sum(noise**2))))
#print('outputSNR[dB]:' + str(10*np.log10(np.sum(signal**2)/np.sum((y-signal)**2))))