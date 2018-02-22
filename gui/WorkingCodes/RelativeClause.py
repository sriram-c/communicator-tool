#!/bin/bash
#!/usr/bin/python
# -*- coding: utf-8 -*-

import webbrowser
from Tkinter import *
import tkFileDialog
import os
import subprocess
import commands
from collections import OrderedDict
import re
import tkMessageBox
import sys

CommunicatorPath="/home/anusaaraka/communicator-tool"


def rbind(): # creates a two lists for two columns in the header txt file where values are seperated by a "\t" character
    global col1 # will take the information such as s1 s2 s.g... etc as a list.
    col1=[]
    global col2 # will take the information regarding the sentence info, combination info in the last line etc.
    col2=[]
    for row in x:
        col1.append(row.split('\t')[0])
        col2.append(row.split('\t')[1])

class relclausehandler():

    directory = os.path.dirname(os.path.abspath(sys.argv[1]))
    
    f = open(sys.argv[1],'r')
    
    os.chdir(CommunicatorPath)
    
    userdict= open(CommunicatorPath+'/dic/concept_dictionary_user.txt',"r")
    
    userdict=userdict.readlines()
        
    
        
    global x
    x=f.readlines()
    rbind()
        # create a new dictionary: headerdict = {'col1key' : {'info': 'col2value', 'indexdic': {'id': 'indexedItem'}, 'execoutput':''}}
    headerdict = OrderedDict()
    for row in x:
            headerdict[row.split('\t')[0]] = row.split('\t')[1].strip('\n') # headerdict has left column as key and right column as value:

        
