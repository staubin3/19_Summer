#!/usr/bin/python3
#code club day 3
file_fh = open("PhiX_genome.fasta")
num = 0
with open("PhiX_genome.fasta")as input:
    for line in input:
        #print(line.strip())
        num += len(line)
        num -= 2
print(num)
