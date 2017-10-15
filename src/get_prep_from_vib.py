#Get preposition from hindi vibhakti
######################################
import sys

d = open('dic/default_prep_dic', 'r')
def_dic = d.readlines()

dic = {}

for line in def_dic:
	if '#' not in line[0]:
		lst = line.strip().split('\t')
		dic[lst[0]] = lst[1]


for line in open(sys.argv[1]):
	lst = line.strip().split('\t')
	if '_' in lst[2]:
		vib = lst[2].split('_')
		for key in dic:
			if key + ')' == vib[-1]:
				print '(id-preposition' + '\t' + lst[1] + '\t' + dic[key] + ')'

