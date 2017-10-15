# python src/extract_template_info_for_user_csv.py Aja_se_xo_sAla_pahale_milI.user.csv  dic/user_template_dic.txt  dic/concept_dictionary_user.txt  dic/hindi_cat.txt  transform.txt > M1_user.csv
############################################

import sys,re,pdb

f = open(sys.argv[1], 'r') #User csv
fr = f.readlines()

f1 = open(sys.argv[2], 'r') #user_template_dic
fr1 = f1.readlines()

f2 = open(sys.argv[3], 'r') #concept_dictionary_user
fr2 = f2.readlines()

fw = open(sys.argv[5], 'w')

dic = {}
temp_dic = {}

for line in fr1:
	lst = line.strip().split('\t')
	if lst[0] not in temp_dic:
		if len(lst) != 5:
			print '%%%%%%%%%% Error in this line ', line.strip() + '%%%%%%%%%%'
			sys.exit()
		else:
			temp_dic[lst[0]] = lst[1] + '\t' + lst[2] + '\t' + lst[3] + '\t' + lst[4]
	else:
		print '%%%%%%%%%%  template repeated \t' , line.strip() + ' %%%%%%%%%%%'
		sys.exit()

#concept dictionary user
for line in fr2:
	lst = line.strip().split(',')
	dic[lst[0]] = lst[1]


hindi_cat_dic = {}
for line in open(sys.argv[4]): #hindi cat dic
	lst = line.strip().split(',')
	hindi_cat_dic[lst[0]] = lst[1]


temp_eng_key = [] 

def replace_a_pattern(var):
	a = var 
	pat = re.findall('{[^}]+}', a)
	if pat[0] in temp_dic.keys(): 
		val = temp_dic[pat[0]].split('\t')
		a = re.sub('{[^}]+}', val[1], a)
		temp_eng_key.append(val[2]) #yesterday
		fw.write('%s\t%s\n' %  (val[2], val[0])) #child
		fw.write('%s\t%s\n' %  (val[3], val[0])) #children
	else:
		print '%%%%%%%%%%%% Add your template ' + pat[0] + ' in user_template_dic.txt and then run sh compile.sh ' 
	return a


def replace_pattern_with_val(lst, dic_name):
	new_list = []
	for j in range(0, len(lst)):
		if j in dic_name.keys():
			new_list.append(dic_name[j])
		else:
			new_list.append(lst[j])
	return new_list


key = ''
key_dic = {}
for i in range(0, len(fr)):
	new_lst = []
	if i == 0: #chunk row
		lst = fr[i].strip().split(',')
		for j in range(0, len(lst)):
			if '{' in lst[j]:	
				key = replace_a_pattern(lst[j])
				key_dic[j] = key #Storing column info of construction pattern
				k = key.split('_')[0]
				new_lst.append(k+'_0')
			else:
				new_lst.append(lst[j])
		print ','.join(new_lst)
	elif i == 1: #lemma row
		if key == '':
			print fr[i].strip()
		else:
			if key not in dic.keys():
				print '%%%%%%%%%%% Add ' + key + ' in concept_dictionary_user.txt and run sh compile.sh'
				sys.exit()
			else:
				lst = fr[i].strip().split(',')
				new_lst = replace_pattern_with_val(lst, key_dic)
				print ','.join(new_lst)
	elif i == 3: #category row
		lst = fr[i].strip().split(',')
		l = replace_pattern_with_val(lst, key_dic)
		new_lst = replace_pattern_with_val(l, hindi_cat_dic) #Checking ladakA_1 in hindi_cat_dic 
		print ','.join(new_lst)	
	elif i == 5:#intrachunk rel row
		lst = fr[i].strip().split(',')
		if key == '':
			print fr[i].strip()
		else:
			lst = fr[i].strip().split(',')
			for each in lst:
				if '{' in each:
					new_lst.append('')
				else:
					new_lst.append(each)
			print ','.join(new_lst)	
	else:
		print fr[i].strip()
