#Programme to print dmrs node info from CHL input
#Written by Roja 10/09/16
###################################################3
import pdb
import sys, os
import re
index = 10000
count = 0

eng_cat_dic = {}
eng_lemma_dic = {}
hnd_gnp_dic = {}
sent_type_dic = {}
head_child_dic = {}
eng_rel = {}
node_id_key_dic = {}
id_node_dic = {}
conj_comp_dic = {}
id_nodes_dic = {}
quant_ins_dic = {}
prep_ins_dic = {}
template_info_dic = {}
noun_quant_info = {}
template_dic = {}
buf = []

fdebug = open(sys.argv[11], 'w')

###################################################################################################
#Arg list:
dic_names = [
	eng_cat_dic,		#Get eng wrd cat info 
	eng_lemma_dic,		#Get eng lemma info
	None,
	sent_type_dic,		#Get sentence type info
	None,
	quant_ins_dic,		#Get quants inserted info
	None,
	template_info_dic,	#Get additional template info used
	noun_quant_info		#Get quantifier present for a noun or not
	]

#Function to store data into dictionaries:
def store_date_into_dic(filename, dic_name):
	for line in filename:
		lst = line.strip().split('\t')
		dic_name[float(lst[1])] = lst[2][:-1]
	

for i in range(0, len(dic_names)):
	if i != 2 and i != 4 and i != 6:
		store_date_into_dic(open(sys.argv[i+1], "r"), dic_names[i])
	
####################################################################################################
#Get gnp info and  tense info  
for line in open(sys.argv[3]):
	lst = line.strip().split('\t')
	if len(lst) >=4:
		lst[4] = lst[4][:-1]
		if lst[4] == 'u':
			lst[4] = '1'
		if lst[4] == 'm':
			lst[4] = '2'
		if lst[4] == 'a':
			lst[4] = '3'
		hnd_gnp_dic[int(lst[1])] = lst[2] + '\t' + lst[3] + '\t' + lst[4]
###################################################################################################
#To get eng rels:
for line in open(sys.argv[5]):
	lst = line.strip().split('\t')
	relhid = lst[1] + '\t' + lst[2]
	if relhid not in eng_rel:
		eng_rel[relhid] = lst[3][:-1]
	else:
		eng_rel[relhid] = eng_rel[relhid] + '\t' + lst[3][:-1]
	if lst[2] not in head_child_dic:
		head_child_dic[lst[2]] = lst[3][:-1]
	else:
		head_child_dic[lst[2]] = head_child_dic[lst[2]] + '\t' + lst[3][:-1]
###################################################################################################
#To get prep inserted info:
for line in open(sys.argv[7]):
	lst = line.strip().split('\t')
	prep_ins_dic[float(lst[1])] = lst[2] + '\t' + lst[3][:-1]
###################################################################################################
#To get templates info:
for line in open(sys.argv[10]):
	lst = line.strip().split('\t')
	template_dic[lst[0]] = lst[1]	
###################################################################################################
#Function to print nodeid in node and link field
star_list = []
head_reverse_node_id = []
head_reverse_key = []
def print_nodeid_in_node_nd_link(fname, index, key):
	node_link_lst = []
	f = open(fname, 'r')
	fr = f.readlines()
	for line in fr:
		a = line.strip()
		if '?1+1' in line:
			var = index+1
			a=re.sub("\?1\+1", str(var), a)
			node_id_key_dic[var] = key
		if '?1+2' in line:
			var = index+2
			a=re.sub("\?1\+2", str(var), a)
			node_id_key_dic[var] = key
		if '?1+3' in line:
			var = index+3
			a=re.sub("\?1\+3", str(var), a)
			node_id_key_dic[var] = key
		if '?1+4' in line:
			var = index+4
			a=re.sub("\?1\+4", str(var), a)
			node_id_key_dic[var] = key
		if '?1-1' in line:
			var = index-1
			a=re.sub("\?1\-1", str(var), a)
		if '"?1"' in line:
			var = index
			a=re.sub("\?1", str(var), a)
			node_id_key_dic[var] = key
		if a[0] == '*':
			star_list.append(var) #Storing head nodeid
