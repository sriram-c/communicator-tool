import sys

f = open(sys.argv[1], 'r')
fr = f.readlines()
fw = open(sys.argv[2], 'w')

len1 = len(fr)

l = []

if len1 == 8:
#	print len1
	for i in range(0, len(fr)):
		lst = fr[i].strip().split(',')
		len_lst = len(lst)
		if i < 2:
			print fr[i].strip()
		elif i == 2:
			print fr[i].strip()
			for i in range(len_lst):
			    l.append('')
			print ','.join(l)
		else:
			print fr[i].strip()
else:
	print f.read()
	fw.write('%%%%%%%%%% User csv file does not contains 8 rows  . Please check %%%%%%%%%%%\n')
