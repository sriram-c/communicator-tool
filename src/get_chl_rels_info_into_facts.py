#python get_chl_rels_info_into_facts.py <csv file> 
#Written by Roja 10/09/16
#######################################################################
import sys,re

f = open(sys.argv[1], 'r')
fr = f.readlines()

fgnp   = open("gnp_info.dat", 'w')
frt    = open("lemma_info_tmp.dat", 'w')
fcat   = open("cat_info_tmp.dat", 'w')
fstype = open("sent_type.dat", 'w')
ferel  = open("rel.dat", 'w')
ftem   = open('template_info.dat', 'w')
fprep  = open('insert_prep.dat', 'w')
fquant = open('quant_info_tmp.dat', 'w')
cat_dic = {}
quant_dic = {}

#def check_

#Function to print CHL info to facts format:
def print_info_from_lst_to_fact(f_name, fact_name, List):
	count = 0
	for i in range(0, len(List)):
		count += 1
		if '[' in List[i]:
			gnp = List[i][1:-1].split()
			f_name.write('(' + fact_name + '\t' + str(count) + '\t' + gnp[0] + '\t' + gnp[1] + '\t' + gnp[2] + ')\n')
		elif '+' in List[i]: #Ex: 6:ARG1/EQ-from-2:ARG2/NEQ+4:ARG1/EQ
			lst = List[i].split('+')
#			print lst
			for each in lst:
				rel = each.split(':')
#				print rel
				if '-' in rel[1]:
					prep_info = re.split('-\w+-', rel[1])
					fprep.write('(' + 'prep_id-head_id-child_id' + '\t' + str(count) + '\t' + rel[0] + '\t' + prep_info[1] + ')\n')
				else:
					f_name.write('(' + fact_name + '\t' + rel[1] + '\t' + rel[0] + '\t' +  str(count) + ')\n')
		elif ':' in List[i]:
			lst = List[i].split(':')
			pattern = re.search('-\w+-', lst[1])
			if pattern  and '_' not in lst[1]:
				prep_info = re.split('-\w+-', lst[1])
				fprep.write('(' + 'prep_id-head_id-child_id' + '\t' + str(count) + '\t' + lst[0] + '\t' + prep_info[1] + ')\n')
			elif '_' in lst[1]:
				rel_info = re.split('-\w+_\w+-', lst[1])
				f_name.write('(' + fact_name + '\t' + rel_info[0] + '\t' + lst[0] + '\t' + str(count) + ')\n')
				f_name.write('(' + fact_name + '\t' + lst[2] + '\t' + rel_info[1] + '\t' + str(count) + ')\n')
			else:
				f_name.write('(' + fact_name + '\t' + lst[1] + '\t' + lst[0] + '\t' + str(count) + ')\n')
		elif fact_name == 'id-lemma_info':
			print List[i]
			lst = List[i].split('_')
			if '_' in List[i]:
				f_name.write('(' + fact_name + '\t' + str(count) + '\t' + lst[0] + ')\n')
				if len(lst) == 2:
					ftem.write('(id-template_info' + '\t' + str(count) + '\t' + lst[1] + ')\n')
			else:
				f_name.write('(' + fact_name + '\t' + str(count) + '\t' + List[i] + ')\n')
		else:
			if List[i] != '':
				print List[i]
				if fact_name == 'id-eng_cat_info':
					cat_dic[count] = List[i]
				if fact_name != 'id-quant_info':
					f_name.write('(' + fact_name + '\t' + str(count) + '\t' + List[i] + ')\n')
				else:
					quant_dic[count] = List[i]
			#else:
			#	if fact_name == 'id-quant_info':
			#		quant_dic[count] = '-'


for i in range(0, len(fr)):
	lst = fr[i].strip().split(',')
	if i == 1:
		print_info_from_lst_to_fact(frt, 'id-lemma_info', lst)
	if i == 3:
		print_info_from_lst_to_fact(fcat, 'id-eng_cat_info', lst)
	if i == 4:
		print_info_from_lst_to_fact(fquant, 'id-quant_info', lst)
	if i == 5:
		print_info_from_lst_to_fact(fgnp, 'id-gen-num-per', lst)
	if i == 6:
		print_info_from_lst_to_fact(fstype, 'sentence_type', lst)
	if i == 7:
		print_info_from_lst_to_fact(ferel, 'id-eng_rel', lst)
	if i == 8:
		print_info_from_lst_to_fact(ftem, 'id-template_info', lst)


#To get quantifier present or not for a noun:
for key in sorted(cat_dic):
	if key in quant_dic:
	        if cat_dic[key] == 'n' or cat_dic[key] == 'comp_n' or cat_dic[key] == 'poss_n': 
        	        fquant.write('(' + 'id-quant_info' + '\t' + str(key) + '\t' + quant_dic[key] + ')\n')
