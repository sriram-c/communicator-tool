#Programme to check syntax errors in CSV file
#Written by Roja(30-10-2016)
#RUN: python check_syntax_error.py <CSV-file> 
#####################################################
import sys

f = open(sys.argv[1], 'r')
fr = f.readlines()

for i in range(0, len(fr)):
	if i == 4: #Quantifier needed row
		lst = fr[i].strip().split(',')
		for each in lst:
			if each != '' and each != 'def':
				print 'Syntax Error: Expected only "def" or "," in row 5'
	##################################################################################
	
