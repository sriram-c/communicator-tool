mkdir -p output

#To check Syntax errors in CSV file:
python src/check_syntax_error.py $1  > err
if  [ -s err ] ; then
	cat err
	exit
fi
#If no errors then proceeding further:
python src/get_chl_rels_info_into_facts.py $1 
python src/insert_definiteness.py lemma_info_tmp.dat cat_info_tmp.dat quant_info_tmp.dat rel.dat dic/names_with_definiteness.txt > quant_insert_tmp.dat
python src/insert_quant.py cat_info_tmp1.dat quant_insert_tmp.dat gnp_info.dat rel.dat lemma_info_tmp1.dat noun-quant_tmp.dat > quant_insert.dat
python src/get_node_nd_link.py cat_info.dat lemma_info.dat gnp_info.dat sent_type.dat rel.dat quant_insert.dat insert_prep.dat template_info.dat noun-quant.dat dic/template_key-template_info.txt $1_template_debug_info.txt> output/$1_dmrs.txt
mv cat_info_tmp*.dat lemma_info_tmp*.dat gnp_info.dat lemma_info.dat cat_info.dat sent_type.dat quant_insert_tmp.dat quant_insert.dat rel.dat template_info.dat insert_prep.dat noun-quant_tmp.dat noun-quant.dat output/
python src/separate_node_nd_link.py output/$1_dmrs.txt > output/$1_tmp_dmrs.txt
python src/replace_sense_info_in_dmrs.py output/$1_tmp_dmrs.txt  dic/Noun_single_sense_dic.txt  n > output/$1_new_dmrs.txt
#python src/replace_sense_info_in_dmrs.py output/$1_tmp_new_dmrs.txt1  v1  v > output/$1_new_dmrs.txt
mv link_f node_f output/
sed -i 's/\(lemma="be" pos="v" sense="\)1"/\1there"/g' output/$1_new_dmrs.txt
#sed -i 's/carg="one"/carg="1"/g' output/$1_new_dmrs.txt
python $PYDELPHIN/language/beta_language/tree_to_dict.py output/$1_new_dmrs.txt > output/$1_mrs.txt
$HOME/ace-0.9.24/ace -g $HOME/ace-0.9.24/erg-1214-x86-64-0.9.24.dat -e output/$1_mrs.txt > output/$1_sent.txt
#cat output/$1_sent.txt