# conditionally store values for each key from headerdic in the following dictionary format into "outputdic"
# outputdic = {'col1key' : {'info': 'col2value', 'indices': {'id': 'indexedItem'}, 'execoutput':''}}
    outputdic=OrderedDict()
    for key in headerdict:
        

        if len(key) == 2: # fetches the keys such as "s1", "s2" etc. and stores them as keys of the dict
            outputdic[key] = {}
            sent = headerdict[key]
            outputdic[key]['info'] = sent

            indexdic = {} # To fetch any indexed word in the sentences and stores them as id:word pair in dictionary format (inside indexdic)
            for num in '123456789':
                if num in sent:
                    indexed_word = re.findall('[A-Za-z]+'+'-'+num, sent)
                    indexed_word = indexed_word[0].replace('-'+num,'')
                           
                    indexdic[num] = indexed_word
                    outputdic[key]['info'] = outputdic[key]['info'].replace('-'+num,'')
                    for char in '~@#$^*_-+}{[]':
                        if char in outputdic[key]['info']:
                            outputdic[key]['info'] = outputdic[key]['info'].replace(char,' ')


            outputdic[key]['csvfile'] = outputdic[key]['info'].replace(' ','_')+'_user.csv'



            outputdic[key]['indices'] = indexdic
            outputdic[key]['execoutput'] = ''

            #return outputdic[key]['csvfile']




        if '.g' in key and len(key) > 3: # matches keys such as "s1.g", "s2.g'" and so on.
            outputdic[key] = {}
            value = headerdict[key]
            outputdic[key]['info'] = value
                

            if 't(' in value:

                sentusercsv = outputdic[key.split('.')[0]]['csvfile']
                    #return sentusercsv
                    #return outputdic
                    
                communicatorOut = subprocess.check_output(['bash run_communicator.sh '+directory+'/'+sentusercsv], shell=True)
                
                   
                    
                #return communicatorOut
                    
                comOutList=[]
                    
                for sent in communicatorOut.split('\n')[len(communicatorOut.split('\n'))-2:None:-1]:
                    if ' ' not in sent:
                        break
                    elif ' ' in sent:
                        comOutList.append(sent)
                           
                   
       
                def popupeditor(filelocation):
                        os.system('gedit -s '+ filelocation)

       
        #if len(my_output) != 0:
            #return my_output
                #global my_finaloutput

                if len(comOutList) > 0:
           
                    my_finaloutput = comOutList[0]
                    
                    #print "\nmy_finaloutput::::\n", my_finaloutput
                    
           
                elif len(comOutList) == 0:
                    os.chdir(CommunicatorPath+'/output')
                    #os.system('ls')
                        
                    #sentname = filename.split('/')[len(filename.split('/'))-1]
                        #return sentname
                    newdmrsfile= sentusercsv.replace('_user.csv','_dev.csv_new_dmrs.txt')
                        
                        #return newdmrsfile
                        #return sentusercsv
                    os.system('gedit -s '+ newdmrsfile)
                    
                    os.chdir('..')
           
                   
                    my_finaloutput = subprocess.check_output(['bash run_mod_dmrs.sh '+sentusercsv.replace('_user.csv','_dev.csv')], shell=True)
                    
                    #print '\nhello hello hello :::\n'
                    #print my_finaloutput
                    comOutList.append(my_finaloutput)
                    
                    if '\n' in my_finaloutput:    
                        for sent in my_finaloutput.split('\n')[len(communicatorOut.split('\n'))-2:None:-1]:
                            if ' ' not in sent:
                                break
                            elif ' ' in sent:
                                comOutList.append(sent)
                            #comOutList = comOutList[0]
                        #return comOutList
                        	
                            
                #print 'comOutList', comOutList

                sentid = key.split('.')[0]

                # comOutList_line1 = comOutList

                sentcsv = sentusercsv.replace('user.csv','dev.csv').replace('__','_')

                indexdic = {}

                csv = open(CommunicatorPath+'/'+sentcsv,'r')

                csvlines = csv.readlines()

                for index in outputdic[sentid]['indices']:
                    indexedword = outputdic[sentid]['indices'][index]

                    for value in csvlines[0].split(','): # takes the 2nd row of dev.csv
                        if indexedword.split(' ')[-1] in value: # if the last indexed word is found in that column
                            valueindex = csvlines[0].split(',').index(value)
                            engword = csvlines[1].split(',')[valueindex]

                            
                            #splitsent = comOutList_line1.split(engword)
                            execoutput = comOutList[0].replace(engword,engword+'-'+index)
                               
                            outputdic[key]['execoutput'] = execoutput #execoutput
                            
                #devcsv.close()

                outputdic[key]['indices'] = indexdic
                
            #print "\noutputdic::::\n", outputdic


            #print '\n\noutputdic\n\n', outputdic
            
            if 's(' in value:

                splitvalue = value.split(',')
                splitvalue1 = splitvalue[0]
                splitvalue2 = splitvalue[1]

                sentid = splitvalue2[0:splitvalue2.index(')')]

                sentence = outputdic[sentid]['execoutput']

                indexdic = {}

                #return sentence

                for indexedword in re.findall(r"\S+-\d", sentence):
                    for index in re.findall(r"-\d+",indexedword):
                        word = indexedword.replace(index, '')
                        #return word

                        indexdic[index]=word

                #return indexdic

                outputdic[key]['indices'] = indexdic

                index = splitvalue1[splitvalue1.index('*')+1:len(splitvalue1)]

                word = outputdic[key]['indices'][index]

                splitoutput = sentence.split(index)

                for item in splitoutput:
                    if item == '':
                        splitoutput[splitoutput.index(item)]=word

                part = splitvalue2[splitvalue2.index('[')+1:len(splitvalue2)-1]

                outputdic[key]['execoutput'] = splitoutput[int(part)-1]

            #return outputdic

            if 'd(' in value:

                splitvalue = value.split(',')
                splitvalue1 = splitvalue[0]
                splitvalue2 = splitvalue[1]
                    
                sentid = splitvalue2[0:splitvalue2.index('g')+1]

                sentence = outputdic[sentid]['execoutput']
                    #return sentence

                indexdic = {}

                for indexedword in re.findall(r"\S+-\d+", sentence):
                    #print "\nindexedword ::::\n",indexedword
                    for index in re.findall(r"-\d+",indexedword):
                        #print "\nindex::::\n",index
                        word = indexedword.replace(index,'')

                        indexdic[index.replace('-','')]=word

                outputdic[key]['indices'] = indexdic

                index = splitvalue1[splitvalue1.index('*')+1:len(splitvalue1)]

                #return indexdic


                word = outputdic[key]['indices'][index.replace('-','')]
                
                #replacegroup
                
                

                outputdic[key]['execoutput'] = sentence.replace(sentence[0:sentence.index(indexedword)],'').replace(indexedword,'')
                
                


            if 'a(' in value:

                splitvalue = value.split(',')
                splitvalue1 = splitvalue[0]
                splitvalue2 = splitvalue[1]

                sentid = splitvalue2[0:value.index(')')]

                sentence = outputdic[sentid.strip(')')]['execoutput']

                if '^' in splitvalue1:
                    word = splitvalue1[splitvalue1.index('^')+1:len(splitvalue1)]
    
                    outputdic[key]['execoutput'] = word+' '+sentence

        #return outputdic
            
        if key == 's.g':
            outputdic[key] = {}
            
            #print "headerdict['s.g']", str(headerdict[key])
            value = headerdict[key]
            keylist = value.split('+')
            #return value.split('+')
            outputdic[key]['info'] = value
            #return outputdic[key]['info']
            #return outputdic

            outputlist = []

            for word in keylist:
                if '.g' in word:
                    outputlist.append(outputdic[word]['execoutput'].strip('.\n'))
                #else:
                    #outputlist.append(word)
                        
                
                #return outputlist
            outputdic[key]['execoutput'] = ' '.join(outputlist).replace('  ',' ')


    print '\n\nOutput ::::::::::::::::\n\n', outputdic[key]['execoutput']+'.','\n\n'
    
    #print outputdic


relclausehandler()

    








        
    #return relsentset, '\n\n', sg
    
    # Do operations according to types of key in the dictionary
    
    





    


