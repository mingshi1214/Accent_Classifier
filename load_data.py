""" This file loads and seperates out the files that are relevant for training/testing 
into seperate folders and converts them to .wav file types.
All the original data set will be stored locally while revelant files may be pushed to
the git repo or shared via Google Drive """

import os 
import numpy as np
import re 
import re
match = re.match(r"([a-z]+)([0-9]+)", 'foofo21', re.I)
directory = os.getcwd()
recordings = os.path.join(directory,"APS360_Project_Data/archive/recordings/recordings/")

for sample in os.listdir(recordings):
    match = re.match(r"([a-z]+)([0-9]+)", sample, re.I)
    if match:
        lang = match.groups()[0]
        print(lang)
    save_path = os.path.join