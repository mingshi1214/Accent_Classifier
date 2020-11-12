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
        self.english = 0 
        self.hindi = 0
        self.mandarin = 0
        self.tagalog = 0
        self.samples = 1000

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
        
    def save_data(self,data,abs_dir,sub_dir, file_name):
        #speech,s = librosa.load(file_path)
        #mfcc = librosa.feature.melspectrogram(y = speech,sr = s) 
        #logspec = librosa.amplitude_to_db(mfcc)
        elems = sub_dir.split('/')
        new_sub_dir = os.path.join("data_mfcc", elems[1])
        if elems[1] == "english" :
            num = self.english
            self.english += 1
            if self.english > self.samples:
                return True 
        if elems[1] == "hindi":
            num = self.hindi
            self.hindi += 1
            if self.hindi > self.samples:
                return True
        if elems[1] == "mandarin":
            num = self.mandarin
            self.mandarin += 1 
            if self.mandarin > self.samples:
                return True
        if elems[1] == "tagalog":
            num = self.tagalog
            self.tagalog += 1 
            if self.tagalog > self.samples:
                return True
        name_only = file_name.split(".mp3")[0]
        new_filename = name_only + "_" + str(num)
        path = [abs_dir,new_sub_dir,new_filename]
        save_path = os.path.join(*path)
        print(save_path)
        pylab.axis('off')
        pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])
        librosa.display.specshow(data)
        pylab.savefig(save_path, bbox_inches=None, pad_inches=0)
        pylab.close()
        return True 
    
    def uniform_clip_split(self, abs_dir, sub_dir, file_name, duration):
        path = [abs_dir,sub_dir,file_name] 
        file_path = os.path.join(*path)
        speech,s = librosa.load(file_path)
        num_frames = int(duration*s)
        for (start,end) in self.windows(librosa.get_duration(speech),num_frames):
            if (len(speech[start:end]) == num_frames):
                clip = speech[start:end]
                mfcc = self.get_MFCC(clip)
                self.save_data(mfcc,abs_dir,sub_dir,file_name)
        return True 
        



        


data = Augment()
print(data.get_MFCC(os.getcwd(), "data_specific/english", "english1.mp3"))

#data.visualize_data(os.path.join(os.getcwd(),"data_specific/english/english1.mp3"))
#data.uniform_clip_split(os.getcwd(), "data_specific/english", "english1.mp3",0.5)    


    