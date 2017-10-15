import sys

#Need to handle replacing of first word.

dic = {}

#Transform information::
for line in open(sys.argv[2]):
	lst = line.strip().split('\t')
	dic[lst[0]] = lst[1]

punc_lst = [',' , '.' , '"', '?' , '!']

p = []

def change_first_letter_upper(word):
	return word[0].upper()+word[1:]


def check_for_punc(word, word_count, org_wrd):
	new_word = []
	if word[-1] not in punc_lst:
		if word in dic.keys():
			if word_count == 1: #To change first letter to upper case
				val = change_first_letter_upper(dic[word])
				new_word.append(val)
			else:
				new_word.append(dic[word])
		elif word_count == 1:
			new_word.append(org_wrd)
		else:
			new_word.append(word)
	else:
		if word[:-1] in dic.keys():
			if word_count == 1: #To change first letter to upper case
				val = change_first_letter_upper(dic[word[:-1]])
				new_word.append(val)
			else:
				new_word.append(dic[word[:-1]])
			p.append(word[-1])
		elif word_count == 1:
			new_word.append(org_wrd)
		else:
			new_word.append(word)
	return ''.join(new_word)



#Replace transform information:
for line in open(sys.argv[1]):
	new_sent = []
	lst = line.strip().split()
	for each in lst:
		if each == lst[0]: #Checking only first word is capital or not
			if each[0].isupper(): 
				wrd = check_for_punc(each.lower(), 1, each) #If first word is not in transform dic then replacing with original word. So giving word count and original word to function
				new_sent.append(wrd)
		else:			
			wrd = check_for_punc(each, 0, each) #Using 0 , incase word is not first word
			new_sent.append(wrd)
		if p != []:
			new_sent.append(''.join(p))
			p = []
	print ' '.join(new_sent) 
