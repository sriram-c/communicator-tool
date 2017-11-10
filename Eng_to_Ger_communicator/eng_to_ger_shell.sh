bash $HOME/ace-0.9.24/generate_multiple_mrs_nd_dmrs.sh $1
python mrs_facts_gen.py $HOME/ace-0.9.24/output/$1_mul_mrs.txt clip.txt
cp clip.txt mrs_facts.dat
myclips -f eng_ger_rules.clp
python fetch_german.py ger_mrs.dat t2.txt
python clip_to_mrs_copy.py t2.txt mrs_generated
cd $HOME/german/german_src
bash mod_mrs_sent.sh $HOME/Eng_to_Ger_communicator/mrs_generated
#cat t2.txt

