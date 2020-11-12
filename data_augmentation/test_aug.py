""" Class of modular functions for augmenting data.
Including: 
1. Getting MFCC graph representation
2. Using rubberband to modify pitch 
3. Trimming into different lengths 
4. Adding gaussian noise 
"""
import os 
import librosa
class Augment:

    def get_MFCC(self,abs_dir,sub_dir,file_name, bands,frames):
        path = [abs_dir,sub_dir,file_name] 
        file_path = os.path.join(path*)
        speech = librosa.core.load(file_path)
        mfcc = librosa.feature.melspectrogram(speech,n_mels = bands)
        logspec

        



    