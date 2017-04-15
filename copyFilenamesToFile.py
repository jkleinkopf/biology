#read all filenames with a specific extension (using "*.extension") and put names into a file.
#usage python copyFilenamesToFile.py directory/*extension

import glob
from sys import argv
import os

filenames = glob.glob(str(argv[1]))

print filenames
newText = open(str(argv[2]), "w")

for i in range(len(filenames)):
	newText.write(filenames[i] + "\n")

newText.close()




