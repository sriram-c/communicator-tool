if [ -s ../dic/concept_dictionary_user.txt ] ; then
	cp ../dic/concept_dictionary_user.txt .
	cp ../dic/concept_dictionary_dev.txt .
fi

if [ -s  ../dic/tam_mapping.csv ] ; then
	cp ../dic/tam_mapping.csv .
fi

if [ -s ../dic/user_template_dic.txt ] ; then
	cp ../dic/user_template_dic.txt .
fi
