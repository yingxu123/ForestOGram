from numpy import int16
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

def load_data(audio_path,labels_path=None):
    sound = AudioSegment.from_file(file=audio_path)
    fs = sound.frame_rate
    #if False:
    #    ss = sound.from_mp3(path)
    #try:
    #    left = sound.split_to_mono()[1]
    #    bit_depth = left.sample_width * 8
    left = sound.split_to_mono()[0]
    bit_depth = left.sample_width * 8

    array_type = get_array_type(bit_depth)
    num_a = array.array(array_type, left._data)
    if labels_path is not None:

        #path = os.path.join(os.getcwd(), "../onset_offset", "XC155388-Pink_Pigeon-Nesoenas_mayeri.txt")
        labels = loadtxt(labels_path)
    else:
        labels = None
    return (fs,num_a,sound,labels)
def process_data(audio_path,labels_path=None,write_waves=False):
    fs,num_a,sound,labels = load_data(audio_path,labels_path=labels_path)
    segments = []
    for ind,lab in enumerate(labels):
        onset = int(lab[0]*fs)
        offset = int(lab[1]*fs)
        segment = num_a[onset:offset]
        segments.append(segment)
        if write_waves:
            write("../../outputs/wav/segment_%s.wav" %ind, fs, int16(segment))
        #print ("finish generating segment %s is from %s s (%s) to %s (%s)s" %(ind, lab[0], onset,lab[1], offset) )
    return segments
