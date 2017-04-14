#rename fasta files with no spaces
import sys

fasta = "S4_primulina.fasta"
output = "S4_primulina_renamed.fasta"

with open(fasta, "r") as input_file, open(output, "w") as output_file:
	for line in input_file:
		if line.startswith(">"):
			output_file.write(line.split()[0] + "\n")
		else:
			output_file.write(line)




input_file.close()
output_file.close()
