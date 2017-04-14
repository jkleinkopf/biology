#pull all filenames and concatenate those with the same prefix (eg all files starting with "CL54.Contig10_S4" are concatenated)
#usage: python readFilenames.py /path/to/dir/.extension

import glob
from sys import argv
import os

filenames = glob.glob(str(argv[1]))

print filenames
newText = open(str(argv[2]), "w")

for i in range(len(filenames)):
	newText.write(filenames[i] + "\n")

newText.close()




