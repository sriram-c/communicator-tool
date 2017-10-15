#Programme to convert "user csv facts" to "csv"
#Written by Roja (01-05-17)
#RUN: python src/convert_facts_to_csv.py output/$1.tmp2 > output/$1.tmp3
###########################################################################
import sys

f = open(sys.argv[1], 'r')
fr = f.readlines()

filenames = [
		"user_chunk_and_vib_info.dat",
		"user_lemma_info.dat",
		None,
		"user_cat_info.dat",
		"user_definiteness_info.dat",
		"user_gnp_info.dat",
		"user_intrachunk_rel.dat",
		"user_interchunk_rel.dat",
		"user_discourse_rel.dat"
	]


fact_info = [
		"user_id-chunk-vib",
		"user_id-lemma",
		None,
		"user_id-cat",
		"user_id-definiteness",
		"user_id-gen-num-per",
		"user_intra_chunk_rel-ids",
		"user_inter_chunk_rel-ids",
		"user_discourse_rel-ids"
	]

#Currently mapping only rels facts:
def print_facts_into_csv(f_name, fact_info):
	rel_f = f_name.read()
	new_lst = []
	if rel_f == '':
		new_lst.append('')
		new_lst.append('')
	else:
		lst = rel_f.split('\n')
		for each in lst:
			l = each[:-1].split()
			if len(l) >= 3:
				while len(new_lst) < int(l[3]) :  #Initially adding empty string (as the facts can be stored in any order) 
					new_lst.append('')
				if len(new_lst) >= int(l[3]) :    #based on the fact replacing relation if present
					new_lst[int(l[3])-1] = l[2] + ':' + l[1]
			else:
				new_lst.append('')
	return new_lst


#Convert relation facts to csv 
for i in range(0, len(fr)):
	if i == 6 or i == 7 or i == 8: #Reading only relation files
		out = print_facts_into_csv(open(filenames[i], "r"), fact_info[i])
		print ','.join(out)
	else:
		print fr[i].strip()
