#!/bin

# 2019-06-12
# Brian St. Aubin





def count_nucleotides(file_name):
    """ Return the number of nucleotides contained in a fastafile"""
    gene_number = 0
    counter = 0
    with open(file_name) as in_file:
        for line in in_file:
            if line[0] == ">":
                gene_number += 1
            else:
                counter += len(line.strip())
    return counter, gene_number


# print("Nucleotides in last gene: %d, genes in file: %d" % (count_nucleotides('PhiX_genome.fasta')))
