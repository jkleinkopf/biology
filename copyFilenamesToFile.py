#read all filenames with a specific extension (using "*.extension") and put names into a file.
#usage python copyFilenamesToFile.py 'directory/*extension' directory/outputFile
#need to put single quotes around '*.extension' (ie '*.fasta')

import glob
from sys import argv

extension = argv[1]

filenames = glob.glob(extension)
print filenames
with open (str(argv[2]), 'w') as outputFile:
	for i in range(len(filenames)):
		outputFile.write(str(filenames[i]) + "\n")

outputFile.close()
