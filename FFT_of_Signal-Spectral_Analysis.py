

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft


"""
How to do Spectral analysis or FFT of Signal in Python?

1. number of cycles per second = (sampling frequency) / (signal frequency)

2. The sampling frequency (or, sampling rate) is the average number of samples
obtained in one second (samples per second), and fs = 1 / T (fs = sampling
frequency).


Refer-
https://www.youtube.com/watch?v=UjUKaQKniLM
https://pythonnumericalmethods.berkeley.edu/notebooks/chapter24.01-The-Basics-of-waves.html
https://mulloverthing.com/how-do-you-calculate-samples-per-cycle/
https://www.youtube.com/watch?v=BXi4_bK7zTQ
https://www.electronics-notes.com/articles/basic_concepts/electronic-electrical-waveforms/sine-waveform.php

https://www.testandmeasurementtips.com/basics-sine-waves/
https://betterexplained.com/articles/intuitive-understanding-of-sine-waves/
"""

# Generate (the spectrum of) a sine wave signal:

# Define sampling frequency (when dealing with signals, sampling
# frequency plays a critical role)-
sampling_freq = 1000
# 1000 Hz

print(f"With a sampling frequency = {sampling_freq} Hz, you sample a given signal every {1 / sampling_freq} second")
# With a sampling frequency = 1000 Hz, you sample a given signal every 0.001 second

print(f"With a sampling frequency = {sampling_freq} Hz, signal time period = {1 / sampling_freq} second")
# With a sampling frequency = 1000 Hz, signal time period = 0.001 second

# We then create a time axis/variable-
t = np.arange(0, 1, 1 / sampling_freq)
# We are generating a signal with a duration of 1 second. And the
# period between two time samples is (1 / sampling_freq)

t.shape
# (1000,)

t.min(), t.max()
# (0.0, 0.999)

# Say we create a signal frequency of 20 Hz-
signal_freq = 20

# Create/generate a signal-
x = np.sin(2 * np.pi * signal_freq * t)


# Visualize the created sine wave-
plt.plot(t, x)
plt.title("sine wave: 20 Hz signal of 1 minute duration")
plt.xlabel("time (seconds)")
plt.ylabel("amplitude")
plt.show()

# There are 20 sine waves in the given time duration of 1 minute.


# Compute FFT (or, spectrum)-
x_fft = fft(x)
# This will be a double sided spectrum.
# 'x_fft' is a complex quantity having both magnitude and phase. Here, we
# only focus on the magnitude spectrum and so, we take its absolute value.

plt.plot(t, np.abs(x_fft))
plt.title("sine wave: FFT - 20 Hz signal of 1 minute duration")
plt.xlabel("time (seconds)")
plt.ylabel("magnitude spectrum")
plt.show()

# We get two spikes because it's going from 0 to 2*pi. It is repeating 10
# intervals of pi. Basic concepts of DSP.

# We only want to plot half of this magnitude spectrum because all of the spectrum
# information is contained upto half of it. And for this, we need to generate the
# frequency axis.

# To compute the frequency axis, first compute the number of elements in the time.
# This helps in creating an exact frequency axis-
n = t.size

n
# 1000

# Create frequency axis-
freq = np.linspace(0, 1, int(n / 2)) * (sampling_freq / 2)
# We use (n / 2) because our sampling frequency = 1000 Hz, and this frequency axis
# should go upto half of the sampling frequency.
# Our frequency axis will go from 0 Hz to 500 Hz according to the sampling theorem.
# We are making it 500 with (sampling_freq / 2) and then we are generating an equal
# spaced samples with 'np.linspace()' between 0 to 1 with a interval of (n / 2).

freq.shape
# (500,)

# 'x_fft' contains double sided spectrum and (for now) we are interested only in half
# of it. We want to extract the magnitude of the FFt-
x_m = np.abs(x_fft[0: int(n / 2)])

# Extract half of it-
plt.plot(freq, x_m)
plt.title("sine wave: FFT - 20 Hz signal of 1 minute duration")
plt.xlabel("frequency")
plt.ylabel("magnitude power spectrum")
plt.show()
# We are getting only one spike, approximately around 20 Hz. Its magnitude is going upto
# 500, while our signal amplitude was only 1.

