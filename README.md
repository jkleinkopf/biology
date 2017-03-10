#cyrtandra

#formatForHybSeq
Takes a genome or transcriptome file and renames contigs to have no spaces, and puts each name/sequence pair on two lines rather than in blocks. Use formatForHybSeq1 only if contig names don't each have more than 1 occurrance of ">" (otherwise use formatForHybSeq2).

#hybSeqBlocksInfo
Takes the hyb-seq output file (blocks_for_exon_probes.fasta) and reads number of exons, number of genes (and genomic contigs), total base-pairs, average length of exon, and longest/shortest exon lengths.

