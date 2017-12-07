MYPATH=`pwd`
#cat $1
cp $1 $MYPATH/Eng_to_Ger_communicator/$1
cp $1 $MYPATH/Eng_to_Jap_communicator/$1
cd Eng_to_Ger_communicator
echo "----German----"
bash eng_to_ger_shell.sh $1 > ger_gen_sent
cat ger_gen_sent
cd ../Eng_to_Jap_communicator
echo "----Japanese----"
bash eng_to_jap_shell.sh $1 > jap_gen_sent
cat jap_gen_sent

