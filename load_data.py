""" This file loads and seperates out the files that are relevant for training/testing.
All the original data set will be stored locally while revelant files may be pushed to
the git repo or shared via Google Drive """

import os 
directory = os.getcwd()
recordings = open(os.path.join(directory,"/APS360_Project_Data/archive/recordings/recordings"))

for sample in recordings:
    