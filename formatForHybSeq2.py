#renames individual contigs to just the first part of the original name
#(e.g., ">JN107811.1 Boea hygrometrica chloroplast, complete genome" becomes
#">JN107811.1") and puts the sequence on a single line below the name (if 
#the sequence is broken up on different lines).

#to use in command line: python formatForHybSeq.py name_of_input_file name_of_output_file

import sys
import os

inputFile = open(str(sys.argv[1]), "r")
outputFile = open(str(sys.argv[2] + ".temp"), "w")


for line in inputFile:
	if line.startswith(">"):
		outputFile.write(line.split()[0] + "\n")
	else:
		outputFile.write(line)


inputFile.close()
outputFile.close()


data = []
names = []
sequences = []



newInputFile = open(str(sys.argv[2] + ".temp"), "r")
newOutputFile = open(str(sys.argv[2]), "w")

data = newInputFile.read().split(">")
del(data[0])

for i in range(len(data)):
	names.append(data[i].splitlines()[0])
	sequences.append("".join(data[i].splitlines()[1:]))

print "Sequences renamed and sequences put on a single line."

for i in range(len(names)):
	newOutputFile.write(">" + names[i].split()[0] + "\n" + sequences[i] + "\n")


newInputFile.close()
newOutputFile.close()

os.remove(str(sys.argv[2] + ".temp"))
