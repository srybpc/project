# Add MOSQITO to the Python path
import sys
sys.path.append('..')

# Import numpy
import numpy as np

# Import plot function
import matplotlib.pyplot as plt

# Import load function
from mosqito.utils import load

# Import MOSQITO color sheme [Optional]
from mosqito import COLORS

# define the path to the wav file (to be replaced by your own path)
file_path = './samples/sound.wav'

# load signal
sig_wav, fs_wav = load(file_path, wav_calib=2 * 2 **0.5)

# plot signal
t_wav = np.linspace(0, (len(sig_wav) - 1) / fs_wav, len(sig_wav))
plt.figure(1)
plt.plot(t_wav, sig_wav, color=COLORS[0])
plt.xlabel('Time [s]')
plt.ylabel('Acoustic pressure [Pa]')
plt.show()