#Programme to check sense and replace it.
#NOTE: As of now handling only nouns with single sense
#Written by Roja (05-011-16)
############################################################
import sys,re

sense_dic = {}

#To get sense dic::
for line in open(sys.argv[2]):
	lst = line.strip().split('\t')
	s = lst[1].split('_')
	sense_dic[lst[0]] = s[1]

#To get cat :
#As of now handling only nouns:
cat = str(sys.argv[3])

#Function to return lemma, pos and sense:
def return_lemma_pos_nd_sense(line):
	lem_pos_sen = []
	lem = re.findall(r'lemma="\w+"', line)
	lemma = lem[0][7:-1] #ex: ['lemma="book"'], lemma = book
	c = re.findall(r'pos="\w+"', line)
	cat = c[0][5:-1]
	if 'sense=' in line:
		s = re.findall(r'sense="[\w\d]+"', line)
		sense = s[0][7:-1] #ex: ['sense="1"'] , sense_info = 1
	else:
		sense = ''
	lem_pos_sen.append(lemma)	
	lem_pos_sen.append(cat)	
	lem_pos_sen.append(sense)	
	return lem_pos_sen

#Check dmrs info
for line in open(sys.argv[1]):
	if 'lemma="' in line:
		out = return_lemma_pos_nd_sense(line)
		if out != None:
			if cat == out[1] and out[0] in sense_dic:
				if sense_dic[out[0]] !=  out[2]:
					var = 'sense="' + sense_dic[out[0]] + '"'
					line = re.sub('sense="[\w\d]+"', var, line)
					print line.strip()
				else:
					print line.strip()
			else:
				print line.strip()
	else:
		print line.strip()
