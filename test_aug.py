""" Class of modular functions for augmenting data.
Including: 
1. Getting MFCC graph representation
2. Using rubberband to modify pitch 
3. Trimming into different lengths 
4. Adding gaussian noise 
"""
import os 
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt 
import pylab
from PIL import Image

class Augment:
    def __init__(self):
        self.mfcc_data = []
        self.bands = 128
        self.frames = 128

    def windows(self,data,window_size):
        start = 0 
        yield start, start + window_size
        start += (window_size / 2)    

    def get_MFCC(self, speech):
        window_size = 512*127
        log_specgrams = []
        for (start,end) in self.windows(speech,window_size):
            if (len(speech[start:end]) == window_size):
                clip_bin = speech[start:end]
                mfcc = librosa.feature.melspectrogram(clip_bin,n_mels = self.bands) 
                logspec = librosa.amplitude_to_db(mfcc)
                logspec = logspec.T.flatten()[:,np.newaxis].T
                log_specgrams.append(logspec)
        log_specgrams = np.array(log_specgrams)
        log_specgrams = np.asarray(log_specgrams).reshape(len(log_specgrams),self.bands,self.frames)
        feature = log_specgrams
        return np.array(feature)
        
    def save_data(self,data,abs_dir,file_name):
        #speech,s = librosa.load(file_path)
        #mfcc = librosa.feature.melspectrogram(y = speech,sr = s) 
        #logspec = librosa.amplitude_to_db(mfcc)
        new_sub_dir = "data_mfcc"
        save_path = os.path.join(abs_dir,)
        pylab.axis('off') # no axis
        pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[]) #
        librosa.display.specshow(logspec)
        pylab.savefig(save_path, bbox_inches=None, pad_inches=0)
        pylab.close()
        return True 
    
    def uniform_split_clip(self, abs_dir, sub_dir, file_name, duration):
        path = [abs_dir,sub_dir,file_name] 
        file_path = os.path.join(*path)
        speech,s = librosa.load(file_path)
        num_frames = int(duration*s)
        for (start,end) in self.windows(librosa.get_duration(speech),num_frames):
            if (len(speech[start:end]) == window_size):
                clip = speech[start:end]
                mfcc = self.get_MFCC(clip,self.bands,self.frames)
                self.save_data(mfcc,abs_dir,sub_dir,file_name)
                self.mfcc_data.append(mfcc)
        



        


data = Augment()
#data.get_MFCC(os.getcwd(), "data_specific", "english/english1.mp3")
#data.visualize_data(os.path.join(os.getcwd(),"data_specific/english/english1.mp3"))
data.uniform_split_clip(os.getcwd(), "data_specific", "english/english1.mp3",1)    



    