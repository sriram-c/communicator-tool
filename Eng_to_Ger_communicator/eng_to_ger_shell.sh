MYPATH=`pwd`
cat $1 
bash $HOME/ace-0.9.24/generate_multiple_mrs_nd_dmrs.sh $1
python mrs_facts_gen.py output/$1_mul_mrs.txt clip.txt
cp clip.txt mrs_facts.dat
myclips -f eng_ger_rules.clp >/dev/null
python fetch_german.py ger_mrs.dat ger_facts.txt $HOME/communicator-tool/dic/concept_dictionary_user.txt german_dict
python clip_to_mrs_copy.py ger_facts.txt mrs_generated
cd $HOME/german/german_src
#cp $2 $MYPATH/file1
bash mod_mrs_sent.sh $HOME/communicator-tool/Eng_to_Ger_communicator/mrs_generated > $MYPATH/German_run/$1_out
cat $MYPATH/German_run/$1_out
#cat t2.txt

