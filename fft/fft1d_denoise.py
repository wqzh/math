import numpy as np
import matplotlib.pyplot as plt
from numpy import pi

plt.rcParams['figure.figsize'] = [16, 12]
plt.rcParams.update({'font.size': 18})

# sample from original signal
dt = 0.001                # fs = 1/dt
t = np.arange(0, 1, dt)   # 1 second, len(t) = fs
f = np.sin(2*pi*50*t) + np.sin(2*pi*120*t) # 50, 120
f_clean = f
f = f + 2.5*np.random.randn(len(t)) # Add noise

# fast fourier transform (FFT)
n = len(t)
fhat = np.fft.fft(f, n)
#psd = fhat * np.conj(fhat) / n    # power spectrum, |c|^2, normalization: div n
psd = np.abs(fhat)**2 / n
freq = (1/(dt*n)) * np.arange(n)  # frequency, x axis, 1/(dt*n) = 1
L = np.arange(1, np.floor(n/2), dtype=('int32'))

# filter low-psd signal(noise) and ifft
idx = psd > 70
psdclean = psd * idx
fhatclean = idx * fhat
fconst = np.fft.ifft(fhatclean)

# clean & noisy signal
fig, axs = plt.subplots(4, 1)
plt.figure(dpi=400)
plt.sca(axs[0])
plt.plot(t, f, color='c', lw=1.5, label='Noisy')
plt.plot(t, f_clean, color='b', lw=2, label='Clean')
plt.xlabel('second');
plt.xlim(t[0], t[-1])
plt.ylim(-10, 10)
plt.legend()

# original noisy power spectrum(all)
plt.sca(axs[1])
plt.plot(freq, psd, color='b', lw=1.5, label='all-noisy')
plt.xlabel('Hz'); plt.ylabel('power'); 
plt.legend()

# reconstructed signal: fft -> filter -> ifft
plt.sca(axs[2])
plt.plot(t, fconst, color='g', lw=1.5, label='reconstruct')
plt.xlabel('second');
plt.xlim(t[0], t[-1])
plt.ylim(-10, 10)
plt.legend()

# original noisy/reconstructed signal power spectrum(half)
plt.sca(axs[3])
plt.plot(freq[L], psd[L], color='b', lw=2, label='half-noisy')
plt.plot(freq[L], psdclean[L], color='g', lw=2, label='half-reconstruct')
plt.xlabel('Hz'); plt.ylabel('power'); 
plt.legend()

#plt.savefig('./fft1_denoise.pdf')
plt.show()