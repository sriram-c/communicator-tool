#Programme to generate ace parser related TAM info using hindi parser tam info
#python src/get_tam_info_for_ace.py dic/tam_mapping.csv  dic/modal_list.txt dic/control_verb_list.txt   > dic/new_tam_dic.csv
#Written by Roja(14-06-17)
#############################################################################################################################
import sys

modal_v_lst = []
cntrl_v_lst = []
new_tam = []

for line in open(sys.argv[2]):
	modal_v_lst.append('_'.join(line.strip().split()))

for line in open(sys.argv[3]):
	cntrl_v_lst.append('_'.join(line.strip().split()))

#print modal_v_lst, cntrl_v_lst 
def print_new_tam(h_tam, e_tam, dev_tam, modal, modal_tam, cat):
	new_tam = []
	new_tam.append(h_tam)
	new_tam.append(e_tam)
	new_tam.append(dev_tam)
	new_tam.append(modal)
	new_tam.append(modal_tam)
	new_tam.append(cat)
	return ','.join(new_tam)
 
for line in open(sys.argv[1]):
	if line.strip() == 'Hindi_anu,English_anu,dev_csv':
		print 'Hindi_tam,Eng_tam,Verb_dev_tam,Modal_verb,Modal_dev_tam,Dev_Cat'
	else:
		lst = line.strip().split(',')
		t = lst[1].split('_')
		if t[0] in modal_v_lst : #or t[0] + '_' + t[1] in modal_v_lst:
			tam_info = lst[2][1:-1].split()
			if tam_info[0] == '+' or tam_info[1] == '+':
				#If either perf or prog info is present then tam info is not passed to modal verb. Only tense info is passed
        	                #Ex:SAyaxa_Sohana_ne_usakI_maxaxa_kiyA_hogA
				v_tam = '[' + tam_info[0] + ' ' + tam_info[1] + ' untensed]'
				m_tam = '[- - ' + tam_info[2] +']'
				out = print_new_tam(lst[0], lst[1], v_tam, t[0], m_tam, 'modal')
			else:
				out = print_new_tam(lst[0], lst[1], '', t[0], lst[2], 'modal')
		elif len(t) > 1 and t[0] + '_' + t[1] in cntrl_v_lst: 
			out = print_new_tam(lst[0], lst[1], '', t[0], lst[2], 'v')
		else:
			out = print_new_tam(lst[0], lst[1], lst[2], '', '', '')
		print out
