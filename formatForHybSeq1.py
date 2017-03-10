#only use this if each contig name has only one occurrance of ">" at the
#beginning of the line. eg, ">Contig1_344 vitis vinifera >gi_genbankno..."
#will split the line at two places and save both. Either replace the second
#instance of ">" in each name, or use formatForHybSeq2.py
#This file is probably faster, but formatForHybSeq2 will not mess up the file.

#renames individual contigs to just the first part of the original name
#(e.g., ">JN107811.1 Boea hygrometrica chloroplast, complete genome" becomes
#">JN107811.1") and puts the sequence on a single line below the name (if
#the sequence is broken up on different lines).

#to use in command line: python formatForHybSeq.py input_file output_file

import sys

data = []
names = []
sequences = []

inputFile = open(str(sys.argv[1]), "r")
outputFile = open(str(sys.argv[2]), "w")

data = inputFile.read().split(">")
del(data[0])

for i in range(len(data)):
	names.append(data[i].splitlines()[0])
	sequences.append("".join(data[i].splitlines()[1:]))

print "Sequences renamed and sequences put on a single line."

for i in range(len(names)):
	outputFile.write(">" + names[i].split()[0] + "\n" + sequences[i] + "\n")

inputFile.close()
outputFile.close()
