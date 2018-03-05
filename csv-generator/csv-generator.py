
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#######################################################################

README

    1. USR(Universal Semantic Representation) file structure:

        each usr file should come with a schema which will contain information regarding the rows in the usr file. 

    2. Individual sentences in the parallel sentence database will have uniq id.
        e.g. 
            id | Eng_sent   id | Hnd_sent   id | Tamil_sent   id | Telugu_sent

    Logic:

    1. Read the Source (Hindi) USR file and the schema and store each rows information in a hash.

    1. Read Source (Hindi) and Target (Tamil) parallel sentence and map the words in the sentences.

    2. Run the Target(Tamil) morph on each word of the Target(Tamil) sentence.

            2.1. mark the root, vibhakti, tam for each word

    3. generate following files for the target language.
    
        1.  CSV file
        2.  Concept-dictionary
        3.  karaka-vibhakti mapping


    Assumption: 

    Source and Target sentences are parallel and word aligned (i.e same number of words in Hindi and Telugu)

   
#######################################################################


import sys
import csv
import subprocess
import os.path
import re

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


#read csv (usr) schema
with open(sys.argv[3], 'rb') as fp:
    csv_schema = fp.readlines()
fp.close()

#read the src (Hindi) and Target (Tamil) parallel sentences

#read src sent with id.
src_id_snt={}
with open(sys.argv[1], 'rb') as fp:
    src_snts_id = fp.readlines()
    for line in src_snts_id:
        src_id = line.strip().split('\t')[0]
        src_snt = line.strip().split('\t')[1]
        src_id_snt[id] = src_snt

fp.close()

#read target sent with id.
trg_id_snt={}
with open(sys.argv[2], 'rb') as fp:
    trg_snts_id = fp.readlines()
    for line in trg_snts_id:
        trg_id = line.strip().split('\t')[0]
        trg_snt = line.strip().split('\t')[1]
        trg_id_snt[id] = trg_snt

fp.close()


#for each snt in trg and src do the processing
for key in trg_id_snt:

    UsrId = key

    trg_snt = trg_id_snt[UsrId]
    src_snt = src_id_snt[UsrId]

    #run the target (Tamil) morph
    tamil_morph = run_morph(trg_snt)

    #read csv file and convert it to wx
    csv_file_name = UsrId + ".csv"
    csv_file_path = COMMUNICATOR_TOOL_PATH+'user_csv/'+csv_file_name


    #convert to wx
    if(os.path.isfile(csv_file_path)):
        fp_csv_wx = open(COMMUNICATOR_TOOL_PATH+'csv-generator/tools/converter/tmp_wx', 'w')
        cmd = COMMUNICATOR_TOOL_PATH+'csv-generator/tools/converter/utf8_wx ' + csv_file_path
        p = subprocess.Popen([cmd], stdout=fp_csv_wx,shell=True)
        ret_code = p.wait()
        fp_csv_wx.flush()
        fp_csv_wx.close()

        with  open(COMMUNICATOR_TOOL_PATH+'csv-generator/tools/converter/tmp_wx', 'r') as fp:
            csv_cont = fp.readlines()


    for line in csv_schema:





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
            


           
            
