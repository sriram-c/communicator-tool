#Programme to insert a quantifier 'a' before a noun
#Written by Roja(19-06-17)
#RUN: python src/insert_quant.py cat_info_tmp1.dat quant_insert_tmp.dat gnp_info.dat rel.dat lemma_info_tmp1.dat noun-quant_tmp.dat > quant_insert.dat
#Outputs:	lemma_info.dat
#		cat_info.dat
#		noun-quant.dat
#		quant_insert.dat
#Algorithm:	1. Check whether the noun  is 'sg'
#		2. Check whether it is not marked 'def' (def means definiteness. 'the' is inserted if 'def' is mentioned by user.
#		3. Check whether the given noun has no relation with the list provided in cat_list
##################################################################################################
import sys

frt = open("lemma_info.dat", 'w')
fcat = open("cat_info.dat", 'w')
fnq = open("noun-quant.dat", "w")


cat_dic = {}
quant_info = {}
gnp_dic = {}
rel_dic = {}
lemma_dic = {}
noun_quant_dic = {}

flag = 0
cat_lst = ['det', 'dem', 'poss_pron', 'poss_propn', 'card', 'q_quant']

for line in open(sys.argv[1]):
	lst = line.strip().split('\t')
	cat_dic[lst[1]] = lst[2][:-1]

for line in open(sys.argv[2]):
	lst = line.strip().split('\t')
	quant_info[lst[1]] = lst[2][:-1]	

for line in open(sys.argv[3]):
	lst = line.strip().split('\t')
	gnp_dic[lst[1]] = lst[3] 

for line in open(sys.argv[4]):
	lst = line.strip().split('\t')
	if lst[2] not in rel_dic :
		rel_dic[lst[2]] = str(lst[3][:-1])
	else:
		rel_dic[lst[2]] = str(rel_dic[lst[2]]) + '\t' + str(lst[3][:-1])

for line in open(sys.argv[5]):
	lst = line.strip().split('\t')
	lemma_dic[lst[1]] = lst[2][:-1]

for line in open(sys.argv[6]):
	lst = line.strip().split('\t')
	noun_quant_dic[lst[1]] = lst[2][:-1]

######################################################################################

for each in sorted(cat_dic):
	flag = 0
	if 'n' in cat_dic.values():
		if cat_dic[each]  == 'n' and str(int(each)) not in quant_info.values() and gnp_dic[each] == 'sg': #Checking the conditions mentioned in alogirthm
			if each in rel_dic.keys():
				rel_lst = rel_dic[each].split('\t')
				if len(rel_lst) == 1:
					if cat_dic[rel_dic[each]] in cat_lst:
						flag = 1
				else:
					for rel in rel_lst:
						if cat_dic[rel] in cat_lst:
							flag = 1
			if flag == 0: #If no relation with cat_list then inserting 'a'
				quant_info[float(int(each)-1+0.1)] = each
				lemma_dic[float(int(each)-1+0.1)] = 'a'
				cat_dic[float(int(each)-1+0.1)] = 'det'
				noun_quant_dic[float(each)] = float(int(each)-1+0.1)
#############################################################################################

for key in sorted(quant_info):
	print '(quant_id-noun' + '\t' + str(key)  + '\t' + str(int(quant_info[key])) + ')'


###########################################################

#Print new lemma info:
for key in sorted(lemma_dic):
	        frt.write('(id-lemma_info' + '\t' + str(key) + '\t' + lemma_dic[key] + ')\n')
	

#Print new cat info:
for key in sorted(cat_dic):
        fcat.write('(id-eng_cat_info' + '\t' + str(key) + '\t' + cat_dic[key] + ')\n')

###########################################################
#Print noun quant info:
for key in sorted(noun_quant_dic):
        fnq.write('(noun-quant_id' + '\t' + str(int(key)) + '\t' + str(noun_quant_dic[key]) + ')\n')

					 
