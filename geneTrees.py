#conduct ML search using raxml on all loci in a directory
#usage: python geneTrees.py /path/to/dir/.extension
#replace -o in the os.system() below to your outgroup of choosing... add/modify bootstrap with -# and random seed -b (-x instead if you want to do rapid bootstrapping


import os
from sys import argv
import glob

bestOut=open("bestTrees.files", "w")
bootOut=open("bootstrap.files", "w")

filenames = glob.glob("*" + str(argv[1]))
#print filenames

for i in range(len(filenames)):
	os.system("raxml -m GTRGAMMA -p 12345 -x 12345 -f a -N 100 -s %s -o BoeaCP -n %s" % (filenames[i], filenames[i]))

bootstrapFiles = glob.glob("RAxML_bootstrap*")
for i in range(len(bootstrapFiles)):
	bestOut.write("RAxML_bestTree." + str('.'.join(bootstrapFiles[i].split(".")[1:])) + "\n")
	bootOut.write(bootstrapFiles[i] + "\n")

os.system("java -jar ~/Desktop/Joseph/programs/Astral/astral.4.10.12.jar -i bestTrees.files -b bootstrap.files -r 100 -a astralMultipleIndividuals.txt -o astralBootstrap.tre")

bestOut.close()
bootOut.close()
