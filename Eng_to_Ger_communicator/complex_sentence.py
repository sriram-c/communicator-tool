import sys
import subprocess
import os
import re

fname1 = str(sys.argv[1])
fname2 = str(sys.argv[2])
fname3 = str(sys.argv[3])
file1=open(fname1,'r')
file2=open(fname2,'w')
file3=open(fname3,'w')

for line in file1:
	if (line.find("s1:\t")!=-1):
		word=line.split("\t")
		sent=word[1].replace("\n","")
		sent=sent.replace(" ","_")
		myfile = open('/home/arpita/create-hindi-parser/chl_to_dmrs/output/'+sent+'_dev.csv_sent.txt','r')
		myline = myfile.readline()
		file2.write(myline)
	if (line.find("s2:\t")!=-1):
                word=line.split("\t")
                sent=word[1].replace("\n","")
                sent=sent.replace(" ","_")
                myfile = open('/home/arpita/create-hindi-parser/chl_to_dmrs/output/'+sent+'_dev.csv_sent.txt','r')
                myline = myfile.readline()
                file3.write(myline)
	if (line.find("s.g:\t")!=-1):
		word=line.split("\t") 
		str1=re.findall(r'\+.*?\+',word[1])
		n=str(str1).strip('[]')
		n=n.replace('+','')
		n=n.replace('\'','')
                n=','+n + '_'
		f=open ('/home/arpita/Eng_to_Ger_communicator/t1.txt','r')
		for lines in f:
			 if (lines.find(n)!=-1):
				str2=lines.split(",")
				gerwrd=str2[5]
				gerwrd=gerwrd.replace("_1\n","")
				print gerwrd

file2.close()
file3.close()
#		print subprocess.check_output(["./home/user/Eng_to_Ger_communicator/eng_to_ger_shell.sh " + str(sys.argv[2])], shell=True) 
#os.system("sh /home/user/Eng_to_Ger_communicator/eng_to_ger_shell.sh " + fname2)

#arglist = 'fname2 f2'
#arglist1 = 'fname3 f3'
#os.system("sh eng_to_ger_shell.sh " + arglist)
os.system("sh eng_to_ger_shell.sh " + fname2)
os.system("sh eng_to_ger_shell.sh " + fname3)
#os.system("sh eng_to_ger_shell.sh " + arglist1)
F1=open(fname2+'_out','r')
F2=open(fname3+'_out','r')
myline1 = F1.readline()
myline2 = F2.readline()
print myline1.replace('.\n','') + " " + gerwrd + " " + myline2.replace('\n','') 
