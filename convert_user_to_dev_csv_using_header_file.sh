## Convert user csv to developer csv for complex sentences ##
#############################################################
MYPATH=`pwd`

rm -f file file1

ls  $1  >list
cp $1  $MYPATH/ 2>/dev/null

sed 's/_user.csv//g' list | sed  's/\(.*\)\/.*/\1/g' > list1
path=`cat list1`

#Read header file info
python src/read_header_file.py  $1 dic/conjunction_dic.txt k k1
cat k

echo "------------------"
while read line 
do
	echo $line
	echo $line | cut -f2 -d ' '> f2 
	echo $line | cut -f1 -d ' '> f1 
	var=`cat f2`
	var1=`cat f1`
	bash run_communicator.sh $path/$var"_user.csv" #Convert user csv to developer csv -> to dmrs ->ace generato
	grep -o ".$" output/$var"_dev.csv_sent.txt" > last_char #storing last punctuation
	sed -i 's/[\.?]$//g' output/$var"_dev.csv_sent.txt"     #removing last punctuation in every sentence
	cat output/$var"_dev.csv_sent.txt" >  $var1
	echo '--------------------'	
done < k

while read line
do
	paste $line last_char > out #restoring last punctuation
	sed -i 's/\t/ /g' out 
	cat out 
done < k1
