import sys 

f = open(sys.argv[1], 'r')
fr = f.readlines()

#Note: moved pass_v cat modification code to convert_user_to_developer_csv.py
cat_lst = []
rel_lst = []

for i in range(0, len(fr)):
	lst = fr[i].strip().split(',')
	if i == 4:
		for each in lst:
			cat_lst.append(each)
	if i == 7:
		rel_lst = lst

for i in range(0, len(fr)):
	if i == 4:
		print ','.join(cat_lst)
	elif i == 7:
		lst = fr[i].strip().split(',')
#		print len(lst)
		for j in range(0, len(lst)):
			rel = lst[j].strip().split(':')
			if cat_lst[j] == 'manner_adv': #I [walk slowly]. Interchanging relation of slowly and walk.
				if rel[0] != '': #Ex:Ram_also_talked_to_a_good_boy_at_the_bus_stop.csv
						rel_lst[j] = ''
					#try:
						if int(rel[0])-1 <= len(rel_lst):
					#		print rel_lst , rel[0]
							if cat_lst[int(rel[0])-1] == 'v':
								rel_lst[int(rel[0])-1] = str(int(rel[0])-1) + ':' + rel[1]
							
						else:
							if cat_lst[int(rel[0])-1] == 'v':
								v = str(int(rel[0])-1) + ':' + rel[1]
								rel_lst.append(v)
					#except :
							#print '%%%%%%% Error %%%%'
		print ','.join(rel_lst)
		rel_lst = []
	elif i == 8: #emp rel need to be mapped near 'v' #Ex: usane_yaha_billI_ko_BI_sAWa_le_liyA_user.csv
		lst = fr[i].strip().split(',')
		rel_lst = lst
		for j in range(0, len(lst)):
			rel = lst[j].strip().split(':')
			if cat_lst[j] == 'manner_adv': #Ex: usane_yaha_billI_ko_BI_sAWa_le_liyA_user.csv
				if rel[0] != '': #Ex:Ram_also_talked_to_a_good_boy_at_the_bus_stop.csv
					rel_lst[j] = ''
					if int(rel[0])-1 <= len(rel_lst):
						if cat_lst[int(rel[0])-1] == 'v':
							rel_lst[int(rel[0])-1] = str(int(rel[0])-1) + ':' + rel[1]
					else:
						if cat_lst[int(rel[0])-1] == 'v':
							v = str(int(rel[0])-1) + ':' + rel[1]
							rel_lst.append(v)
		print ','.join(rel_lst)
	else:
		print fr[i].strip()
			
