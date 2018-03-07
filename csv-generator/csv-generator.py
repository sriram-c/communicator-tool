
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#######################################################################
#                           README
#
#    1. USR(Universal Semantic Representation) file structure:
#
#        each usr file should come with a schema which will contain information regarding the rows in the usr file. 
#
#        for e.g.
#
#        schema file: (currently using the default schema given in "../docs/updated_user_csv_guideline.pdf")
#
#        for e.g. current schema file 
#
#            1	grp	Grouping
#            2	concpt_dic	Concept from Concept dictionary
#            3	idx_concpt_dic	Index for Concepts
#            4	catg	Lexical Category (only for proper nouns, pronouns) AND Ontological Information about nouns
#            5	gnp	GNP (Gender, Number, Person) Information
#            6	intra_chk	Intrachunk Dependency Relations
#            7	inter_chk	Interchunk Dependency Relations
#            8	disc_rel	Discourse Relations
#
#    2. Individual sentences in the parallel sentence database will have uniq id.
#        e.g. 
#            id | Eng_sent   id | Hnd_sent   id | Tamil_sent   id | Telugu_sent
#
#    Logic:
#
#    1. Read the Source (Hindi) USR file and the schema and store each rows information in a hash.
#
#    1. Read Source (Hindi) and Target (Tamil) parallel sentence and map the words in the sentences.
#
#    2. Run the Target(Tamil) morph on each word of the Target(Tamil) sentence.
#
#            2.1. mark the root, vibhakti, tam for each word
#
#    3. generate following files for the target language.
#    
#        1.  CSV file
#        2.  Concept-dictionary
#        3.  karaka-vibhakti mapping
#
#
#   Assumption: 
#
#   Source and Target sentences are parallel and word aligned (i.e same number of words in Hindi and Telugu)

#   To Run:
#   python  csv-generator.py   usr-hnd usr-tamil  usr-schema  tamil.usr hnd-tamil-concept.dic karaka-vib 

#   Files Required:

#   usr-hnd : contains the  Hindi sentences with USR id
#   usr-tamil : contains the  Tamil sentences with USR id
#   usr-schema: Contains the usr-schema information

#   Assumption is that for each USR id the corresponding id.usr file is present in the current directory,  for the source language

#    for e.g. 1.usr , 2.usr , 3.usr

#    File output:

#   tamil.usr:  File contains the Tamil usr file for the corresponding Hindi usr file
#   hnd-tamil-concept.dic: File contains the concept dictionary for Hindi and Tamil sentence pairs.
#   karaka-vib: karaka and vibhakti mapping for  Hindi and Tamil 
    
   
#######################################################################


import sys
import csv
import subprocess
import os.path
import re


#path for communicator tool
COMMUNICATOR_TOOL_PATH = "/home/sriram/phd/communicator/communicator-tool/"

#Function to run tamil morph in Apertium format

def run_morph(tamil_snt):

    #write the words into a file
    fp = open(COMMUNICATOR_TOOL_PATH + 'csv-generator/tools/morph/Tamil/tmp', 'w')
    for wd in tamil_snt.split():
        fp.write(wd)
        fp.write('\n')
    fp.close()

    #open a file to store the morph output
    fp_morph = open(COMMUNICATOR_TOOL_PATH+'csv-generator/tools/morph/Tamil/tmp1', 'w')

    #command to run the tamil apertium morph in command line
    cmd = 'lt-proc -c '+ COMMUNICATOR_TOOL_PATH + "csv-generator/tools/morph/Tamil/Tamilmorph_KP_CALTS_030917.mo < " + COMMUNICATOR_TOOL_PATH + "csv-generator/tools/morph/Tamil/tmp"
    p = subprocess.Popen([cmd], stdout=fp_morph, shell=True)
    ret_code = p.wait()
    fp_morph.flush()
    fp_morph.close()

    #read the morph output from the file.
    with open(COMMUNICATOR_TOOL_PATH+'csv-generator/tools/morph/Tamil/tmp1', 'r') as fp:
        tamil_morph = fp.readlines()
    fp.close()

    #return the morph output
    return tamil_morph


#read usr schema file and and usr file and store each row information in a hash
with open(sys.argv[3], 'rb') as fp:
    usr_schema = fp.readlines()
fp.close()
#read the src (Hindi) and Target (Tamil) parallel sentences

#read src sent with id.
src_id_snt={}
with open(sys.argv[1], 'rb') as fp:
    src_snts_id = fp.readlines()
    for line in src_snts_id:
        src_id = line.strip().split('\t')[0]
        src_snt = line.strip().split('\t')[1]
        src_id_snt[src_id] = src_snt

fp.close()

#read target sent with id.
trg_id_snt={}
with open(sys.argv[2], 'rb') as fp:
    trg_snts_id = fp.readlines()
    for line in trg_snts_id:
        trg_id = line.strip().split('\t')[0]
        trg_snt = line.strip().split('\t')[1]
        trg_id_snt[trg_id] = trg_snt

fp.close()