# To demonstrate the magnitude spectrum more appropriately, we need to normalize the
# magnitude spectrum, which can be done simply with (2 / length of sequence) = (2 / n)-
x_m = (2 / n) * np.abs(x_fft[0: int(n / 2)])

# Extract half of it-
plt.plot(freq, x_m)
plt.title("Magnitude Power Spectrum")
plt.xlabel("frequency (Hz)")
plt.ylabel("magnitude")
plt.show()
# And now, we can see that maximum amplitude is 1 which is represented by a signal having
# a frequency of 20 Hz (original plot above).




# We verify these concepts by taking more Example having one frequency component:
sampling_freq = 100
# A sampling frequency of 100 Hz is sufficient as we are plotting a 20 Hz signal.

t = np.arange(0, 1, 1 / sampling_freq)

t.shape
# (100,)

# Create/generate a signal-
x = np.sin(2 * np.pi * signal_freq * t)

# Visualize the created sine wave-
plt.plot(t, x)
plt.title("sine wave: 20 Hz signal of 1 minute duration")
plt.xlabel("time (seconds)")
plt.ylabel("amplitude")
plt.show()

x_fft = fft(x)
# This will be a double sided spectrum.
# 'x_fft' is a complex quantity having both magnitude and phase. Here, we
# only focus on the magnitude spectrum and so, we take its absolute value.

plt.plot(t, np.abs(x_fft))
plt.title("sine wave: FFT - 20 Hz signal of 1 minute duration")
plt.xlabel("time (seconds)")
plt.ylabel("magnitude spectrum")
plt.show()

n = t.size

n
# 100

# Create frequency axis-
freq = np.linspace(0, 1, int(n / 2)) * (sampling_freq / 2)

freq.shape
# (50,)

x_m = (2 / n) * np.abs(x_fft[0: int(n / 2)])

# Extract half of it-
plt.plot(freq, x_m)
plt.title("Magnitude Power Spectrum")
plt.xlabel("frequency (Hz)")
plt.ylabel("magnitude")
plt.show()
# We have a maximum amplitude is 1 which is represented by a signal having a 20 Hz signal.




# Final example:

# Sampling frequency of 300 Hz-
sampling_freq = 300

t = np.arange(0, 1, 1 / sampling_freq)

t.shape
# (300,)

# Create/generate a signal-
x = np.sin(2 * np.pi * signal_freq * t) + (0.5 * np.sin(2 * np.pi * 40 * t)) + \
(1.5 * np.sin(2 * np.pi * 5 * t))

# Visualize the compunded signal consisting of 3 sine waves-
plt.plot(t, x)
plt.title("3 sine waves: 5, 20 & 40 Hz signals of 1 minute duration (time domain)")
plt.xlabel("time (seconds)")
plt.ylabel("amplitude")
plt.show()

# Compute FFT-
x_fft = fft(x)
# This will be a double sided spectrum.
# 'x_fft' is a complex quantity having both magnitude and phase. Here, we
# only focus on the magnitude spectrum and so, we take its absolute value.

plt.plot(t, np.abs(x_fft))
plt.title("FFT of compound signal")
plt.xlabel("time (seconds)")
plt.ylabel("magnitude spectrum")
plt.show()

n = t.size

n
# 300

# Create frequency axis-
freq = np.linspace(0, 1, int(n / 2)) * (sampling_freq / 2)

freq.shape
# (150,)

x_m = (2 / n) * np.abs(x_fft[0: int(n / 2)])

# Extract half of it-
plt.plot(freq, x_m)
plt.title("Magnitude Power Spectrum")
plt.xlabel("frequency (Hz)")
plt.ylabel("magnitude")
plt.show()
# We see the corresponding 3 components occurring in our input signal denoted
# by the 3 peaks at 5, 20 and 40 Hz. The 5 Hz signal has an amplitude = 1.5,
# the 20 Hz signal has an amplitude of 1.0, and the 40 Hz signal has an
# amplitude of 0.5.
# Interpret different frequency component(s) from the magnitude spectrum.

