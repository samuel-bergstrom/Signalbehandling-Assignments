# 1TE651 Signal Processing
# This file provides code for loading data for one patient
# The file assumes the DATASET folder is in the same folder with this file
import scipy.io
import numpy as np

patient_no = 2
s = str(patient_no)

# Load the .mat files
x_1_dict = scipy.io.loadmat(f'DATASET/ECG_{s}/ECG_{s}_V.mat')
x_2_dict = scipy.io.loadmat(f'DATASET/ECG_{s}/ECG_{s}_AVR.mat')
x_T_dict = scipy.io.loadmat(f'DATASET/ECG_{s}/ECG_{s}_II.mat')
x_missing_dict = scipy.io.loadmat(f'DATASET/ECG_{s}/ECG_{s}_II_missing.mat')

# Extract data
x_1 = np.array(x_1_dict[f'ECG_{s}_V'])
x_2 = np.array(x_2_dict[f'ECG_{s}_AVR'])
x_T = np.array(x_T_dict[f'ECG_{s}_II'])
x_missing = np.array(x_missing_dict[f'ECG_{s}_II_missing'])