#for each snt in trg and src,  align the words  run morph on each target word.
for key in trg_id_snt:



    usr_id = key

    trg_snt = trg_id_snt[usr_id]
    src_snt = src_id_snt[usr_id]



    #read the usr file for the sent
    #    using the  current schema file 
    #
    #            1	grp	Grouping
    #            2	concpt_dic	Concept from Concept dictionary
    #            3	idx_concpt_dic	Index for Concepts
    #            4	catg	Lexical Category (only for proper nouns, pronouns) AND Ontological Information about nouns
    #            5	gnp	GNP (Gender, Number, Person) Information
    #            6	intra_chk	Intrachunk Dependency Relations
    #            7	inter_chk	Interchunk Dependency Relations
    #            8	disc_rel	Discourse Relations
    #


    #read the usr file with the usr_id (i.e. 1.usr , 2.usr etc..)
    with open(str(usr_id)+".usr") as fp:
        usr_cont = fp.readlines()
    fp.close()

    #put the info in source usr file into a hash
    src_usr_hash = {}
    for i in range(0, len(usr_cont)):
        key = usr_schema[i].split('\t')[1].strip()
        usr_value = usr_cont[i].strip()
        src_usr_hash[key]=usr_value

    
    #run the target (Tamil) morph
    trg_morph = run_morph(trg_snt)

    #for each sent in src(HIndi) create the usr file in target(Tamil) 

    #read src words from the 1st row of usr (grouping) assuming the lwg is already done
    #if last word is "." don't count it on wds list
    src_wds = []
    for wds in src_usr_hash['grp'].split(','):
        if (wds != "."):
            src_wds.append(wds)

    #split the target(Tamil) sentence to get the words
    trg_wds=trg_snt.split()

    
    #create the target usr hash
    trg_hash = {}

    #initialise the hash with all the row information in usr-schema
    for i in range(0,len(usr_schema)):
        key = usr_schema[i].split('\t')[1].strip()
        trg_hash[key] = ""





    #create concept dictionary for target language
    concept_dic = []

    #for each word in source sent process for target language
    for i in range(0,len(src_wds)):


            #get word ,root, pos from morph o/p of the target language

            wd =  trg_wds[i].strip()

            root = trg_morph[i].strip().split('/')[-1].split('<')[0].strip()

            pos = trg_morph[i].strip().split('/')[-1].split('<')[    1].strip('>')

            #if the pos format is in "cat:<  >" then do the regular expression

            if(re.search(r'cat:(.*)>\$', pos)):
                pos = re.search(r'cat:(.*)>\$', pos).group(1)

            #vibhakti information from morph o/p

            vib = trg_morph[i].strip().split('/')[-1].split('<')[-1].split('>')[0]


            #concept dictionary:
            concept_dic.append([src_wds[i].strip(),root+"_1",pos])



            #write to the target hash in order of the usr schema provided.
            # for each row in the usr schema information put it as it is

            # if vib is determiner don't write it otherwise add it to the root word
            # incase of verb write the root_tam
            # so 1st row will contain  word_vibhakti, verb_tam

            if(vib == "cat:det"):
                if (trg_hash['grp'] == ""):
                    trg_hash['grp'] = root
                else:
                    trg_hash['grp'] = trg_hash['grp']+","+root

            else:
                if (trg_hash['grp'] == ""):
                    trg_hash['grp'] = root+"_"+vib
                else:
                    trg_hash['grp'] = trg_hash['grp']+","+root+"_"+vib

            #2nd row : concept dictionary  (word_vibhakti, verb_tam)
            if(trg_hash['concpt_dic'] == ""):
                trg_hash['concpt_dic'] = root+"_1"
            else:
                trg_hash['concpt_dic'] = trg_hash['concpt_dic']+","+root+"_1"



            #as of now for  Hindi- Tamil pair
            # other rows  (i.e 3rd,4th,5th,6th,7th) are same so copy as it is from source (hindi.usr)

            trg_hash['idx_concpt_dic'] = src_usr_hash['idx_concpt_dic'].strip()
            trg_hash['catg'] = src_usr_hash['catg'].strip()
            trg_hash['gnp'] = src_usr_hash['gnp'].strip()
            trg_hash['intra_chk'] = src_usr_hash['intra_chk'].strip()
            trg_hash['inter_chk'] = src_usr_hash['inter_chk'].strip()





    #write the target usr file for this sentence in the order given in usr-schema file
    fp = open(sys.argv[4],'w')
    for i in range(0, len(usr_schema)):
        key = usr_schema[i].split('\t')[1].strip()
        line = trg_hash[key]
        fp.write(line+"\n") 
    fp.close()

    #write the cocept dictionary
    fp = open(sys.argv[5],'w')
    for line in concept_dic:
        fp.write(','.join(line)+"\n")

    fp.close()


    #prepare karaka vibhakti mapping
    #read the karaka relation in src usr and map it to the vibhakti in the target words

    karak_vib = []

    k_sen =  trg_hash['inter_chk'].split(',')

    for i in range(0,len(k_sen)):
        if(k_sen[i] != ''):

            #need to understand vid -1 
            #in the 7th row (intra_chk) find the verb id/wd
            # e.g. ['5:k1', '', '5:k2', '5:k7t', '']

            vid = int(k_sen[i].split(':')[0])

            # since counting is from 0 so -1 from actual id
            vwd = trg_hash['concpt_dic'][vid-1]

            #vibhakti from the group word
            vib = trg_hash['grp'].split(",")[i].split('_')[1]
            karaka = k_sen[i].split(':')[1]

            #print karaka,vwd,vib
            karak_vib.append([karaka,vwd,vib])


#write the karaka-vibhakti mapping

fp = open(sys.argv[6],'w')
for l in karak_vib:
    fp.write(','.join(l)+'\n')
fp.close()



           
            
