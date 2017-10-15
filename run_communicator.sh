#To run language communicator 
#Input: user csv 
#Output: Sentence generated from Ace parser. 
#RUN: bash run_communicator.sh <user.csv>
#	Ex: bash run_communicator.sh   boy_can_eat_rice_with_the_spoon_user.csv 
#######################################################################################
MYPATH=`pwd`

#Pre-processing input file::
rm -f err1
ls  $1  >list
cp $1  $MYPATH/ 2>/dev/null

sed 's/_user.csv//g' list | sed  's/.*\/\(.*\)/\1/g' > list1

var=`cat list1`
mkdir -p output
#mkdir -p files
#converting utf8 to wx::
utf8_wx $var"_user.csv" > tmp 
sed  -i 's/[ ]*,[ ]*/,/g' tmp

#If dic exists in provisional dics folder  
if [ -e provisional_dics/user_template_dic.txt ] ; then
	python src/extract_template_info_for_user_csv.py tmp  provisional_dics/user_template_dic.txt  provisional_dics/concept_dictionary_user.txt dic/hindi_cat.txt output/$var"_transform.txt" > tmp1
else
	python src/extract_template_info_for_user_csv.py tmp  dic/user_template_dic.txt  dic/concept_dictionary_user.txt dic/hindi_cat.txt output/$var"_transform.txt" > tmp1
fi

error=`grep "%%%%\|IndexError" tmp1`

if [ "$error" == "" ]; then

	#Temporarily adding dummy category row 
	python src/check_for_cat_row.py tmp1 err1 > $var"_user.csv"
	if [ -s err1 ] ; then
		cat err1
		cp tmp $var"_user.csv"
		exit
	fi 
else
	echo  $error
	exit
fi

#Convert User csv to developer csv 
sh convert_user_to_dev_csv.sh $var"_user.csv"  $var"_dev.csv" >> err1 2>&1
cat err1 
var1=`grep "%%%%\|IndexError" err1`

if [ "$var1" == "" ] ; then  
	sh run.sh  $var"_dev.csv"
	if  ! [ -s output/$var"_transform.txt" ] ; then 
		cat output/$var"_dev.csv"_sent.txt 
	else
		python src/transform_sentence.py output/$var"_dev.csv"_sent.txt  output/$var"_transform.txt"
	fi
else
	exit
fi

#mv $var"_user.csv"  $var"_dev.csv" files/
