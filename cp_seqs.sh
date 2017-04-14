#!/bin/bash
#run this script using ./cp_seqs.sh plastid_fasta transcriptome_or_genome_fasta

echo "Blat-ing $2 against $1"
blat $1 $2 -noHead CPtargets_$2.pslx

cut -f10 CPtargets_$2.pslx | sort | sed -e 's/^/\>/' > CPhits_$2.txt

python cpNewFasta.py $2
