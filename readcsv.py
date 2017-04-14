
import csv

targets=[]
with open('ac.ges.targets.csv', 'rb') as csvfile:
	readfile = csv.reader(csvfile, delimiter=' ')
	for row in readfile:
		if row not in targets:
			targets.append(row)
		else: 
			pass

newfile = open('ac.ges.targetsrefined.txt', 'w')
for sequence in targets:
	newfile.write('>'+''.join(sequence)+'\n')

