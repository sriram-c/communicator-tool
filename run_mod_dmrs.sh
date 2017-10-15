python $PYDELPHIN/language/beta_language/tree_to_dict.py output/$1_new_dmrs.txt > output/$1_mrs.txt
$HOME/ace-0.9.24/ace -g $HOME/ace-0.9.24/erg-1214-x86-64-0.9.24.dat -e output/$1_mrs.txt > output/$1_sent.txt
cat output/$1_sent.txt
