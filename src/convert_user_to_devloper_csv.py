#Convert User Csv to Developer Csv:
#python src/convert_user_to_devloper_csv.py  output/$1.tmp3 dic/pronoun_lemma_dic.txt dic/new_tam_dic.csv  dic/link_list.txt prep_insertion.dat dic/hnd_pron_dic.txt  dic/cat_relation_mapping.txt output/replace_id.dat $2
#where $1 is input file name , $2 is output filename
#Written by Roja(14-11-16)
#######################################################################
import sys, pdb, re

f = open(sys.argv[1], 'r') #user csv file
fr = f.readlines()
fw = open(sys.argv[10], 'w') #dev csv file

pass_verb_f = open(sys.argv[9], 'r')
pass_verb_lst = pass_verb_f.readlines()

#################################################################
#Declarations:
chunk_dic = {}
pronoun_lemma_dic = {}
eng_lemma_dic = {}
ids_dic = {}
cat_dic = {}
def_dic = {}
gnp_dic = {}
tam_dic = {}
rel_dic = {}
cat_nd_rel_dic = {}
noun_noun_dic = {}
noun_verb_dic = {}
verb_verb_dic = {}
rel_link_dic = {}
prep_dic = {}
hnd_pron_dic = {}
modal_list = []
control_v_list = []
replace_id_lst = []
count = 0
flag = 0

#######################################################################
for line in open(sys.argv[2]): #pronoun dic
	lst = line.strip().split('\t')
	pronoun_lemma_dic[lst[0]] = lst[1]	

for line in open(sys.argv[3]): #tam dic
	lst = line.strip().split(',')
	tam_dic[lst[0]] = lst[1] + '\t' + lst[2] + '\t' + lst[3] + '\t' + lst[4] + '\t' + lst[5]

start = 0
for line in open(sys.argv[4]): #link_list dic
	lst = line.strip().split('\t')
	if '####noun-verb####' in line:
		start = 1
	elif '####noun-noun####' in line:
		start = 2
	elif '####verb-verb link####' in line:
		start = 3
	elif line[0] == '\n' or line[0] == '-':
		pass
	elif start == 1 :
		noun_verb_dic[lst[0]] = lst[1]
		rel_link_dic[lst[0]] = lst[1]  #as of now storing all rels in rel_link_dic and using this dic. If cat wise dic needed then comment this dic and modify the code to use noun_verb, noun_noun, verb_verb dics
	elif start == 2 :
		noun_noun_dic[lst[0]] = lst[1]
		rel_link_dic[lst[0]] = lst[1]
	elif start == 3:
		verb_verb_dic[lst[0]] = lst[1]
		rel_link_dic[lst[0]] = lst[1]

prep_count = 0	
for line in open(sys.argv[5]): #prep insertion facts
	prep_count += 1
	lst = line.strip().split()
	prep_dic[prep_count] = lst[1] + '\t' + lst[2] + '\t' + lst[3][:-1]

for line in open(sys.argv[6]): #hnd pron dic (note: created from pron dic)
	lst = line.strip().split('\t')
	hnd_pron_dic[lst[0]] = lst[1]
	
for line in open(sys.argv[7]): #based on rel modifying cat dic
	lst = line.strip().split(',')
	cat_nd_rel_dic[lst[0]+','+lst[1]] = lst[2]

for line in open(sys.argv[8]): #If there is any id to be replaced:
	lst = line.strip().split('\t')
	if lst != []:
		replace_id_lst.append(lst[1])
#######################################################################

dic_names = [
		chunk_dic,
		eng_lemma_dic,
		ids_dic,
	        cat_dic,
		def_dic,
		gnp_dic,
		rel_dic
	    ]		


def return_value(lst, dic):
	count = 1
	for each in lst:
		if count not in dic:
			if dic == rel_dic:
				if each != '':
					dic[count] = each#Not storing empty info in rel dics. If more than one rel in same col storing with '+'
			else:
				dic[count] = each 
		else:
			if dic == rel_dic:
				if each != '':
					dic[count] =  dic[count] + '+' + each #Not storing empty info in rel dics. If more than one rel in same col storing with '+'
			else:
				dic[count] = dic[count] +  each
		count += 1

