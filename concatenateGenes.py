#pull all filenames and concatenate those with the same prefix (eg all files starting with "CL54.Contig10_S4" are concatenated)
#usage: python readFilenames.py /path/to/dir/.extension

import glob
from sys import argv
import os

filenames = glob.glob("*" + str(argv[1]))
prefix = []
genes = []

for i in range(len(filenames)):
	split = str(filenames[i].split("...")[0])
	#print split
	if split not in prefix:
		prefix.append(split)
	else:
		pass

for i in range(len(prefix)):
	name = prefix[i]
	os.system("perl catfasta2phyml.pl -f %s* > %s.cat.fasta" % (name, name))
	os.system("perl catfasta2phyml.pl %s* > %s.cat.phy" % (name, name))

#print len(prefix)

