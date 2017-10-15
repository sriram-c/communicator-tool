#Programme to get prep from verb from a dic to facts format
#Written by Roja(01-04-17)
#RUN: python src/get_prep_from_verb.py dic/verb_rel_prep_mapping.txt > prep_insertion_based_on_verb.dat
################################################################################################
import sys

for line in open(sys.argv[1]):
	lst = line.strip().split('\t')
	print '(verb-rel-prep' + '\t' + lst[0] + ' ' + lst[1] + ' ' + lst[2] +')'
