#python src/map_concept_dic_to_dev.py  dic/concept_dictionary_user.txt  dic/user_cat-to-dev_cat.txt   dic/concept_dictionary.txt
#Writen by Roja (23-02-17)
import sys

dic = {}

user_cat_dic = {}
tmp_dic = {}
fw = open(sys.argv[3], 'w')


for line in open(sys.argv[1]):
	lst = line.strip().split(',')
	key = lst[0] + ',' + lst[1]
	if key not in tmp_dic:
		tmp_dic[key] = lst[2]
	else:
		tmp_dic[key] = tmp_dic[key] + '#' + lst[2]
	


for line in open(sys.argv[2]):
	lst = line.strip().split('\t')
	user_cat_dic[lst[0]] = lst[1] #to get dev cat	

#for key in sorted(user_cat_dic):
#	print key + '\t' + user_cat_dic[key]

for line in open(sys.argv[1]):
	lst = line.strip().split(',')
	if lst[1] in user_cat_dic.keys():
		if lst[1] == 'n' and '+' not in lst[0]:
			key = lst[0] + ',n' 
		else:
			key = lst[0] + ',' + user_cat_dic[lst[1]]
			
		if key not in dic:
			dic[key] = lst[2]
		else:
			dic[key] = dic[key] + '#' + lst[2]
	else:
		key = lst[0] + ',' + lst[1]
		if key not in dic:
			dic[key] = lst[2]
		else:
			dic[key] = dic[key] + '#' + lst[2]



#for key in sorted(dic):
#	print key + ',' + dic[key]


for key in sorted(dic):
	fw.write('%s,%s\n' % (key, dic[key]))
