#This script reads the blocks for probe design fasta file (from the hyb-seq
#protocol by weitemier et al) and gives back:
#-Total number of exons, and how many transcriptomic contigs (genes)
#and genomic contigs were used to ID these exons.
#-Total base pairs in the file.
#-Avg length of exon
#-Longest and shortest exons.


fasta = open("blocks_for_probe_design.fasta", "r")

txloci = []
gnloci = []
numEachLoci = []
totalNumExon = 0
totalExonLen = 0
longestExon = 500
shortestExon = 500

for line in fasta:
	if line.startswith(">"):
		totalNumExon += 1
		tx = line.split(",")[0]
		gn = line.split(",")[1]
		#print ln
		if tx not in txloci:
			txloci.append(tx)
		if gn not in gnloci:
			gnloci.append(gn)
		else:
			pass

	else:
		exonLength = len(line)
		totalExonLen += exonLength
		if exonLength > longestExon:
			longestExon = exonLength
		elif exonLength < shortestExon:
			shortestExon = exonLength
		else:
			pass



print "\tThere are " + str(totalNumExon) + " exons from " + str(len(txloci)) + " transcriptome loci (genes) or " + str(len(gnloci)) + " genome loci."
print "\tIn total there are " + str(totalExonLen) + "bp in this file."
print "\tAverage length of exon is " + str(totalExonLen/totalNumExon) + "bp."
print "\tThe longest exon is " + str(longestExon) + "bp long."
print "\tThe shortest exon is " + str(shortestExon) + "bp long."
