#Programme to get prep from verb from a dic to facts format
#Written by Roja(01-04-17)
#RUN: python src/get_prep_from_verb.py dic/verb_kAraka_prep_mapping.txt > prep_insertion_based_on_verb.dat
################################################################################################
import sys

lem = ''

for line in open(sys.argv[1]):
	lst = line.strip('\n').split('\t')
	#print lst
	if lst[0]  != '':
		lem = lst[0]
	print '(verb-rel-prep' + '\t' + lem + ' ' + lst[1] + ' ' + lst[2] +')'