for i in range(0, len(fr)):
	lst = fr[i].strip().split(',')
	#if  i != 0 and i != 3 and i != 5 and i != 7 and i != 8 :
	if  i != 6 and i != 7 and i != 8 :
		return_value(lst, dic_names[i])
	elif i == 6 :
		return_value(lst, dic_names[i])	
	elif i == 7:
		return_value(lst, dic_names[i-1])
	elif i == 8:
		return_value(lst, dic_names[i-2])

#######################################################################
#Storing propn info in cat dic:
for key in sorted(def_dic):
	#if def_dic[key] != 'yes':
	if def_dic[key] != 'def':
#		cat_dic[key] = def_dic[key]
		def_dic[key] = ''

#######################################################################
#Get lemma info for pronoun
def get_lemma_info(lemma, cat, gnp):
	gnp_lst = gnp[1:-1].split()
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

#######################################################################
#Get tam info
def get_tam_info(tam, col_no):
	if tam in tam_dic:
		tam_list =  tam_dic[tam].split('\t')
		if pred_adj_id_lst != []:
			for each in pred_adj_id_lst:
				pred_adj_h = each.split(':')
				if int(pred_adj_h[1]) == col_no:
					eng_lemma_dic[col_no] = ''
					cat_dic[col_no] = ''
					gnp_dic[int(pred_adj_h[0])] = tam_list[1] #Ex: kyA_Apa_[nArAjZa_hEM]_user.csv
		elif tam_list[2] != '':
			if tam_list[0] != '':
				eng_lemma_dic[col_no]  = eng_lemma_dic[col_no] + '_' + tam_list[0]   #storing eng tam info
			eng_lemma_dic[len(eng_lemma_dic)+1] = tam_list[2]
			cat_dic[len(cat_dic)+1] = tam_list[4]
			gnp_dic[col_no] = tam_list[1]
			gnp_dic[len(gnp_dic)+1] = tam_list[3]
			if tam_list[4] == 'modal':
				modal_verb_pres = str(len(cat_dic))
				key = str(col_no) + ':' + str(len(cat_dic))
				v_list.append(key)
				return modal_verb_pres
			else:
				rel_dic[col_no] = str(len(cat_dic)) + ':' + 'control_v'
		else:
			if tam_list[0] != '':
				eng_lemma_dic[col_no]  = eng_lemma_dic[col_no] + '_' + tam_list[0]   #storing eng tam info
			gnp_dic[col_no] = tam_list[1]	
			
	else:
		print '%%%%%%%%%%% Tam missing in dic. Please add tam "' + tam + '" and its equivalent in dic/tam_mapping.csv %%%%%%%%%%%%'
		sys.exit()

#######################################################################
pred_adj_id_lst = []
########################################################################

#Modifying categories based on relations:
for key in sorted(cat_dic):
	new_cat_key = ''
	if key in rel_dic:
		rel = rel_dic[key].split(':')
		if len(rel) != 1:
			new_cat_key = cat_dic[key] + ',' + rel[1]
	if new_cat_key in cat_nd_rel_dic.keys():
		cat_dic[key] = cat_nd_rel_dic[new_cat_key]
		if cat_dic[key] == 'pred_adj':
			pred_adj_id_lst.append(str(key) + ':' + rel[0]) #Storing child and head info of pred_adj


#Modifying category based on chunk:
for key in sorted(chunk_dic):
	if '-' in chunk_dic[key] and cat_dic[key] == 'v':
		tam = chunk_dic[key].split('-')	
		if tam[1]+'\n' in pass_verb_lst:
			cat_dic[key] = 'pass_v'

#######################################################################
#before proceeding into lemma insertions , cat insertions get dics in order.
#ex: if cat of any wrd is not present storing as ''. (Ex: kyA)
def get_values_in_order(dic):
	for key in sorted(ids_dic):
		if key not in dic:
			dic[key] = ''


get_values_in_order(eng_lemma_dic)
get_values_in_order(cat_dic)
get_values_in_order(def_dic)
get_values_in_order(gnp_dic)
get_values_in_order(rel_dic)

##############################################################################################
new_rel = '' 

