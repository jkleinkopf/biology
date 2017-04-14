#!/bin/bash
FILES=*.fasta

for f in $FILES
do
	echo "Processing $f ... "
	mafft $f > ALIGNED_$f

done



