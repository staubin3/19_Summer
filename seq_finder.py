#!/bin

# 06/26/2019
# Brian St. Aubin

import os


def seq_finder(seq_original, in_file):
    """return True if a sequence is in a file"""
    with open(in_file, 'r') as new_file:
        old_line = ""
        seq_original = seq_original.upper()
        for line in new_file:
            new_line = (old_line + line).strip().upper()
            print(line)
            if len(seq_original) > len(new_line):
                old_line = new_line
                continue
            if seq_original in new_line:
                return True
            else:
                old_line = new_line[-len(seq_original):]
    return False


query = 'ATCG'
for file in os.listdir("."):
    if file.endswith(".fasta") or file.endswith(".fa"):
        if seq_finder(query, file):
            print('%s is in %s' % (query, file))