for each in sorted(ids_dic):
	#so_rahe_ho_kyA ? (here in this ex. there is no pron.. so getting pron info from gnp of 'v')
	if cat_dic[each] == 'v' and gnp_dic[each] != '': 
		h_key = 'pron' + ',' + gnp_dic[each]
		lem = hnd_pron_dic[h_key]  #To get hindi pronoun
		out = get_lemma_info(lem, 'pron', gnp_dic[each])  #To get english pronoun
		eng_lemma_dic[len(eng_lemma_dic)+1] = out
		cat_dic[len(cat_dic)+1] = 'pron'
		gnp_dic[len(gnp_dic)+1] = gnp_dic[each]
		new_rel = str(len(eng_lemma_dic))  + ':' + str(each) + ':ARG1/NEQ'

##############################################################################################
		
#for key in cat_dic:
#	print key, '$$$$$', cat_dic[key]


##############################################################################################
prep_lst = []
for key in sorted(prep_dic):
	p = prep_dic[key].split('\t')
	c = int(p[2])
	if cat_dic[c] != 'poss_propn' and cat_dic[c] != 'poss_pron' and cat_dic[c] != 'place_adv' and cat_dic[c] != 'time_adv' and cat_dic[c] != 'wh-word' and cat_dic[c] != 'poss_n':
		ids_dic[len(ids_dic)+1] = len(ids_dic)+1
		eng_lemma_dic[len(eng_lemma_dic)+1] = p[0]
		cat_dic[len(cat_dic)+1] = 'p'
		gnp_dic[len(gnp_dic)+1] = ''
		prep_lst.append(str(len(ids_dic)+1) + ':' + p[0] + ':' + p[1] + ':' + p[2])

##############################################################################################
v_list = []
rel_lst = []
new_rel_lst = []

def replace_head_id(rel, head_id, replace_id):
	a = rel
	var = head_id + ':' 
	var1 = replace_id + ':'
	if var in a:
		a = re.sub(var, var1, a)
	return a	
	
def check_replace_head_id(rel, head_id, replace_id):
	rel_id = rel.split(':')
	if rel_id[0] == head_id:
		out = replace_head_id(rel, rel_id[0], replace_id)
		if out != None:
			return out
		else:
			return rel
	else:
		return rel
	
def check_each_rel(lst, rel):
	for item in lst:
		rep_id = item.split(':')
		if rel == '': #kyA
			new_rel_lst.append('')
		elif '-' in rel: #Ex: 2:ARG1/EQ-poss_pron-1:ARG2/NEQ
			r = []
			rel_lst = rel.split('-')
			for each in rel_lst:
				if ':' in each:
					out = check_replace_head_id(each, rep_id[1], rep_id[0])
					r.append(out)
				else:
					r.append(each)
			new_rel_lst.append('-'.join(r))
		else:
			out = check_replace_head_id(rel, rep_id[1], rep_id[0])
			new_rel_lst.append(out)
 
##############################################################################################
not_present = 0
last_item = ''

#To get Developer CSV::
#####################
for i in range(0, len(fr)):
	if i == 0:
		lst = fr[i].strip().split(',')
		last_item = lst[len(lst)-1]
		for j in sorted(chunk_dic):
			if j in cat_dic:
				if cat_dic[j] == 'v' or cat_dic[j] == 'pass_v': #rAma mAra_gayA
					if '-' in chunk_dic[j]: #Tam info separated from root by '-'
						tam_list = chunk_dic[j].split('-') 
						if len(tam_list) >= 2:
						 	mv = get_tam_info(tam_list[1], j)
							modal_verb_pres = mv

