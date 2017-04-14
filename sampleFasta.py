
fasta = open('boea_renamed_twolines.fasta', 'r')
output = open('boea_renamed_twolines_1st100lines.fasta', 'w')

for i in range(100):
	line = fasta.next().strip()
	output.write(line+'\n')

fasta.close()
output.close()
