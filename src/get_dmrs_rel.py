#Programme to print dmrs rels from Karaka rels
#Written by Roja(15/10/16)
#Input : CSV file 
#Output : CSV file with mapped dmrs rels. Ex: karwA is mapped to ARG1/NEQ
#########################################################################

import sys

f = open(sys.argv[1], 'r')
fr = f.readlines()
f1 = open('dic/link_list.txt', 'r')
fr1 = f1.readlines()

fw = open(sys.argv[2], 'w')

link_dic = {}

new_link_lst = []

#get link list in a dic format:
for line in fr1:
	lst = line.strip().split('\t')
	link_dic[lst[0]] = lst[1]

#Function to compare dmrs rels:
def check_dmrs_rels(lst):
	for i in range(0, len(new_link_lst)-1):
		if len(lst) <= len(new_link_lst):
			if lst[i] != new_link_lst[i]:
				print 'mismatch in dmrs rels in col no: ' +  str(i) +  '\t' + lst[i] + '\t' + new_link_lst[i]
			


for i in range(0, len(fr)):
	lst = fr[i].strip().split(',')
	if i == 3:
		for rel in lst:
			if ':' in rel:
				rel_name = rel.split(':')
				if rel_name[1] in link_dic.keys():
#					print rel_name[1], '----', link_dic.keys()
					new_link_lst.append(link_dic[rel_name[1]])
				else:
					new_link_lst.append('')
			else:
				new_link_lst.append('')
		fw.write(fr[i])
	elif i == 9:
		check_dmrs_rels(lst)
#		print ','.join(new_link_lst)
		fw.write('%s\n' % ','.join(new_link_lst))
	else:
		fw.write(fr[i])

if len(fr) != 10:
	fw.write('%s\n' % ','.join(new_link_lst))
