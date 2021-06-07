import numpy as np

fs = 8
#f = 0
print("fs={}".format(fs))
for f in range(fs):
  r = 0.5
  t = np.arange(fs).reshape(1, fs)/fs
  x = r*np.cos(2*np.pi*f*t)
  c = np.sum(x*np.exp(-1j*2*np.pi*f*t))/fs
  print("(f = {}) abs(c): {}".format(f, abs(c)))

fs=7
print("fs={}".format(fs))
for f in range(fs):
  r = 0.5
  t = np.arange(fs).reshape(1, fs)/fs
  x = r*np.cos(2*np.pi*f*t)
  c = np.sum(x*np.exp(-1j*2*np.pi*f*t))/fs
  print("(f = {}) abs(c): {}".format(f, abs(c)))