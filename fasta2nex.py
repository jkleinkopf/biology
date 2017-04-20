#converts all fasta in the current directory into nexus files
#simply put this script into a directory with all files you want to convert and
#enter "python fasta2nex.py" into the command line.
#Input files MUST end in ".fasta" to work, and SHOULD be aligned beforehand in fasta format.
#Output files will simply be the fasta file with ".nexus" appended to the end.

import sys
import os
import glob

filenames = glob.glob("*fasta")
print "Making new nexus directory..."
os.system("mkdir nexus")

for i in range(len(filenames)):
	file=str(filenames[i])
	print "Converting %s..." % (file)
	fasta = open(file, "r")
	names, sequences = [], []
	data = fasta.read().split(">")
	del data[0]
	#print len(data)
	
	for i in range(len(data)):
		names.append(data[i].split()[0])
		sequences.append("".join(data[i].splitlines()[1:]))
	#print names

	longestseq = 0
	
	for i in range(len(sequences)):
		if len(sequences[i]) > longestseq:
			longestseq = len(sequences[i])
		else:
			pass
			
	nchar = str(longestseq)
	ntax = str(len(names))
	
	nexus = open("nexus/" + '.'.join(file.split(".")[:-1]) + ".nexus", "w")
	nexus.write("#NEXUS\nBegin data;\nDimensions ntax=%s nchar=%s;\nformat datatype=dna missing=-;\nmatrix\n\n" % (ntax, nchar))
	for i in range(len(names)):
		nexus.write(names[i] + " " + sequences[i] + "\n")
	nexus.write(";\nend;")
	print "Conversion of %s completed." % (file)
	fasta.close()
	nexus.close()
			