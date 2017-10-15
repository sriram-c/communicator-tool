#Programme to convert user.csv  to facts format
#Written by Roja(23-02-17)
#RUN: python src/convert_user_csv_to_facts.py  output/Apane_upanyAsa_yaha_vinxu_waka_paDzA_hE_user.csv.tmp2 
###########################################################################################################
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


#map puncs in chunk to avoid errors in Clips
def map_punc_info(chunk):
	new_lst = []
	lst = chunk.split('_')
	for each in lst:
		if '?' in each:	
			new_lst.append('PUNCTQUES')
		else:
			new_lst.append(each)
	c = '_'.join(new_lst)
	return c	


#Get vib information from chunk . Vib is stored with a '_'	
def get_vib_frm_chunk(chunk):
	if '-' not in chunk:
		lst = chunk.split('_')
		return lst[1:]



#function to print list to facts format:
def print_info_from_lst_to_fact(f_name, fact_name, List):
	count = 0 
#	if fact_name != 'user_intra_chunk_rel-ids' and fact_name != 'user_inter_chunk_rel-ids' and fact_name != 'user_discourse_rel-ids':
	if '_rel-ids' not in fact_name:
		for each in List:
			count += 1
			if fact_name == 'user_id-gen-num-per' and each != '': #As GNP is stored in [  ] format
				f_name.write('(' + fact_name + ' ' + str(count) +  ' ' + each[1:-1] + ')\n')
			elif fact_name == 'user_id-chunk-vib' and each != '':
				each =  map_punc_info(each) #map puncs 
				vib = get_vib_frm_chunk(each)
				if vib != None and '#' not in each:
					f_name.write('(' + fact_name + ' ' + str(count) +  ' ' + each + ' ' + '_'.join(vib) + ')\n')
				elif vib != None and '#' in each:
					f_name.write('(' + fact_name + ' ' + str(count) +  ' ' + each + ' ' + '_'.join(vib) + ' -)\n')
			elif each != '':
				f_name.write('(' + fact_name + ' ' + str(count) +  ' ' + each + ')\n')
	else:
		for each in List:
			count += 1
			rel = each.split(':')
			if len(rel) == 2:   #printing (rel head dependent) format
				f_name.write('(' + fact_name + ' ' + rel[1] + ' ' +  rel[0] + ' ' + str(count) + ')\n')



for i in range(0, len(fr)):
	lst = fr[i].strip().split(',')
	if i != 2: #ignoring i == 2 , as it shows only ids	
		print_info_from_lst_to_fact(open(filenames[i], "w"), fact_info[i], lst) #convert each lst into facts
