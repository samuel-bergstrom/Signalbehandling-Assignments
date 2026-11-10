#####################
# 1TE651 Signal Processing 
# Assignment: Active Noise Cancellation with LMS 
# This script is used to cancel noise from a noisy music signal using the normalized LMS algorithm. See the assingment description for more details.
##################
# STODO indicates the parts of the code that the students need to complete.
##################
#  NOTE: We implemented two options for loading/recording of audio files. One uses the soundfile library, while the other uses the torchaudio library. You can choose the desired option by setting the audio_library variable to 'lib_sd' or 'lib_torch'. There is no difference in the output between the two options. We have provided the code for both options to ensure that the code runs on different platforms. (Soundfile seems to have problems on some macos machines.)
###################


import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sc
audio_library = 'lib_sd'  # 'lib_sd' or 'lib_torch'
if audio_library == 'lib_sd':
    import soundfile as sf
elif audio_library == 'lib_torch':
    import torchaudio
    import torch


# Choose noise scenario, possible values: 1,2,3,4 
mynoiseScenario=2

# Create file path assuming DATASETA is a subfolder of your current  directory
noisefile = f'./DATASETA/N{mynoiseScenario}.wav' 
signalfile = f'./DATASETA/vocalN{mynoiseScenario}.wav'

# Read noise recording
# w: sampled noise, Fs: sampling rate (same both w and xw),
if audio_library == 'lib_sd':
   w, Fs = sf.read(noisefile)    
elif audio_library == 'lib_torch':
  wt, Fs =torchaudio.load(noisefile)
  w=wt.detach().numpy()
w=w.reshape(-1, 1)

# Read signal (music+noise) recording
# xw: sampled music+noise
if audio_library == 'lib_sd':
   xw, _ = sf.read(signalfile)    
elif audio_library == 'lib_torch':
  xwt, _ = torchaudio.load(signalfile) 
  xw=xwt.detach().numpy()
xw=xw.reshape(-1, 1)


# STODO:Processing of the signals, to be completed by the course participants


# .......
# .......


#############################################
##################


# --------------------------------------
# At this point,  recx should hold the reconstructed/cleaned signal.
# Make sure to normalize recx with its maximum absolute value before saving it.
# It will be useful to think why this normalization is necessary.
# --------------------------------------
# Save the cleaned signal
recfile = f'recvocalN{mynoiseScenario}.wav'
if audio_library == 'lib_sd':
   sf.write(recfile,recx,Fs)
elif audio_library == 'lib_torch':
  recxt=torch.from_numpy(recx)
  recxtt=torch.reshape(recxt, (1,-1))
  torchaudio.save(recfile, recxtt, Fs)


#-------------------------------------
# STODO: Now plot the power spectra of the associated signals 
# Following can be useful for this purpose: scipy.signal.welch, scipy.fft, scipy.signal.periodogram
# For readability,  while plotting the power spectrum, use decibels in the y-axis.
# For instance, instead of plotting  P, plot 10 *log10 (P). 
#---------------------------------------  
# 
#



#-------------------------------
########################