import sys, re
f = open(sys.argv[1], 'r')
fr = f.readlines()

count = 0 

row = []
dic = {}
c_id = []

for i in range(0, len(fr)):
	if i == 1:
		lst = fr[1].strip().split(',')
		for j in range(0, len(lst)):
			if '~' in lst[j] or '*' in lst[j] :
				c_id.append(j)
#				l = lst[j].split('~')
				l = re.split('[~*]', lst[j])
				m = 0.1 #as chunks are stored in 0.1, 0.2 etc.
				for k in range(0, len(l)):
#					print '^^^', l[k]
					if k != len(l)-1:
						dic[j+count] = j + m 
						count += 1
						m  += 0.1
					else:
						dic[j+count] = j + m 
						m = 0
			else:
				dic[j+count] = j 

#for key in sorted(dic):
#	print key , '--', dic[key]

def replace_telda_with_comma(lst):
	row = []
	for j in range(0, len(lst)):
		if '~' not in lst[j] and '*' not in lst[j]:
			row.append(lst[j])
		else:
		#	l = lst[j].split('~')
			l = re.split('[~*]', lst[j])
			for k in range(0, len(l)):
				row.append(l[k])
	return row
	

for i in range(0, len(fr)):
	row = []
	if i == 2:
		ids = []
		for each in dic.keys():
			ids.append(str(each+1))
		print ','.join(ids)
	elif i >= 5:
		row = []
		lst = fr[i].strip().split(',')
		out = replace_telda_with_comma(lst)
		val = ''
#		print out 
		for each in out:
			if ':' in each:
				rel = each.split(':')
				k = rel[0].split('.')
#				if float(rel[0])-1 == float(dic[key]):
				if len(k) == 2:  #removed above condition as float of subtracted values varies Ex: float(2.3)-1 != 1.3 
					v = int(k[0]) + int(k[1]) - 1
					val = str(v) + ':' + rel[1]
				else:
					for key in sorted(dic):
						v = int(k[0]) - 1
						if float(v) == dic[key]: #checking only direct float values 
							val = str(key+1) + ':' + rel[1]
						#elif float(v) == key-1: #Need to check this elif . Ex: [wumhArI_manapasaMxa]_PiZlma_kOna_sI_hE_user.csv
						#	val = str(key+1) + ':' + rel[1] 
				row.append(val)
			else:
				row.append(each)
		print ','.join(row)
	elif '~' in fr[i] or '*' in fr[i]:
		lst = fr[i].strip().split(',')
		out = replace_telda_with_comma(lst)
		print ','.join(out)
	else:
		print fr[i].strip()
