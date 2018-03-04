#rm -rf databases/default_prep.gdbm  

# src/create-gdbm.pl databases/default_prep.gdbm < dic/chl_rel_prep_mapping.txt

 ./comp.sh src/ir
 mv src/ir.out  $DMRS/bin/ir
 ./comp.sh src/ir_no@
 mv src/ir_no@.out  $DMRS/bin/ir_no@

#python src/map_concept_dic_to_dev.py  dic/concept_dictionary_user.txt  dic/user_cat-to-dev_cat.txt   dic/concept_dictionary.txt
python src/get_tam_info_for_ace.py dic/tam_mapping.csv  dic/modal_list.txt dic/control_verb_list.txt   > dic/new_tam_dic.csv

cd provisional_dics/
if  [ -e concept_dictionary_user.txt ] ; then
	#concept dictionary
	cat ../dic/concept_dictionary_user.txt concept_dictionary_user.txt > dic
	sort -u dic > concept_dictionary_user.txt
	cat ../dic/concept_dictionary_dev.txt concept_dictionary_dev.txt > dic
	sort -u dic > concept_dictionary_dev.txt
	
	#tam file:
	cat ../dic/tam_mapping.csv tam_mapping.csv > tmp
	sort -u tmp > tam_mapping.csv
	python ../src/get_tam_info_for_ace.py tam_mapping.csv  ../dic/modal_list.txt ../dic/control_verb_list.txt   > new_tam_dic.csv

	#template dic:
	cat ../dic/user_template_dic.txt user_template_dic.txt > tmp
	sort -u tmp > user_template_dic.txt

	rm -f tmp
fi

cut -f1 ../dic/pronoun_lemma_dic.txt > f1
cut -f1 -d','  f1 > f1-1
cut -f2 -d','  f1 > f2-1
cut -f3 -d','  f1 > f3-1
paste f2-1 f3-1 > f2-f3
sed -i 's/\t/,/g' f2-f3 
paste f2-f3 f1-1 > ../dic/hnd_pron_dic.txt
rm f1 f1-1 f2-1 f3-1 f2-f3
