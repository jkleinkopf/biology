#!/usr/bin/env python

"""
The purpose of this program is to pull exon names and contigs from multiple fasta files
and put each contig from each fasta file into a new fasta file (named for 
the contig). IE, if you have 36 files, each with 570 exon sequences, this
program will read the names of the exon sequences from the original probe set, and use 
this information to build 570 fasta files, each with 36 homologous sequences. This 
relies on the naming between probe-set and your sample files to be identical, as it does 
not use sequence similarity to ID homologous sequences. This program was originally
designed to be used on consensus sequences following read mapping to a probe-set in 
geneious.

Put all sample files (should end in *assembly.fasta), this script, and the probe design 
file into a single directory and run the program. The probe file should be called 
"blocks_for_probe_design.fasta" (or you can modify the script here to read whatever you 
name your file).
"""

import os
import glob

probe_set = open("blocks_for_probe_design.fasta", "r")
probe_names = []

for line in probe_set:
	if line.startswith(">"):
		contig_name = line.split("\n")[0].replace(">", "")
		probe_names.append(contig_name)
	else:
		pass

for i in range(len(probe_names)):
	individual_probe_fasta = open("%s" % probe_names[i] + "_probe.fasta", "w")

#print probe_names[0:10]
#print sample_contig_names[0:10]

for filename in glob.glob("*assembly.fasta"):
	print filename
	
	sample_contig_names = []
	sample_contig_sequences = []
	
	assembly = open(str(filename), "r")
	for line in assembly:
		if line.startswith(">"):
			sample_contigs = line.split()[0].replace(">", "")
			sample_contigs = sample_contigs.replace("Consensus", "Contig")
			sample_contig_names.append(sample_contigs)
		else:
			sample_contig_sequences.append(line)
			
	#print sample_contig_names[5]
	#print sample_contig_sequences[5]
	
	for i in range(len(probe_names)):
		individual_probe_fasta = open("%s" % probe_names[i] + "_probe.fasta", "a")
		for k in range(len(sample_contig_names)):
			if probe_names[i] == sample_contig_names[k]:
				individual_probe_fasta.write(">" + str(filename.split(".")[0]) + "_" + str(sample_contig_names[k]) + "\n")
				individual_probe_fasta.write(str(sample_contig_sequences[k]))
			else:
				pass

			
	individual_probe_fasta.close()	
assembly.close()
	
#for filename in glob.glob("*_probe.fasta"):
#	print filename

probe_set.close()
