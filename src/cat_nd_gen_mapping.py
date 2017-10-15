#Programme to modify cat and GNP as required by Developer Csv
#Written by Roja (10-12-16)
#RUN:: python src/cat_nd_gen_mapping.py  <User-CSV>  dic/user_cat-to-dev_cat.txt > output/<User-CSV>.tmp
#EX::  python src/cat_nd_gen_mapping.py  I_saw_2_tigers_user.csv dic/user_cat-to-dev_cat.txt
##################################################################
import sys, re

f = open(sys.argv[1], 'r')
fr = f.readlines()

cat_dic = {}
hnd_pron_dic = {}
lem_lst = []
cat_list = []
gnp_lst = []
rel_lst = []
rel_lst1 = []
rel_lst2 = []

####################################################
#using user_cat to dev_cat mapping dic:
for line in open(sys.argv[2]):
	lst = line.strip().split('\t')
	cat_dic[lst[0]] = lst[1]

####################################################
#Using hindi pronoun dic :
for line in open(sys.argv[3]):
	lst = line.strip().split('\t')
	hnd_pron_dic[lst[0]] = lst[1]
	
####################################################
#Function to check whether GNP in pronoun case is written correctly ...if not correct then modifying it to the correct one
def check_gnp(gnp):
	if gnp[2] == 'm':
		new_gnp = '- - m'
	elif gnp[2] == 'u':
		new_gnp = '- ' + gnp[1] + ' ' + gnp[2]
	else:
		new_gnp = gnp[0] + ' ' + gnp[1] + ' ' + gnp[2] 
	return new_gnp

####################################################
count = 0
new_r = []
head = []
for i in range(0, len(fr)):
	if i == 1:	#Lemma field
		lst = fr[i].strip().split(',')
		for each in lst:
			lem_lst.append(each)
		for j in range(0, len(lst)):
			if '~' in lst[j] or '*' in lst[j]:
				r = re.split('[~*]', lst[j])
#				print '%%%', r 
				count = len(r) - 1  
			new_r.append(str(j) + ':' + str(count)) #storing column info and how many telda's r there 
			count = 0
	####################################################
	if i == 4:	#Category field
		lst = fr[i].strip().split(',')
		for each in lst:
			if each in cat_dic:
				cat_output = cat_dic[each] 
				cat_list.append(cat_output)
			elif each == 'yes_no_qsn': #Ex: kyA
				cat_list.append('')
			else:
				cat_list.append(each)
	####################################################
	elif i == 5:	#GNP field
		lst = fr[i].strip().split(',')
		#print cat_list , len(cat_list), len(lst)
		for j in range(0, len(lst)):
			if cat_list[j] == 'pron':
				gnp = lst[j][1:-1].split()
				gnp_output = check_gnp(gnp)
				gnp_lst.append('[' + gnp_output + ']')
			else:
				gnp_lst.append(lst[j])
	####################################################
	elif i == 6:	#Relation field
#		count = 0
		lst = fr[i].strip().split(',')
		for j in range(0, len(lst)):
			for k in new_r:
				t = k.split(':')
				new_c = []
				new_g = []
				if int(t[0]) == j:
					if '~' not in lst[j] and '*' not in lst[j]:
						if ':' in lst[j]:
							rel = lst[j].split(':')
							if '.' in rel[0] and rel[0] not in head:
								head.append(rel[0])
							if rel[1] in cat_dic:
								m = cat_dic[rel[1]]
								new_c.append(m)
								new_g.append('')	
					else:
						#r = lst[j].split('~')
						r = re.split('[~*]', lst[j])
						for each in r :  #Ex: eka~acCA~ladZakA_ke_sAWa
							rel = each.split(':')
							if '.' in rel[0] and rel[0] not in head:
								head.append(rel[0])
							if rel[1] in cat_dic:
								m = cat_dic[rel[1]]
								new_c.append(m)
								new_g.append('')	
	#							count += 1
					new_c.append(cat_list[j])
					new_g.append(gnp_lst[j])	
					cat_list[j] = '~'.join(new_c) #Ex:card~adj~n
					gnp_lst[j] = '~'.join(new_g) #storing head info and keeping remaining gnp empty Ex: ,,[m sg a] for above ex.
			rel_lst.append(lst[j])
	elif i == 7:
		lst = fr[i].strip().split(',')
		for j in range(0, len(lst)):
			r = []
			if j <= len(new_r):
				t = new_r[j].split(':')
				if int(t[0]) == j:
					for i in range(0,int(t[1])):
						r.append('')
 					r.append(lst[j])
					rel_lst1.append('~'.join(r))
				else:
					rel_lst1.append(lst[j])
			else:
				rel_lst1.append(lst[j])
#		for each in lst:
#			rel_lst1.append(each)

	####################################################
	elif i == 8:
		lst = fr[i].strip().split(',')
#		for each in lst:
#			rel_lst2.append(each)
		for j in range(0, len(lst)):
			rel = lst[j].split(':')
			if len(rel) == 2:
				if rel[1] == 'emp':
					cat_list[j] = cat_list[j] + '*manner_adv'
					gnp_lst[j] = gnp_lst[j] + '*'
#				if rel[1] == 'res':
					
				if rel[1] == 'co-ref': #apanA is refered to pron with co-ref so storing lemma, cat and gnp of co-ref id
					if cat_list[int(rel[0])-1] == 'pron': #(co-ref with pron)
						cat_list[j] = 'pron'
						gnp_lst[j] = gnp_lst[int(rel[0])-1]
						lem_lst[j] = lem_lst[int(rel[0])-1]
					else:  #[rAma_apanA]_piwA_ko_xeKa_rahA_hE (co-ref is with propn)
						cat_list[j] = 'pron'
						gnp_lst[j] = gnp_lst[int(rel[0])-1]
						prn_key = 'pron,'  + gnp_lst[int(rel[0])-1]
						lem_lst[j] = hnd_pron_dic[prn_key]
			r = []
			if j <= len(new_r):
				t = new_r[j].split(':')
				if int(t[0]) == j:
					for i in range(0,int(t[1])):
						r.append('')
					if 'co-ref' in lst[j] : #Remove co-ref relation as we are storing lemma, cat and gnp info
						rel_lst2.append('')
					else:
						r.append(lst[j])
						rel_lst2.append('~'.join(r))
				else:
					rel_lst2.append(lst[j])
			else: 
				rel_lst2.append(lst[j])

					
									
	####################################################

############################################################
#print csv file after changing pos and gnp:
#lem_lst = []
for i in range(0, len(fr)):
	lst = fr[i].strip().split(',')
	if i == 1:
		for j in range(0, len(lst)):
			if cat_list[j] == 'pron' and '_' not in lst[j] and lst[j] != '':
				lem_lst[j] = lst[j] + '_1'
			if lem_lst[j] == 'apanA_1' and rel_lst2[j] != 'co-ref': #muJe_apanI_puswaka_xiKAo 
				cat_list[j] = 'pron'
				gnp_lst[j] = '[- - m]'
				lem_lst[j] = 'wuma_1'
#			else:
#				lem_lst.append(lst[j])
		print ','.join(lem_lst)			
	elif i == 4:
		print ','.join(cat_list)
	elif i == 5:
		print ','.join(gnp_lst)
	elif i == 6:
		print ','.join(rel_lst)
	elif i == 7:
		print ','.join(rel_lst1)
	elif i == 8:
		print ','.join(rel_lst2)
	else:
		print fr[i].strip()
############################################################