#			print star_list
			a = a[1:]
			id_nodes_dic[key] = var
		if 'loc_nonsp' in line or 'unspec_manner' in line:
			head_reverse_node_id.append(var) #Storing node id where head need to be reverse
			head_reverse_key.append(str(int(key)))
		node_link_lst.append(a)
	f.close()	
	return node_link_lst
###################################################################################################
#get lemma, gnp info, verb info:
lemma_gnp_info_lst = []
def print_lemma_nd_gnp_info(line, lemma, gnp_info):
	lemma_gnp_info_lst = []
	if gnp_info != '':
		if gnp_info[0] == '-':
			perf = '-'
		if gnp_info[0] == '+':
			perf = '+'
		if gnp_info[1] == '-':
			prog = '-'
		if gnp_info[1] == '+':
			prog = '+'
		if gnp_info[2] == '-':
			tense = 'untensed'
		else:
			tense = gnp_info[2]
	else:
		perf = ''
		prog = ''
		sf = ''
		tense = ''
		sf = ''
	if '-' in lemma: #Ex: bus-stop (compound noun)
		lem_lst = lemma.split('-')
   	for i in range(0, len(line)):
#		a = each.strip()
		a = line[i].strip()
		if 'gend="?"' in a:
			var = 'gend="' + gnp_info[0] + '"'
			a = re.sub('gend="\?"', var, a)
		if 'num="?"' in a:
			var = 'num="' + gnp_info[1] + '"'
			a = re.sub('num="\?"', var, a)
		if 'pers="?"' in a:
			var = 'pers="' + gnp_info[2] + '"'
			a = re.sub('pers="\?"', var, a)
		if 'lemma="?"' in a:
			if '-' in lemma: #Ex: bus-stop (compound noun)
				var = 'lemma="' + lem_lst[0] + '"'
				del lem_lst[0]
			else:
				var = 'lemma="' + lemma + '"'
			a = re.sub('lemma="\?"', var, a)
		if 'perf="?"' in a:
			if perf == '':
				var = ''
			else:
				var = 'perf="' + perf + '"'
			a = re.sub('perf="\?"', var, a)
		if 'prog="?"' in a:
			if prog == '':
				var = ''
			else:
				var = 'prog="' + prog + '"'
			a = re.sub('prog="\?"', var, a)
		if 'tense="?"' in a:
			if tense == '':
				var = ''
			else:
				var = 'tense="' + tense + '"'
			a = re.sub('tense="\?"', var, a)
		if 'sf="?"' in a:
			if perf == '' and prog == '' and tense == '': 
				var = ''
			else:
				var = 'sf="' + sent_type_dic[1] + '"'
			a = re.sub('sf="\?"', var, a)
		if '&quot;?&quot;' in a:
#		if 'carg="?"' in a:
			var = '&quot;' + lemma + '&quot;'
#			var = 'carg="' + lemma + '"'
			a = re.sub('&quot;\?&quot;', var, a)
#			a = re.sub('carg="\?"', var, a)
		if 'pos="?"' in a:
			var = 'pos="' + gnp_info[3] + '"'
			a = re.sub('pos="\?"', var, a)
		lemma_gnp_info_lst.append(a)
	return lemma_gnp_info_lst
###################################################################################################
#get head and child nodes interchange
def reverse_head_nd_child(line, child):
	if 'from="' in line:
		from_id = re.findall(r'\d+', line)
		var = 'from="' + str(child) + '"'
		line = re.sub('from="(\d+)"', var, line)
		var1 = 'to="' + from_id[0] + '"'
		line = re.sub('to="\d+"', var1, line)
	return line
