""" This file loads and seperates out the files that are relevant for training/testing 
into seperate folders and converts them to .wav file types.
All the original data set will be stored locally while revelant files may be pushed to
the git repo or shared via Google Drive """
# sample librosa load: file = librosa.load(os.path.join(recordings,sample)) NOTE: does 
# take a while to load - will need to convert to MFCCs later 
import os 
import numpy as np
import re 
import re
import librosa
import pandas as pd
from shutil import copyfile
match = re.match(r"([a-z]+)([0-9]+)", 'foofo21', re.I)
directory = os.getcwd()
recordings = os.path.join(directory,"APS360_Project_Data/archive/recordings/recordings/")
csv = os.path.join(directory,"APS360_Project_Data/archive/speakers_all.csv")
df = pd.read_csv(csv)
subdf = df[["filename", "native_language", "country", "file_missing?"]]
rows_not_missing = subdf.loc[subdf['file_missing?'] == False]

english_samples = rows_not_missing.loc[rows_not_missing['native_language'] == 'english']
english_samples = english_samples.loc[rows_not_missing['country'].isin(['usa','canada'])]
english_samples = english_samples[:50]

mandarin_samples = rows_not_missing.loc[rows_not_missing['native_language'] == 'mandarin']
mandarin_samples = mandarin_samples[:50]

tagalog_samples = rows_not_missing.loc[rows_not_missing['native_language'] == 'spanish']
tagalog_samples = tagalog_samples[:50]

hindi_samples = rows_not_missing.loc[rows_not_missing['country'] == 'india']
hindi_samples = hindi_samples[:50]

samples_lst = [english_samples, mandarin_samples, tagalog_samples, hindi_samples]
samples = pd.concat(samples_lst)
cnt = 0 
samples = samples.sample(frac=1)
samples = samples['filename']
for sample in samples:
    cnt = cnt + 1

    # Get the native language of the speaker
    match = re.match(r"([a-z]+)([0-9]+)", sample, re.I)
    if match:
        lang = match.groups()[0]
    
    # Save 70% of data to the train set  
    if cnt/len(samples) < 0.70:
        sample_name = sample + ".mp3"
        dirs = [directory,"audio_split_2","train",lang]
        save_path = os.path.join(*dirs)
        try:
            copyfile(os.path.join(recordings,sample_name), os.path.join(save_path,sample_name))
        except:
            os.mkdir(save_path)
            copyfile(os.path.join(recordings,sample_name), os.path.join(save_path,sample_name))
    
    # Save 15% of data to the validation set 
    if cnt/len(samples) >= 0.70 and cnt/len(samples) < 0.85:
        sample_name = sample + ".mp3"
        dirs = [directory,"audio_split_2","validation",lang]
        save_path = os.path.join(*dirs)
        try:
            copyfile(os.path.join(recordings,sample_name), os.path.join(save_path,sample_name))
        except:
            os.mkdir(save_path)
            copyfile(os.path.join(recordings,sample_name), os.path.join(save_path,sample_name))
    
    # Save 15 % of data to the test set 
    if cnt/len(samples) >= 0.85:
        sample_name = sample + ".mp3"
        dirs = [directory,"audio_split_2","test",lang]
        save_path = os.path.join(*dirs)
        try:
            copyfile(os.path.join(recordings,sample_name), os.path.join(save_path,sample_name))
        except:
            os.mkdir(save_path)
            copyfile(os.path.join(recordings,sample_name), os.path.join(save_path,sample_name))
    

    
    
