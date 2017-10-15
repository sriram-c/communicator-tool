import sys

f = open(sys.argv[3], 'w')
f1 = open(sys.argv[4], 'w')
d = open(sys.argv[2], 'r')

dic = {}

for line in d:
	lst = line.strip().split()
	dic[lst[0]] = lst[1]



count = 0
sent_info = []

for line in open(sys.argv[1]):
	lst = line.strip().split('\t')
	key = 's' + str(count) + ':'
	if key in lst[0]:
		lst = line.strip().split('\t')
		sent = lst[1].split()
		f.write('s%d.g\t%s\n' % (count , '_'.join(sent)))
	if 's.g' in line:
		lst = line.strip().split('\t')
		rule = lst[1].split('+')
		for each in rule:
			if each not in dic.keys():
				sent_info.append(each)
			else:
				f2 = open(dic[each], 'w')
				sent_info.append(dic[each])
				f2.write(dic[each]+'\n')
		f1.write('%s\n' % ' '.join(sent_info))
	count += 1
	