###################################################################################################
#Fill rel info:
def fill_rel_info(head, child, lst):
	new_lst = []
	for each_rel in eng_rel:
#		print eng_rel[each_rel], child
		child_info =  eng_rel[each_rel].split('\t')
		for each_child in child_info:
#			print each_child, child
			if each_child == str(child):
				rel_info = each_rel.split('\t')
#				print head, child, rel_info, 
				if rel_info[1] == str(head):
					eng_rel_info =  rel_info[0].split('/')
					for line in lst:
						a= line.strip()
						if '<rargname>?<' in line:
							var = '<rargname>' + eng_rel_info[0] + '<'
							a = re.sub('<rargname>\?<', var, a)
						if '<post>?</post>' in line:
							var = '<post>' + eng_rel_info[1] + '<'
							a = re.sub('<post>\?<', var, a)
						new_lst.append(a)
			if each_child == str(head):
				rel_info = each_rel.split('\t')
				if rel_info[1] == str(child):
					eng_rel_info =  rel_info[0].split('/')
#					print child, rel_info[1], eng_rel_info, lst
					for line in lst:
						a= line.strip()
						if '<rargname>?<' in line:
							var = '<rargname>' + eng_rel_info[0] + '<'
							a = re.sub('<rargname>\?<', var, a)
						if '<post>?</post>' in line:
							var = '<post>' + eng_rel_info[1] + '<'
							a = re.sub('<post>\?<', var, a)
						new_lst.append(a)
	return new_lst


###################################################################################################
#get ids for conj components:
def get_node_ids_for_conj_comp(lst, comp_list):
	a = []
	for i in range(0, len(lst)):
		line = lst[i]
#		print line
		if 'L-INDEX' in line or 'L-HNDL' in line:
			var = 'to="' + comp_list[0] + '"'
			line = re.sub('to="\?"', var, line)
		if 'R-INDEX' in line or 'R-HNDL' in line:
			var = 'to="' + comp_list[1] + '"'
			line = re.sub('to="\?"', var, line)
		a.append(line)
	return a
###################################################################################################
#Func to fill 'to' id:
def fill_to_id_info(lst, index):
	for i in range(0, len(lst)):
		if ' to="?' in lst[i]:
			var = ' to="' + str(index) + '"'
			a = re.sub(' to="\?"', var, lst[i])
#			print '**', a
			buf.append(a)
		else:
#			buf.append(lst[i])
			print lst[i].strip()
###################################################################################################
#func to fill rel and to id info in verbs:
def fill_to_id_nd_rel_in_verb(lst):
	node_lst = []
	link_lst = []
	link1_lst = []
	for i in lst:
		if '<node ' in i:
			node_lst.append(i)
		else:
			if head_child_dic.keys() == []: #Come in. When there are no relations.
				if '?' not in i:
					print i
			else:
				if '?' not in i:
					if i not in link_lst:
						link_lst.append(i)
				else:
					if i not in link1_lst:
						link1_lst.append(i)
	for each in head_child_dic:
		child = head_child_dic[each].split('\t')
		for c in child:
			if c not in link_decided_lst:#if verb link is decided in child then not considering it
				if int(each) == int(key) and c != each: #In csv same id linkages are also given ..so to avoid adding c != each
					out2 = fill_rel_info(int(key), int(c), link1_lst)
					if out2 != None:
						fill_to_id_info(out2, int(c))
	print '\n'.join(node_lst)
	print '\n'.join(link_lst)
###################################################################################################

#Declarations::
poss_pronouns = ['her', 'hers', 'his', 'their', 'mine', 'yours', 'its', 'ours',  'our', 'my']
poss_pronouns_without_gen_num = ['your']
pred_adj = []
link_decided_lst = []
sent_type_decided = [] 
###################################################################################################
#Count no: of nodes in a template:
def count_no_of_nodes(template):
	count = 0
	f = open(template, 'r')
	fr = f.readlines()
	for line in fr:
		if '<node ' in line:
			count += 1
	return count
