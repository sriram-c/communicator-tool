#Programme to insert quantifier
#Written by Roja 23/09/16
######################################################################
import sys, pdb

frt = open("lemma_info_tmp1.dat", 'w')
fcat = open("cat_info_tmp1.dat", 'w')
fnq = open("noun-quant_tmp.dat", "w")

lemma_dic = {}
new_lemma_dic = {}
cat_dic = {}
new_cat_dic = {}
gnp_dic = {}
mass_noun_dic = {}
rel_dic = {}
quant_dic = {}

cat_list = ['poss_pron', 'poss_n', 'poss_propn', 'det']
noun_type_list = ['n', 'comp_n', 'poss_n']
fp = open(sys.argv[5], 'r')
proper_noun_def = fp.read().split()
#print proper_noun_def

#To get lemma info ::
for line in open(sys.argv[1]):
	lst = line.strip().split('\t')
	lemma_dic[int(lst[1])] = lst[2][:-1]

#To get cat info ::
for line in open(sys.argv[2]):
	lst = line.strip().split('\t')
	cat_dic[int(lst[1])] = lst[2][:-1]


#To get quantifier present or not from csv:
for line in open(sys.argv[3]):
	lst = line.strip().split('\t')
	quant_dic[int(lst[1])] = lst[2][:-1]


##Get rel info:
for line in open(sys.argv[4]):
	lst = line.strip().split('\t')
	if cat_dic[int(lst[2])] in noun_type_list and cat_dic[int(lst[3][:-1])] in cat_list:
		fnq.write('(noun-quant_id' + '\t' + lst[2] + '\t' + lst[3][:-1] + ')\n')

###########################################################

#Func to insert quant
#def insert_quant(index, gnp, key):
def insert_quant(index, key):
	new_cat_dic[index] = 'det'
	new_lemma_dic[index] = 'the'
	print '(quant_id-noun' + '\t' + str(index) + '\t' + str(key) + ')'
	fnq.write('(noun-quant_id' + '\t' + str(key) + '\t' + str(index) + ')\n')

#Check when to add quant:
for key in sorted(cat_dic):
	if key in quant_dic:
		if cat_dic[key] in noun_type_list and quant_dic[key] != '-':
			index = key - 1 + 0.1
			insert_quant(index, key)
	elif cat_dic[key] == 'propn' and lemma_dic[key] in proper_noun_def: #vaha_[rAmAyaNa]_paDZa_rahA_hE
		index = key - 1 + 0.1
		new_cat_dic[key] = 'propn_def'
		insert_quant(index, key)	
###########################################################
#Get new lemma info:
for key in sorted(new_lemma_dic):
	lemma_dic[key] = new_lemma_dic[key]

#Get new cat info:
for key in sorted(new_cat_dic):
	cat_dic[key] = new_cat_dic[key]

###########################################################
#Print new lemma info:
for key in sorted(lemma_dic):
	frt.write('(id-lemma_info' + '\t' + str(key) + '\t' + lemma_dic[key] + ')\n')

#Print new cat info:
for key in sorted(cat_dic):
	fcat.write('(id-eng_cat_info' + '\t' + str(key) + '\t' + cat_dic[key] + ')\n')

###########################################################
