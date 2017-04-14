#rename fasta files with no spaces

fasta = "GCA_001598015.1_Boea_hygrometrica.v1_genomic.fasta" #enter name of fasta file here

with open(str(fasta), "r") as input_file, open("boea_names.txt", "w") as output_file:
	for line in input_file:
		if line.startswith(">"):
			output_file.write(line)




input_file.close()
output_file.close()