###################################################################################################
def load_template(template, index, key, gnp_lst):
	lst = []
	out = print_nodeid_in_node_nd_link('templates/' + template, index, key)
	out1 = print_lemma_nd_gnp_info(out, eng_lemma_dic[key], gnp_lst)
	fdebug.write('(id-template_info' + '\t' + str(int(key)) + '\t' + 'templates/' + template + ')\n')
	cn = count_no_of_nodes('templates/' + template)
	index = index + cn
	lst.append(out1)
	lst.append(index)
	return lst
###################################################################################################
#First checking user defined templates available for the lemma given::
prov_def = []
for key in sorted(eng_lemma_dic):
	#To get gnp info into a list
	if key in hnd_gnp_dic:
		gnp_lst = hnd_gnp_dic[key].split('\t')
		if gnp_lst[2] == '-':
			gnp_lst[2] = '3' #Considering '3' person as default
	else:
		gnp_lst=''
	user_template = eng_lemma_dic[key] + '_' + 'user_defined_template.txt'
	if os.path.isfile('provisional_templates/' + user_template):
		out = print_nodeid_in_node_nd_link('provisional_templates/' + user_template, index, key)
		out1 = print_lemma_nd_gnp_info(out, eng_lemma_dic[key], gnp_lst)
		prov_def.append(key)
		if filter(lambda x: '?' in x, out1)  == []: #To check whether '?' present in any item of the list #
			buf.append('\n'.join(out1))         #Ex: Do you know any [nursery-rhyme] ?
		else:
			for each_id in eng_rel:
				rel_id =  each_id.split('\t')
				child = eng_rel[each_id]
				child_lst = child.split('\t')
	#			print child_lst 
				for each in child_lst:
	#				print '^^', key, each, each_id
					if int(key) == int(each): #If template is not verb
						fill_to_id_info(out1, rel_id[1])
					if key == int(rel_id[1]): #If template is verb
						out2 = fill_rel_info(int(rel_id[1]), int(each), out1)
						fill_to_id_info(out2, child)
	
		fdebug.write('(id-template_info' + '\t' + str(int(key)) + '\t' + 'provisional_templates/' + user_template + ')\n')
		c = count_no_of_nodes('provisional_templates/' + user_template)
		index = index + c
