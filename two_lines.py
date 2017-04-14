#put name on first line and sequence on second line

input_file = "S4_primulina_renamed.fasta"
fna = open(input_file, "r")
output_file = "S4_primulina_renamed.twolines.fasta"
outfile = open(output_file, "w")

names = []
sequences = []

#create list by splitting data at ">"s. Delete data[0] which is blank.
data = fna.read().split(">")
del(data[0])

#append names of each sequences to names list, and sequences to sequences list.
for i in range(len(data)):
	names.append(data[i].splitlines()[0])
	sequences.append("".join(data[i].splitlines()[1:]))

#new file with name on first line, sequence on second line
for i in range(len(names)):
	outfile.write(">" + names[i] + "\n" + sequences[i] + "\n")




fna.close()
outfile.close()
