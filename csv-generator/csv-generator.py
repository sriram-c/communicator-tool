
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#######################################################################
#                               content                               #


# Objective
    
#    Given the csv file for a source language and morphological analyser for a target language
#    
#    generate following files for the target language.
#
#    
#        1.  CSV file
#        2.  Concept-dictionary
#        3.  karaka-vibhakti mapping
#
#Logic:
#
#1. Read Hindi and Telugu parallel sentence and map the words in the sentences.
#
#2. Run the telugu morph on each word of the Telugu sentence
#
#	2.1. mark the root, vibhakti, tam for each word
#
#3. start writing the Telugu csv file similar to the Hindi csv rows.

#

#Functions:
#
#    1. Create_concept_dictionary
#    2. Create_karaka_vibhakti_mapping
#    3. create_csv
#


#
#Assumption: 
#
#Hindi and Telugu sentences are parallel and word aligned (i.e same number of words in Hindi and Telugu)
#
#
#Required files/tools:
#
#1. Hindi csv file
#2. Hindi - Telugu parallel sentences
#3. Telugu morph analyser
#4. Lttoolbox
#


#######################################################################


import sys
import csv
import subprocess
import os.path
import re

#COMMUNICATOR_TOOL_PATH = "/home/anusaaraka/communicator-tool/"
COMMUNICATOR_TOOL_PATH = "/home/sriram/phd/communicator/communicator-tool/"
#read the hindi csv file

#run tamil morph
def run_morph(tamil_snt):
    fp = open(COMMUNICATOR_TOOL_PATH + 'csv-generator/tools/morph/Tamil/tmp', 'w')
    for wd in tamil_snt.split():
        fp.write(wd)
        fp.write('\n')

    fp.close()

    fp_morph = open(COMMUNICATOR_TOOL_PATH+'csv-generator/tools/morph/Tamil/tmp1', 'w')

    cmd = 'lt-proc -c '+ COMMUNICATOR_TOOL_PATH + "csv-generator/tools/morph/Tamil/Tamilmorph_KP_CALTS_030917.mo < " + COMMUNICATOR_TOOL_PATH + "csv-generator/tools/morph/Tamil/tmp"
    p = subprocess.Popen([cmd], stdout=fp_morph, shell=True)
    ret_code = p.wait()
    fp_morph.flush()
    fp_morph.close()

    with open(COMMUNICATOR_TOOL_PATH+'csv-generator/tools/morph/Tamil/tmp1', 'r') as fp:
        tamil_morph = fp.readlines()

    fp.close()
    return tamil_morph





#read the Hindi Telugu parallel sentences

with open(sys.argv[1], 'rb') as fp_csv:
    csv_cont = csv.DictReader(fp_csv)
    
    for row in csv_cont:

        csv_file = row['csv_file'].strip()
        hnd_snt = row['Hindi'].strip()
        tamil_snt = row['Tamil_WX'].strip()

        #run tamil morph
        tamil_morph = run_morph(tamil_snt)

        #read csv file and convert it to wx
        csv_file_path = COMMUNICATOR_TOOL_PATH+'user_csv/'+csv_file

        if(os.path.isfile(csv_file_path)):
            fp_csv_wx = open(COMMUNICATOR_TOOL_PATH+'csv-generator/tools/converter/tmp_wx', 'w')
            cmd = COMMUNICATOR_TOOL_PATH+'csv-generator/tools/converter/utf8_wx ' + csv_file_path
            p = subprocess.Popen([cmd], stdout=fp_csv_wx,shell=True)
            ret_code = p.wait()
            fp_csv_wx.flush()
            fp_csv_wx.close()

            with  open(COMMUNICATOR_TOOL_PATH+'csv-generator/tools/converter/tmp_wx', 'r') as fp:
                csv_cont = fp.readlines()


        #create tamil csv file

            hnd_wds=csv_cont[1].split(',')
            tamil_wds=tamil_snt.split()

            print tamil_snt

            concept_dic = []
            tamil_csv_1 = []
            tamil_csv_2 = []
            for i in range(0,len(hnd_wds)):

                wd =  tamil_wds[i].strip()
                root = tamil_morph[i].strip().split('/')[-1].split('<')[0].strip()
                pos = tamil_morph[i].strip().split('/')[-1].split('<')[    1].strip('>')
                if(re.search(r'cat:(.*)>\$', pos)):
                    pos = re.search(r'cat:(.*)>\$', pos).group(1)


                vib = tamil_morph[i].strip().split('/')[-1].split('<')[-1].split('>')[0]


                #concept dictionary:
                concept_dic.append([hnd_wds[i].strip(),root+"_1",pos])



                #1st row : word_vibhakti, verb_tam
                if(vib == "cat:det"):
                    tamil_csv_1.append(root)
                else:
                    tamil_csv_1.append(root+"_"+vib)

                #2nd row : word_vibhakti, verb_tam
                tamil_csv_2.append(root+"_1")


                #3rd,4th,5th,6th,7th row copy as it is from hindi.csv
                tamil_csv_3= csv_cont[2].strip()
                tamil_csv_4= csv_cont[3].strip()
                tamil_csv_5= csv_cont[4].strip()
                tamil_csv_6= csv_cont[5].strip()
                tamil_csv_7= csv_cont[6].strip()


            tamil_csv = []
            tamil_csv.append(','.join(tamil_csv_1))
            tamil_csv.append(','.join(tamil_csv_2))
            tamil_csv.append(tamil_csv_3)
            tamil_csv.append(tamil_csv_4)
            tamil_csv.append(tamil_csv_5)
            tamil_csv.append(tamil_csv_6)
            tamil_csv.append(tamil_csv_7)


            print tamil_morph
            fp = open(sys.argv[2],'w')
            for line in tamil_csv:
                fp.write(line+"\n") 
            fp.close()

            #write the cocept dictionary
            fp = open(sys.argv[3],'w')
            for line in concept_dic:
                fp.write(','.join(line)+"\n")

            fp.close()


            #prepare karaka vibhakti mapping
            karak_vib = []
            k_sen =  tamil_csv_7.split(',')
            for i in range(0,len(k_sen)):
                if(k_sen[i] != ''):
                    vid = int(k_sen[i].split(':')[0])
                    vwd = tamil_csv_2[vid-1]
                    vib = tamil_csv_1[i].split('_')[1]
                    karaka = k_sen[i].split(':')[1]

                    #print karaka,vwd,vib
                    karak_vib.append([karaka,vwd,vib])

           
            #write the karaka-vibhakti mapping

            fp = open(sys.argv[4],'w')
            for l in karak_vib:
                fp.write(','.join(l)+'\n')
            fp.close()
            


           
            
