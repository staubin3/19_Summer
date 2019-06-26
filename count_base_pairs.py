#!/bin/python
# Description: count the number of base pairs in a fasta file
# Kenia Segura Aba
# 06-12-2019

with open ('PhiX_genome.fasta') as inF:
  inF.readline() # skip FASTA header
  total = 0
  for line in inF: 
    total += len (line.strip())
  print ('total base pairs:', total)
