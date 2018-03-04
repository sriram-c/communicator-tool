#Programme to get concept dictionary info from user
#RUN: python src/get_concept_info.py output/boy_can_eat_rice_with_the_spoon_user.csv.tmp3 dic/concept_dictionary_user.txt dic/concept_dictionary_dev.txt  dic/pronoun_lemma_dic.txt output/$1.tmp4 output/replace_id.dat
#Written by Roja(28-06-17)
#(Note: separated below code from convert_user_to_devloper_csv.py)
############################################################################################################################################## 
import sys, pdb

f = open(sys.argv[1], 'r')
fr = f.readlines()
fw = open(sys.argv[5], 'w')
fw1 = open(sys.argv[6], 'w')

chunk_dic = {}
lemma_dic = {}
ids_dic = {}
cat_dic = {}
gnp_dic = {}
def_dic = {}
rel_dic = {}
concept_user_dic = {}
concept_dev_dic = {}
pronoun_lemma_dic = {}

###########
eng_lemma_dic = {}
cat = ''
lemma = ''
gnp_lst = []

#Store user concept info
for line in open(sys.argv[2]):
	lst = line.strip().split(',')
	concept_user_dic[lst[0]] = lst[2] #lst[2] is english column 

#Store dev concept info
for line in open(sys.argv[3]):
	lst = line.strip().split(',')
	concept_dev_dic[lst[0]] = lst[1] 

#Store pronoun info
for line in open(sys.argv[4]): #pronoun dic
	lst = line.strip().split('\t')
	pronoun_lemma_dic[lst[0]] = lst[1]

dic_names = [ chunk_dic, lemma_dic, ids_dic, cat_dic, def_dic, gnp_dic, None, rel_dic ]

#Function to print user csv data into dic:
def print_data_into_dic(lst, dic):
	count = 0
	for each in lst:
		count += 1
		dic[count] = each

for i in range(0, len(fr)):
	lst = fr[i].strip().split(',')
	if i != 6 and i != 8:
		print_data_into_dic(lst, dic_names[i])

for key in sorted(def_dic):
	if def_dic[key] != 'def':
		cat_dic[key] = def_dic[key]
		def_dic[key] = ''


#Get lemma info for pronoun:
def get_lemma_info(lemma, cat, gnp_lst):
	if gnp_lst[2] == '-':
		gnp_lst[2] = 'a'
	gnp_n = '[' + gnp_lst[0] + ' ' + gnp_lst[1] + ' ' + gnp_lst[2] + ']'
	key = lemma + ',' + cat + ',' + str(gnp_n)
	if key in pronoun_lemma_dic:
		print key
		return pronoun_lemma_dic[key]
	elif lemma != '':
		print '%%%%%%%%%%% Error:: Check pronoun "' +  key  +  '" %%%%%%%%%%%%'
		sys.exit()
	else:
		return ''

#Get template key and lemma info:
def get_template_key_nd_lemma_frm_concept_dic(lemma, col_info):
	if lemma in concept_user_dic:
		v = concept_user_dic[lemma].split('_')
		#print v, lemma, concept_user_dic[lemma]
                eng_lemma_dic[col_info] = v[0]
		cat_dic[col_info] = concept_dev_dic[concept_user_dic[lemma]]
	elif lemma == '':
		eng_lemma_dic[col_info] = ''
		cat_dic[col_info] = ''
		print 'Lemma not neccessary for this word', lemma 
	else:
		print '%%%%%%%%%%% Root missing in dic. Please add root for "' + lemma + '" in dic/concept_dictionary_user.txt and run "sh compile.sh" %%%%%%%%%%%%'


#Get concept info for each id:
for key in sorted(ids_dic):
	if key in cat_dic:
		cat = cat_dic[key]
	if key in lemma_dic:
		lemma = lemma_dic[key]
	if key in gnp_dic:
		gnp_lst = gnp_dic[key][1:-1].split()
	if cat == 'propn':
		if '_' in lemma:
			root = lemma.split('_')
			eng_lemma_dic[key] = root[0]
	elif cat == 'pron':
		out = get_lemma_info(lemma, cat, gnp_lst)
		eng_lemma_dic[key] = out
	elif cat == 'kriyA-praSna':
		l = lemma.split('+')
		get_template_key_nd_lemma_frm_concept_dic(l[0]+ '_1', key) # l[0] = kyA
		get_template_key_nd_lemma_frm_concept_dic(l[1] , len(eng_lemma_dic)+1) #Stroring kara info in last 
		c = chunk_dic[key].split('+') 
		chunk_dic[key] = c[0] 
		punct = chunk_dic[len(eng_lemma_dic)]  
		chunk_dic[len(eng_lemma_dic)] = c[1]  #Interchanging kara info before punc
		chunk_dic[len(eng_lemma_dic)+1] = punct #Storing punct in last as usually 
		ids_dic[len(ids_dic)+1] = str(len(ids_dic)+1)
		fw1.write('replace_id' + '\t' + str(len(eng_lemma_dic)) + ':' + str(key) + '\n')
		if key not in rel_dic.keys(): 
			rel_dic[key] = ''  #Storing empty rel info for 'kyA' 

	else:
		get_template_key_nd_lemma_frm_concept_dic(lemma, key)


#Print csv:
for i in range(0, len(fr)):
	if i == 0:
		fw.write('%s\n' % ','.join(chunk_dic.values()))
	elif i == 1:
		fw.write('%s\n' % ','.join(eng_lemma_dic.values()))
	elif i == 2:
		fw.write('%s\n' % ','.join(ids_dic.values()))
	elif i == 3:
		fw.write('%s\n' % ','.join(cat_dic.values()))
	elif i == 4:
		fw.write('%s\n' % ','.join(def_dic.values()))
	elif i == 7:
		fw.write('%s\n' % ','.join(rel_dic.values()))
	else:
		fw.write(fr[i])
