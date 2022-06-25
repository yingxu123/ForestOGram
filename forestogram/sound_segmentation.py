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

def load_data():
    path = os.path.join(os.getcwd(), "../mp3", "XC155388-Pink_Pigeon_(song,_Mauritius,_Black_River_Gorge,_nov2012,_2).MP3")
    sound = AudioSegment.from_file(file=path)
    fs = sound.frame_rate
    left = sound.split_to_mono()[1]
    bit_depth = left.sample_width * 8
    array_type = get_array_type(bit_depth)
    num_a = array.array(array_type, left._data)
    path = os.path.join(os.getcwd(), "../onset_offset", "XC155388-Pink_Pigeon-Nesoenas_mayeri.txt")
    labels = loadtxt(path)
    return (fs,num_a,sound,labels)
def process_data():
    fs,num_a,sound,labels = load_data()
    segments = []
    for ind,lab in enumerate(labels):
        onset = int(lab[0]*fs)
        offset = int(lab[1]*fs)
        segment = num_a[onset:offset]
        segments.append(segment)
        write("../wav/segment_%s.wav" %ind, fs, int16(segment))
        #print ("finish generating segment %s is from %s s (%s) to %s (%s)s" %(ind, lab[0], onset,lab[1], offset) )
    return segments

"""
old code
num_label = np.shape(label)[0]
for raw in range(num_label):
    onset = int(label[raw, 0]*fs)
    offset = int(label[raw, 1]*fs)
    #print("onset",onset,"offset",offset)
    segment = numeric_array[onset:offset]
    write("segment_%s.wav" %raw, fs, int16(segment))
    print ("finish generating segment %s is from %s s (%s) to %s (%s)s" %(raw,label[raw, 0], onset,label[raw, 1], offset) )
"""