#		fw.write(fr[i])
		fw.write('%s\n' % ','.join(chunk_dic.values()))
	if i == 1:
		print ','.join(eng_lemma_dic.values())
		fw.write('%s\n' % ','.join(eng_lemma_dic.values()))
	if i == 2:
		#print ','.join(map(str, eng_lemma_dic.keys()))
		fw.write('%s\n' % ','.join(map(str, eng_lemma_dic.keys())))
	if i == 3:
		fw.write('%s\n' % ','.join(cat_dic.values()))
	if i == 4:
		fw.write('%s\n' % ','.join(def_dic.values()))
	if i == 5:
		get_values_in_order(gnp_dic)
		fw.write('%s\n' % ','.join(gnp_dic.values()))
		if len(tam_list) >= 2:
			if tam_list[1] == 'ie' or tam_list[1] == '0' or tam_list[1] == 'o' or tam_list[1] == 'iegA' :
				fw.write('comm,' + '\n')
			elif last_item == '.' or last_item == '|':
				fw.write('prop,' + '\n')
			elif last_item == '?':
				fw.write('ques,' + '\n')
	if i == 7:
		new_lst = []
		lst = fr[i].strip().split(',')
		#To pick implicit relations
		 
		for key in sorted(eng_lemma_dic):
		    if key not in rel_dic:
			rel_lst.append('')
		    else:
			l = rel_dic[key].split('+')
			for item in l:
				rel = item.split(':')
				if rel[0] == '':
					rel_lst.append('')
				else:
						if cat_dic[key] == 'det':
							rel_lst.append(rel[0] + ':') #Ex: 3.1:det Apane_upanyAsa_yaha_vinxu_waka_paDzA_hE_user.csv
						elif rel[1] == 'vAkya-viSeRaNa':
							if modal_verb_pres != None:
								r = modal_verb_pres + ':' + rel_link_dic[rel[1]]
							else:
								r = rel[0] + ':' + rel_link_dic[rel[1]]
							rel_lst.append(r)	
						elif rel[1] in rel_link_dic:
							rel_lst.append(rel[0] + ':' + rel_link_dic[rel[1]])
						elif rel[1] == 'r6': #Ex:[rAma_kA_betA]_vixyAlaya_meM_paDawA_hE
							r = rel[0] + ':ARG1/EQ-' + cat_dic[key] + '-' +  str(key) + ':ARG2/NEQ'
							rel_lst.append(r)
						elif rel[1] == 'comp_n': #Ex: i_went_to_the_[bus_stop].csv
							r = str(key) + ':ARG1/EQ-comp_n-' + str(key) + ':ARG2/NEQ'
							rel_lst.append(r)
						else:
							print '%%%%%%%%%%% relation mapping missing in dic. Please add mapping for  "' + rel[1] + '" and its equivalent in dic/link_list.txt %%%%%%%%%%%%'	
							sys.exit()
		################################################################################################
#		To get prepositions rels:
		for each in prep_lst:
			prep_id = each.split(':') #To get prep id and head id Ex: kamare_meM

			#to print prep rel 
			value = prep_id[2] + ':ARG1/EQ-' + prep_id[1] + '-' + prep_id[3] + ':ARG2/NEQ' 

			for k in range(0, len(rel_lst)):
				if int(prep_id[0]) <= len(rel_lst):
					rel_lst[int(prep_id[0])-2] =  value
				else:
					rel_lst.append('')
			rel_lst[int(prep_id[3])-1] = ''

		################################################################################################
		for each in v_list: #To get modal verb info:
			v = each.split(':')
			for key in sorted(eng_lemma_dic):
				if eng_lemma_dic[key] == 'not' and cat_dic[key] == 'neg':
					not_present = 1
					not_id = key   #Storing id of 'not' . Using this id to add relation b/w modal verb and not.
			if len(rel_lst) > int(v[0])-1:
				rel_lst[int(v[0])-1] = v[1] + ':ARG1/H'  #main verb and modal verb 
				if not_present == 1: 
					rel_lst[not_id-1] = v[1] + ':ARG1/H'   #Assuming previous word of modal verb is 'not'
					not_present = 0
			else:
				rel_lst.append(v[1] + ':ARG1/H') #main verb and modal verb
				if not_present == 1: 
					rel_lst.append(v[1] + ':ARG1/H')   #Assuming previous word of modal verb is 'not'
					not_present = 0
		
		##############################################################################################
		#Replacing head id if head id is in pred_adj_id_lst
		for each in rel_lst:
			if pred_adj_id_lst != []: #Ex: kyA_Apa_nArAjZa_hEM_user.csv
				check_each_rel(pred_adj_id_lst, each)
			elif replace_id_lst != []:
				check_each_rel(replace_id_lst, each)
			else: 
				new_rel_lst = rel_lst

		##############################################################################################
#		#using new_rel:
		r = new_rel.split(':')
		if len(r) > 1:
			while len(rel_lst) < int(r[0]):
				rel_lst.append('')
			rel_lst[int(r[0])-1] = r[1] + ':' + r[2]
		##############################################################################################

		fw.write('%s\n' % ','.join(new_rel_lst))
