## Convert user csv to developer csv ##
#######################################
MYPATH=`pwd`

mkdir -p output
rm -f prep_debug_file.dat
echo "(defglobal ?*chlpath* = $MYPATH)" > path.clp

echo "Checking Syntax Errors in CSV file ..."
#To check Syntax errors in CSV file:
python src/check_syntax_error_in_user_csv.py $1  > err
if  [ -s err ] ; then
        cat err
        exit
fi
#If no errors then proceeding further:
echo "Map user category to developer category ..."
python src/cat_nd_gen_mapping.py  $1 dic/user_cat-to-dev_cat.txt dic/hnd_pron_dic.txt > output/$1.tmp
python src/map_chunk_info.py  output/$1.tmp  > output/$1.tmp1 
python src/map_rel_nd_cat.py output/$1.tmp1 > output/$1.tmp2
echo "Convert user csv to facts format ..."
python src/convert_user_csv_to_facts.py output/$1.tmp2
#python src/get_prep_from_verb.py dic/verb_rel_prep_mapping.txt > prep_insertion_based_on_verb.dat
python src/get_prep_from_verb.py dic/verb_kAraka_prep_mapping.txt > prep_insertion_based_on_verb.dat
sed 's/^/(rel_name-default_prep  /g' dic/chl_rel_prep_mapping.txt | sed 's/$/)/g' > default_prep_insertion_based_on_rel.dat

timeout 10 clips -f clip_files/run.bat > output/err 2>&1

echo "Convert user csv facts to csv"
python src/convert_facts_to_csv.py output/$1.tmp2 > output/$1.tmp3
if [ -e provisional_dics/concept_dictionary_user.txt ] ; then
	python src/get_concept_info.py  output/$1.tmp3  provisional_dics/concept_dictionary_user.txt provisional_dics/concept_dictionary_dev.txt dic/pronoun_lemma_dic.txt output/$1.tmp4 output/replace_id.dat 
else
	python src/get_concept_info.py  output/$1.tmp3  dic/concept_dictionary_user.txt dic/concept_dictionary_dev.txt dic/pronoun_lemma_dic.txt output/$1.tmp4 output/replace_id.dat 
fi

mv user*.dat output/

echo "Convert user csv to developer csv"
touch prep_insertion.dat
if [ -e provisional_dics/tam_mapping.csv ] ; then
	python src/convert_user_to_devloper_csv.py  output/$1.tmp4 dic/pronoun_lemma_dic.txt provisional_dics/new_tam_dic.csv  dic/link_list.txt prep_insertion.dat dic/hnd_pron_dic.txt dic/cat_relation_mapping.txt output/replace_id.dat dic/passive.txt $2
else
	python src/convert_user_to_devloper_csv.py  output/$1.tmp4 dic/pronoun_lemma_dic.txt dic/new_tam_dic.csv  dic/link_list.txt prep_insertion.dat dic/hnd_pron_dic.txt dic/cat_relation_mapping.txt output/replace_id.dat dic/passive.txt $2
fi
