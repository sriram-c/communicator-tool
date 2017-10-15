#Checking syntax errors in user csv 

import sys

f = open(sys.argv[1], 'r')
fr = f.readlines()
wrd_lst = []
for i in range(0, len(fr)):
	lst = fr[i].strip().split(',')
	#Case1::
	if i == 0:
		wrd_lst = lst 
		#Checking sentence type::
		if  len(lst[len(lst)-1]) != 1:
			print '%%%%%%%%%%%  Sentence type missing in row 1 %%%%%%%%%%%%%%'
		
		########################################################
	#Case2::
	if i == 1:
		cat_lst = fr[i+2].strip().split(',')
		for j in range(0, len(cat_lst)):
			#checking whether root and tam are written correctly in 'v' 
			if cat_lst[j] == 'v' and '-' not in wrd_lst[j]:
				print '%%%%%%%%%%%%%% Syntax error:: in row 1 , root and tam need to be separated with "-"  in ' + wrd_lst[j] + '\t%%%%%%%%%' 
		########################################################
	#Case3::
	if i >= 9:
		print '%%%%%%%%%%%% No: of rows are are greater than 9 rows. Please check. %%%%%%%%%%'
		########################################################
		
				
