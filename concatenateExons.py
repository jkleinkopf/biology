#!/usr/bin/env python

"""
Concatenate exons by sample and write to a single new file.
All exons should end in *twolines.fasta (or edit the script here).
Include a file with identifiers for the samples you are using.
E.g., my exon fastas are identified with the names ">CaffW_" ">Ccord_" (or something similar),
and I would include a file with >CaffW and >Ccord each on a single line (code splits the 
line by '_'s and takes the first split).

usage:
python concatenateExons.py samplenames.txt outputfile.fasta
"""

from sys import argv
import glob

sampleNamesFile = open(str(argv[1]), "r")

names = []

for line in sampleNamesFile:
	if line.startswith(">"):
		names.append(line.replace("\n", ""))
	else:
		pass

sequences = [''] * len(names)

#print sequences
	
#print names

for filename in glob.glob("*twolines.fasta"):
	#print filename
	
	probe_file = open(filename, "r")
	
	exon_seqnames = []
	exon_sequences = []
	
	for line in probe_file:
		if line.startswith(">"):
			exon_seqnames.append(line.split("_")[0])
		else:
			exon_sequences.append(line.split("\n")[0])
					
	#print exon_seqnames
	#print exon_sequences
	

	for i in range(len(names)):
		for k in range(len(exon_seqnames)):
			if names[i] == exon_seqnames[k]:
				#print exon_sequences[k]
				sequences[i] = "".join([sequences[i], exon_sequences[k]])
			else:
				pass

print names[2]
print sequences[2]
print names[3]
print sequences[3]

output = open(str(argv[2]), "w")

for i in range(len(names)):

	output.write(names[i] + "\n" + sequences [i] + "\n")
	
output.close()
probe_file.close()