###################################################################################################
#Print dmrs info::
#get node and link info for each cat
#----------------------------------
for key in sorted(eng_cat_dic):
   flag = 0
   cat = []
   if key not in prov_def:
	cat = eng_cat_dic[key].split()
	#To get gnp info into a list
	if key in hnd_gnp_dic:
		gnp_lst = hnd_gnp_dic[key].split('\t')
		if gnp_lst[2] == '-' and cat[0] != 'v':
			gnp_lst[2] = '3' #Considering '3' person as default
	elif cat[0] == 'sent_conj':
		c_index = head_child_dic[str(int(key))].split('\t')
		gnp_lst = hnd_gnp_dic[float(c_index[0])].split('\t') #Checking L-index Gnp and passing it to 'sent_conj'
	else:
		gnp_lst=''
	###################################################################################################
	#for i in range(0, len(cat_list)):
	for i in sorted(template_dic):
		if cat[0] == i:
			output = load_template(template_dic[i], index, key, gnp_lst)
			out1 = output[0]
			index = output[1]
			if filter(lambda x: '?' in x, out1)  == []: #To check whether '?' present in any item of the list #
				buf.append('\n'.join(out1))         #Ex: Do you know any [nursery-rhyme] ?
			else:			
				if cat[0] == 'modal' or cat[0] == 'pass_v' or cat[0] == 'causative' or cat[0] == 'pred_adj':
					fill_to_id_nd_rel_in_verb(out1) #[Can] you return the books?
				elif cat[0] == 'noun_conj' or cat[0] == 'sent_conj' or cat[0] == 'reason_conj':
					for c in head_child_dic:
						if str(int(key)) == c:
							c_index = head_child_dic[c].split('\t')
							out2 = get_node_ids_for_conj_comp(out1, c_index)
							buf.append('\n'.join(out2))
				else:
					for each in head_child_dic:
						#head_child_dic[c] == str(int(key)) and c != head_child_dic[c]
						if each == str(int(key)): #Had you not gone to play yesterday.
							child = head_child_dic[each].split('\t')
							for c in child:
								if c not in link_decided_lst and c != each and each not in link_decided_lst:
									out2 = fill_rel_info(each, c, out1) #I walk slowly.
									fill_to_id_info(out2, c)
									link_decided_lst.append(each)
		#	Commented above condition for sent : It does not work properly.
						elif str(int(key)) in head_child_dic[each] and each != head_child_dic[each]: #Can you lend me [100] rupees?
							if str(int(key)) not in link_decided_lst:
								out2 = fill_rel_info(each, str(int(key)), out1) #He had a new pen.
								fill_to_id_info(out2, each)
        	                                		link_decided_lst.append(str(int(key))) #Ex: Please shut the door.

			flag = 1
	###################################################################################################
	if flag == 0:		
		#get pronoun info::
		if cat[0] == 'pron':
			#To get possesive pronoun info without gen and num info::
			if eng_lemma_dic[key] in poss_pronouns_without_gen_num:
				output = load_template('poss_pron_without_gen_num.txt', index, key, gnp_lst)
				out1 = output[0] 
				index = output[1]
				for c in head_child_dic:
					if head_child_dic[c] == str(int(key)) and c != head_child_dic[c]:
						fill_to_id_info(out1, c)
			###################################################################################################
			#To get	possesive pronoun info::
			elif eng_lemma_dic[key] in poss_pronouns:
				output = load_template('possesive_pronoun.txt', index, key, gnp_lst)
				out1 = output[0]
				index = output[1]
				buf.append('\n'.join(out1))
			###################################################################################################
			#To get pronoun info without gen::
			elif  eng_lemma_dic[key] == 'I' or eng_lemma_dic[key] == 'we' or eng_lemma_dic[key] == 'they':
				output = load_template('pronoun_without_gen.txt', index, key, gnp_lst)
				out1 = output[0]
				index = output[1]
				buf.append('\n'.join(out1))
			###################################################################################################
			#To get pronoun info without gen and num::
			elif  eng_lemma_dic[key] == 'you':
				output = load_template('pronoun_without_gen_num.txt', index, key, gnp_lst)
				out1 = output[0]
				index = output[1]
				buf.append('\n'.join(out1))
			###################################################################################################
			#To get pronoun info of this, that, those and these
			elif  eng_lemma_dic[key] == 'this' or eng_lemma_dic[key] == 'that' or eng_lemma_dic[key] == 'those' or eng_lemma_dic[key] == 'these':
				output = load_template('this_that_pron.txt', index, key, gnp_lst)
				out1 = output[0]
				index = output[1]
				buf.append('\n'.join(out1))
			###################################################################################################
			else:
				output = load_template('pronoun.txt', index, key, gnp_lst)
				out1 = output[0]
				index = output[1]
				buf.append('\n'.join(out1))
		###################################################################################################
		elif cat[0] == 'poss_propn':
			output = load_template('poss-propn.txt', index, key, gnp_lst)
			out1 = output[0]
			index = output[1]
			for c in head_child_dic:
	#			print c , head_child_dic[c]
				if head_child_dic[c] == str(int(key)) and c != head_child_dic[c]:
	                                fill_to_id_info(out1, c)
		###################################################################################################
		elif cat[0] == 'poss_pron':
			if eng_lemma_dic[key] == 'you':
				output = load_template('poss_pron_without_gen_num.txt', index, key, gnp_lst)
			elif  eng_lemma_dic[key] == 'I' or eng_lemma_dic[key] == 'we' or eng_lemma_dic[key] == 'they':
				output = load_template('poss_pron_without_gen.txt', index, key, gnp_lst)
			else:
				output = load_template('possesive_pronoun.txt', index, key, gnp_lst)
			out1 = output[0]
			index = output[1]
			for c in head_child_dic:
				each = head_child_dic[c].split('\t') #My teacher's son is a doctor.
				for item in each:
					if item == str(int(key)) and c != item:
						fill_to_id_info(out1, c)
		###################################################################################################
		elif cat[0] == 'poss_n':
			output = load_template('poss_noun.txt', index, key, gnp_lst)
			out1 = output[0]
			index = output[1]
			for c in head_child_dic:
				if head_child_dic[c] == str(int(key)) and c != head_child_dic[c]:
					fill_to_id_info(out1, c)
		###################################################################################################
		elif cat[0] == 'refl_pron':
			if eng_lemma_dic[key] == 'you':
				output = load_template('reflexive_pronoun_without_gen_num.txt', index, key, gnp_lst)
			elif eng_lemma_dic[key] == 'I' or eng_lemma_dic[key] == 'we' or eng_lemma_dic[key] == 'they':
				output = load_template('reflexive_pronoun_without_gen.txt', index, key, gnp_lst)
			else:
				output = load_template('reflexive_pronoun.txt', index, key, gnp_lst)
			out1 = output[0]
			index = output[1]
			for c in head_child_dic:
					each = head_child_dic[c].split('\t')
					for item in each:
						if item == str(int(key)) and c != item:
							fill_to_id_info(out1, c)
		###################################################################################################
		#To get noun info::
		elif cat[0] == 'n':
			#To get noun with quantifier info
			if key in noun_quant_info:
				output = load_template('noun_with_quant.txt', index, key, gnp_lst)
				out1 = output[0]
				index = output[1]
				buf.append('\n'.join(out1))
			###################################################################################################
			#To get noun without quantifier info
			else:
				output = load_template('noun_without_quant.txt', index, key, gnp_lst)
				out1 = output[0]
				index = output[1]
				buf.append('\n'.join(out1))
		###################################################################################################
		#To get verb info::
		elif eng_cat_dic[key] == 'v':
			flag = 0
			if sent_type_dic[1] == 'comm' and gnp_lst != '': #Let me [get] the money. Here get has no GNP info.
				output = load_template('imperative.txt', index, key, gnp_lst)
				sent_type_decided.append(sent_type_dic[1])
			else: 
				output = load_template('verb.txt', index, key, gnp_lst)
			out1 = output[0]
			index = output[1]
			fill_to_id_nd_rel_in_verb(out1)
		###################################################################################################
		#To get quantifiers info (excluding "this, "that" and "many"::
		elif eng_cat_dic[key] == 'det':
			gnp_lst = ''
			if eng_lemma_dic[key] == 'this' or eng_lemma_dic[key] == 'that' or eng_lemma_dic[key] == 'these' or eng_lemma_dic[key] == 'those':
				output = load_template('this_that_dem.txt', index, key, gnp_lst)
			else:
				output = load_template('quant.txt', index, key, gnp_lst)
			out1 = output[0]
			index = output[1]
			if key in quant_ins_dic: #Had you eaten [the bread]?
				fill_to_id_info(out1, int(quant_ins_dic[key]))
			else:
				for each in head_child_dic:
					child = head_child_dic[each].split('\t')
					if str(int(key)) in child:
						fill_to_id_info(out1, int(each)) #Rama is reading [a letter]
		###################################################################################################
		#To get preposition info::
		elif eng_cat_dic[key] == 'p':
			if gnp_lst == '':
				output = load_template('preposition.txt', index, key, gnp_lst)
			elif sent_type_dic[1] in sent_type_decided:
				output = load_template('preposition_with_TAM.txt', index, key, gnp_lst)
			elif sent_type_dic[1] not in sent_type_decided:
				if sent_type_dic[1] == 'comm' and gnp_lst != '': #Do not be [in] a hurry
					output = load_template('imperative_preposition.txt', index, key, gnp_lst)
			out1 = output[0]
			index = output[1]
			if key in prep_ins_dic:
				head_child = prep_ins_dic[key].split('\t')
				for i in range(0, len(out1)):
					a = out1[i].strip()
					if 'ARG1' in a:
						var = 'to="' + head_child[0] + '"'
						a = re.sub('to="\?"', var, a)
					if 'ARG2' in a:
						var = 'to="' + head_child[1] + '"'
						a = re.sub('to="\?"', var, a)
					buf.append(a)
			else:
				fill_to_id_nd_rel_in_verb(out1)
		###################################################################################################
		elif eng_cat_dic[key] == 'wh-word':
			if eng_lemma_dic[key] == 'how':
				output = load_template('how.txt', index, key, gnp_lst) 
			elif eng_lemma_dic[key] == 'why':
				output = load_template('why.txt', index, key, gnp_lst) 
			elif eng_lemma_dic[key] == 'where':
				output = load_template('where.txt', index, key, gnp_lst) 
			elif eng_lemma_dic[key] == 'what':
				output = load_template('what.txt', index, key, gnp_lst) 
			elif eng_lemma_dic[key] == 'which':
				output = load_template('which.txt', index, key, gnp_lst) 
			else: 
				output = load_template('when.txt', index, key, gnp_lst) 
			out1 = output[0]
			index = output[1]
			if filter(lambda x: '?' in x, out1)  == []: #To check whether '?' present in any item of the list #
				buf.append('\n'.join(out1))         
			else:
				#print out1
				for c in head_child_dic:
				#print c, head_child_dic[c], key, head_reverse_node_id 
					if '\t' in head_child_dic[c]:
						lst = head_child_dic[c].split('\t')
						if str(int(key)) in lst:
							fill_to_id_info(out1, c)
							if str(int(key)) not in head_reverse_key:
								link_decided_lst.append(str(int(key)))
					elif head_child_dic[c] == str(int(key)):
						fill_to_id_info(out1, c)
						if str(int(key)) not in head_reverse_key:
							link_decided_lst.append(str(int(key)))
		
