from numpy import *
import matplotlib
import matplotlib.pyplot as plt
import time
from scipy import signal, misc
from scipy.linalg import svd
import scipy
from scipy.ndimage.filters import gaussian_filter
from scipy.ndimage import gaussian_filter1d
from scipy.io.wavfile import write
from scipy import signal

import colorsys
import soundfile as sf
import h5py
import array
from pydub import AudioSegment
from pydub.utils import get_array_type
import wave

import numpy as np
import os

def load_data(path):
    sound = AudioSegment.from_file(file=path)
    fs = sound.frame_rate
    left = sound.split_to_mono()[1]
    bit_depth = left.sample_width * 8
    array_type = get_array_type(bit_depth)
    num_a = array.array(array_type, left._data)
    path = os.path.join(os.getcwd(), "../onset_offset", "XC155388-Pink_Pigeon-Nesoenas_mayeri.txt")
    labels = loadtxt(path)
    return (fs,num_a,sound,labels)
def process_data(path):
    fs,num_a,sound,labels = load_data(path)
    segments = []
    for ind,lab in enumerate(labels):
        onset = int(lab[0]*fs)
        offset = int(lab[1]*fs)
        segment = num_a[onset:offset]
        segments.append(segment)
        write("../wav/segment_%s.wav" %ind, fs, int16(segment))
        #print ("finish generating segment %s is from %s s (%s) to %s (%s)s" %(ind, lab[0], onset,lab[1], offset) )
    return segments

#!/usr/bin/env python
# coding: utf-8

# Apply Kestrel Segmentation, Features and Training via PyAudioAnalysis

import matplotlib.pyplot as plt
import sound_segmentation
PSeg = sound_segmentation 

import sounddevice as sd
from pyAudioAnalysis import audioTrainTest as aT
import pyAudioAnalysis
from pyAudioAnalysis import ShortTermFeatures, MidTermFeatures
from pyAudioAnalysis import audioBasicIO as aIO
from pyAudioAnalysis import audioSegmentation as aS
from scipy.io.wavfile import write

from pydub.utils import get_array_type
import array
from numpy import int16

import os
import numpy as np
import pandas as pd


example_path = os.path.join(os.getcwd(), "../../", "inputs/mp3/mauritius_kestrel.mp3")


def silence_removal(path,write=False,short_features=False,medium_features=False,auto_train=False):
	(fs,num_a,sound,_) = PSeg.load_data(path)
	left = sound.split_to_mono()[0]
	bit_depth = left.sample_width * 8
	array_type = get_array_type(bit_depth)
	num_a = array.array(array_type, left._data)
	recording_duration = len(num_a)/fs
	segments = aS.silence_removal(np.array(num_a), fs, 0.020, 0.020, smooth_window = 1.0, weight = 0.3, plot = False)
	sampling_rate = 1.0/fs
	signal = np.array(num_a)
	time_x = np.arange(0, signal.shape[0] / float(sampling_rate), 1.0 /
		               sampling_rate)


	sound_segs_th = []
	silence_segs = []
	for ind,seg in enumerate(segments):
		onset = int(seg[0]*fs)
		offset = int(seg[1]*fs)
		wave_sound = np.array(num_a)[onset:offset]
		wave_silence = num_a[old_offset:onset]       
		old_offset = offset
		segs_th.extend(wave_sound)
		silence_segs.extend(wave_silence)
	if write:
		write("../kestrel_segs_th.wav", fs, int16(segs_th))



	if short_features:
		F, f_names = ShortTermFeatures.feature_extraction(segs_th, fs, 0.050*fs, 0.025*fs)
		matrix_ = aT.features_to_matrix(F)
		df = pd.DataFrame([{ff_names:np.sum(ff) for ff, ff_names in zip(F, f_names)}])
		dfs=df.T


	if medium_features:
		midFeat,shortFeat,midFeatLabels=MidTermFeatures.mid_feature_extraction(
			segs_th,
			fs,
			0.43*fs, 0.43*fs,
			0.16*fs, 0.16*fs
		)
		matrix_mid = aT.features_to_matrix(midFeat)
		df = pd.DataFrame([{ff_names:np.sum(ff) for ff, ff_names in zip(midFeat, midFeatLabels)}])
		dfm=df.T


	if auto_train:
		results = aT.extract_features_and_train("../", 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmModel", False)			
		Result, P, classNames = results