###################################################################################################
##Print node_id_key dic::
#for key in node_id_key_dic:
#        print key, node_id_key_dic[key]

###################################################################################################
##Get id and node info 
for node in node_id_key_dic:
        if node_id_key_dic[node] in id_node_dic :
                if node in star_list and node_id_key_dic[node] not in quant_ins_dic:
                        id_node_dic[int(node_id_key_dic[node])] = node
        else:
		if node_id_key_dic[node] not in quant_ins_dic:
	                id_node_dic[int(node_id_key_dic[node])] = node

###################################################################################################
##Print id_node dic::
new_buf = []
for line in buf:
	flag = 0
	lst = line.split('\n')
	for each in lst:
		if '<node' in each:
			if each not in new_buf:
				new_buf.append(each)
		else:
			to_id = re.findall(r'\d+', each)
			if len(to_id[1]) == 1:
				var = ' to="' + to_id[1] + '"'
				if var in each:
					var1 = ' to="' + str(id_node_dic[int(to_id[1])]) + '"'
					each = re.sub(var, var1, each)
					if id_node_dic[int(to_id[1])] in head_reverse_node_id: #loc_nonsp
						out = reverse_head_nd_child(each, id_node_dic[int(to_id[1])])
						if out!= None:
							new_buf.append(out)
					else:
						new_buf.append(each)
				else:
					if each not in new_buf and '?' not in each:
						new_buf.append(each)
			else:
#				print id_node_dic[int(to_id[1])]
				if each not in new_buf :
					new_buf.append(each)
print '\n'.join(new_buf)							 

###################################################################################################
