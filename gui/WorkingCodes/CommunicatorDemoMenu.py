#!/bin/bash
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Dr. Abhijit Debnath, RS, Anusaaraka Lab, IIIT-Hyd.

import webbrowser
from Tkinter import *
import tkFileDialog
import os
import subprocess
import commands
from collections import OrderedDict
import re
##########################
## 1. Communicator Tool ##
##########################
class Example(Frame): # FrameClass in which the given button will open the File Dialogue Interface to upload a usercsv

    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent        
        self.initUI()

    def initUI(self):

        self.parent.title("Communicator-Interactive-Output") # Name of communicator tool Window 
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)        

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)


    def onOpen(self):

        ftypes = [('csv files', '*.csv'), ('All files', '*')] # File options which will be default available to select.
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        fl = dlg.show() # Creates a popup dialogue window having a FILE upload option.

        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)

    def readFile(self, filename):

        f = open(filename, "r+") # Open the file that has been selected through file dialogue in Tkinter.
        os.chdir('/home/anusaaraka/create-hindi-parser/chl_to_dmrs') # Target the directory to whichever folder location the run_communicator.sh file is located
		
	
        communicatorOut = subprocess.check_output(['bash run_communicator.sh '+filename], shell=True) # Store the output of the communicator.sh command that has been run upon the filename(i.e., the user.csv).
        return filename + "\n" + "\n" + communicatorOut # In the popup window, displays the list of probable english sentences preceded by the steps of executions (advanced level information).

#####################################	
    	

def main(): # A command that the relevant button can call and execute.

    root = Tk()
    ex = Example(root) # links the "Example" class which contains the plain Hindi to English Translation display commands.
    root.geometry("300x250+300+300") # Fixes a proper 2D display dimension for the display of the Translation Space.
    root.mainloop() # executes the contents connected to the root.
    

#####################
## 2. Rel Analyzer ##
#####################

# Relative clause analyser takes a Header file in a text format. That text format has two major columns of information. So rbind seperates these two sets of information columnwise by creating a pair of lists.

def rbind(): # creates a two lists for two columns in the header txt file where values are seperated by a "\t" character
    global col1 # will take the information such as s1 s2 s.g... etc as a list.
    col1=[]
    global col2 # will take the information regarding the sentence info, combination info in the last line etc.
    col2=[]
    for row in x:
        col1.append(row.split('\t')[0])
	col2.append(row.split('\t')[1])

class Example4(Frame): # Starts a class of operation definitions for the simple relative clause file like "1. Communicator tool".

	    
    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent        
        self.initUI()

    def initUI(self):

        self.parent.title("Relative Clause Translator")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Simple Relative Clause", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)        

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)


    def onOpen(self):

        ftypes = [('text files', '*.txt'), ('All files', '*')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)

    def readFile(self, filename):

        f = open(filename, "r")
        directory = os.path.dirname(os.path.abspath(filename))
        os.chdir('/home/anusaaraka/create-hindi-parser/chl_to_dmrs/')
        conceptdic=open('dic/concept_dictionary_user.txt')
        myconcepts= conceptdic.readlines()
        
        
	global x
	x=f.readlines()
	rbind()
	
	# Taking the word-combination info at the last row into 'relsentset'
	relsentset = col2[col1.index("s.g")].split('\n')[0].split('+')
	                
	# Fetch words to be combined according to formula in 'relsentset'
	for x in col1: 
	    if x in str(relsentset[0]): 
	        global sent1
	        sent1 = col2[col1.index(x)].split('.\n')[0]
	        sent1usercsv = '_'.join(sent1.split())+'_user.csv'
	    if x in str(relsentset[2]):
	        global sent2
	        sent2 = col2[col1.index(x)].split('.\n')[0]
	        sent2usercsv = '_'.join(sent2.split())+'_user.csv'
	
	global engComptizr
	engComptizr = []
	engComptizr.append(relsentset[1])
	
	global wrd2delete
	
	relWrdRow = col2[col1.index("r.w.g2")].split('\n')[0].split(' - ')
	wrd2delete= relWrdRow[1]
	
	
	communicatorOut1 = subprocess.check_output(['bash run_communicator.sh '+directory+'/'+sent1usercsv], shell=True)
        
        communicatorOut2 = subprocess.check_output(['bash run_communicator.sh '+directory+'/'+sent2usercsv], shell=True)
        
# create a collection of last outputs of the communicator tool
        
        global comOut1List
        comOut1List=[]
        global comOut2List
        comOut2List=[]
        
        for sent in communicatorOut1.split('\n')[len(communicatorOut1.split('\n'))-2:None:-1]:
            if ' ' not in sent:
                break
            
            else:
                if ' ' in sent:
                    comOut1List.append(sent)
                    
        for sent in communicatorOut2.split('\n')[len(communicatorOut2.split('\n'))-2:None:-1]:
            if ' ' not in sent:
                break
            
            else:
                if ' ' in sent:
                    comOut2List.append(sent.replace(wrd2delete,''))
        
        
        global finalrelcl
        global finaldisplay
        finaldisplay = []
        for sent1 in comOut1List:
            listedsent = []
            listedsent.append(sent1)
            for sent2 in comOut2List:
                listedsent2 = []
                listedsent2.append(sent2)
                finalrelcl = listedsent + engComptizr + listedsent2
                finalres = ' '.join(finalrelcl)
                finalres2= finalres.replace('.', '')
                

                finaldisplay.append(finalres2)
        
        return '\n'.join(finaldisplay)+'\n'
                
        #finalrelcl = comOut1List + engComptizr + comOut2List
        #finalres = ' '.join(finalrelcl)
        #finalres2= finalres.replace('.', '')
        
        
        #return finalres2
        
        
        
###################        
        
def reltool2():

    root4 = Tk()
    ex = Example4(root4)
    root4.geometry("300x250+300+300")
    root4.mainloop() 
    


##########################
## Complex Rel Analyzer ##
##########################




class Example2(Frame):

	    
    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent        
        self.initUI()

    def initUI(self):

        self.parent.title("Relative Clause Translator")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Complex Relative Clause", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)        

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)


    def onOpen(self):

        ftypes = [('csv files', '*.txt'), ('All files', '*')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)

    def readFile(self, filename):

        f = open(filename, "r")
        directory = os.path.dirname(os.path.abspath(filename))
        os.chdir('/home/anusaaraka/create-hindi-parser/chl_to_dmrs/')
        userdict= open('/home/anusaaraka/create-hindi-parser/chl_to_dmrs/provisional_dics/concept_dictionary_user.txt',"r")
        userdict=userdict.readlines()
        
        
	global x
	x=f.readlines()
	rbind()
	
	# Taking the word-combination info at the last row into 'relsentset'
	relsentset = col2[col1.index("s.g")].split('\n')[0].split('+')
	
	# Creating a dictionary of keys using the values in relsentset
	global sg # globally create a dictionary
	sg = OrderedDict()
	for item in relsentset:
	    sg[item]='None'
	    
	#return relsentset, '\n\n', sg
	
	# Do operations according to types of key in the dictionary
	
	# This code looks at the values of the second column of the last row (as splitted by "+" symbol) as keys of the dictionary "sg" and does the following operations according to given conditions.
	for key in sg:
	    if '_' in key: # if an index id is available in a key (indicated by "_" + index number) then it identifies the mentioned sub-sentence-id in that Key and finds the sub-sentence and looks for a word having that same index attached to it.
	        for x in col1:
	            if x in key:
	                wordlist=col2[col1.index(x)].split('.\n')[0]
	                wordlist=wordlist.split()
	                for word in wordlist:
	                    if '_'+key[key.index('_')+1] in word:
	                       global indexedwrd
	                       indexedwrd=word.split('_')[0]
	                       for string in userdict:
	                           if word ==  string.split('\n')[0].split(',')[0]:
	                               meaning = string.split('\n')[0].split(',')[1].split('_')[0]
	                               #return meaning
	                               sg[key]= meaning
	                           else:
	                               sg[key]=indexedwrd
	                               #return indexedwrd
	                               #return sg
	                               
	    
	    elif len(re.findall('[A-Za-z]+',key)) == 1:
	        sg[key] = key
	        
	    elif '.g' in key:
	        
	        sentid = key[key.index('.')-1]
	        for item in col1:
	            if "r.w.g"+sentid in item:
	                wrd2delRow = col2[col1.index("r.w.g"+sentid)].split('\n')[0].split(' - ')
	                #global wrd2del
	                global wrd2del
	                wrd2del = wrd2delRow[1]
	                
	            #else:
	                #wrd2del = '' 
	                #return wrd2del, sentid
	                 
	        
	        for x in col1:
	            if x+'.g' in key:
	                global sent
	                sent = col2[col1.index(x)].split('.\n')[0].split()
	            
	                for wrd in sent:
	                    if '_' in wrd:
	                        word = wrd.split('_')[0]
	                        sent[sent.index(wrd)]=word
	                        
	                sentusercsv = '_'.join(sent)+'_user.csv'
	                communicatorOut = subprocess.check_output(['bash run_communicator.sh '+directory+'/'+sentusercsv], shell=True)        
	                 
	                global comOutList
	                comOutList=[]
	                
	                for sent in communicatorOut.split('\n')[len(communicatorOut.split('\n'))-2:None:-1]:
	                    if ' ' not in sent:
	                        break
	                    else:
	                        if ' ' in sent:
	                            #for item in col1:
	                                #if "r.w.g"+sentid in item:
	                                    #wrd2delRow = col2[col1.index("r.w.g"+sentid)].split('\n')[0].split(' - ')
	                                    #global wrd2del
	                                    #wrd2del = wrd2delRow[1]
	                            
	                            comOutList.append(sent.replace(wrd2del,'').replace(wrd2del.capitalize(),'').replace('.',''))
	                                    #return wrd2del, comOutList
	        
	        sg[key] = comOutList                    
	        #return comOutList       
	                
	                #return communicatorOut
	                
	                

	                #return sentusercsv
	                
	                    
	                    
	                    #itemlist = re.findall('_\d',wrd)
	                    #for item in itemlist:
	                        #if item in wrd:
	                            #wrd.replace(item,'')
	                            #return sent
	                            
	                
	        
	        
	        
	        
	        
	finalsent = []
	for key in sg:
	    if isinstance(sg[key], str):
	        finalsent.append(sg[key])
	    elif isinstance(sg[key], list):
	        finalsent.append(sg[key][0].replace('  ',''))
	            
	return ' '.join(finalsent).replace('  ',' ')+'\n\n'
        os.chdir(directory)
	                           
	                       #return indexedwrd
	                       
	                   
        
        
###################        
        
def reltool():

    root2 = Tk()
    ex = Example2(root2)
    root2.geometry("300x250+300+300")
    root2.mainloop() 
    
    
    


    
#################################
## Conditional Clause Analyzer ##
#################################



class Example3(Frame):

	    
    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent        
        self.initUI()

    def initUI(self):

        self.parent.title("Relative Clause Translator")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Conditional Clause", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)        

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)


    def onOpen(self):

        ftypes = [('csv files', '*.txt'), ('All files', '*')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)

    def readFile(self, filename):

        f = open(filename, "r")
        directory = os.path.dirname(os.path.abspath(filename))
        os.chdir('/home/anusaaraka/create-hindi-parser/chl_to_dmrs/')
        
	global x
	x=f.readlines()
	rbind()
	
	condsentset = col2[col1.index("s.g")].split('\n')[0].split('+')
	
	for x in col1:
	    if x in str(condsentset[1]):
	        global condsent1
	        condsent1 = col2[col1.index(x)].split('.\n')[0]
	        condsent1usercsv = '_'.join(condsent1.split())+'_user.csv'
	    if x in str(condsentset[3]):
	        global condsent2
	        condsent2 = col2[col1.index(x)].split('.\n')[0]
	        condsent2usercsv = '_'.join(condsent2.split())+'_user.csv'
	
	global ifword
	ifword = []
	ifword.append(condsentset[0])
	
	global thenword
	
	thenword = []
	thenword.append(condsentset[2])
	
	
	communicatorOut1 = subprocess.check_output(['bash run_communicator.sh '+directory+'/'+condsent1usercsv], shell=True)
        
        communicatorOut2 = subprocess.check_output(['bash run_communicator.sh '+directory+'/'+condsent2usercsv], shell=True)
        
# create a collection of last outputs of the communicator tool
        
        global comOut1List
        comOut1List=[]
        global comOut2List
        comOut2List=[]
        
        for sent in communicatorOut1.split('\n')[len(communicatorOut1.split('\n'))-2:None:-1]:
            if ' ' not in sent:
                break
            
            else:
                if ' ' in sent:
                    comOut1List.append(sent)
                    
        for sent in communicatorOut2.split('\n')[len(communicatorOut2.split('\n'))-2:None:-1]:
            if ' ' not in sent:
                break
            
            else:
                if ' ' in sent:
                    comOut2List.append(sent)
        
        global finalcondcl
        global finaldisplay
        finaldisplay = []
        for sent1 in comOut1List:
            listedsent = []
            listedsent.append(sent1)
            for sent2 in comOut2List:
                listedsent2 = []
                listedsent2.append(sent2)
                finalcondcl = ifword + listedsent + thenword + listedsent2
                finalres = ' '.join(finalcondcl)
                finalres2= finalres.replace('.', '')
                
                finaldisplay.append(finalres2)
        
        return '\n'.join(finaldisplay)+'\n'
        

####################

def condtool():

    root3 = Tk()
    ex = Example3(root3)
    root3.geometry("300x250+300+300")
    root3.mainloop()


####################
    
master = Tk()
master.title("AnuTransKit") # TitleDisplay of Main window

###################

###################
def csvEditor():
	os.system('gedit -s '+ csvText)



def displayInterface():

    f1 = Frame(master, borderwidth=10)
    f2 = Frame(master, borderwidth=10)
    f3 = Frame(master)
    f4 = Frame(master)
    frame1 = Frame(master, borderwidth=10)
##
##
    for frame in (f1, f2, f3, f4, frame1):
        frame.grid(row=0, column=0, sticky='news')

    def raise_frame(frame):
        frame.tkraise()

    filemenu = Menu(master)
    filemenu.add_command(label="ComTool", command=lambda:raise_frame(frame1))

    useridLabel= Label(frame1, text="Insert your text below:\n", anchor=N, justify=CENTER)
    useridLabel.pack(anchor=N,)

## 1.Input txt file containing IndianLg Data
# Entry Options:
    
    # a. Typing in Entry Box

    txtentry= Entry(frame1, width=50)
    txtentry.pack(side=TOP)
    
    # b. Upload of Txt File (value is stored in the variable "text" usable later) (Socket)

    fileUpload=Button(frame1, text="Upload User-CSV", fg="blue", command=main)
    fileUpload.pack(side = TOP, anchor=N)
    
   
    fileUpload=Button(frame1, text="Edit Uploaded CSV", fg="brown", command=csvEditor)
    fileUpload.pack(side = TOP, anchor=N)

## Hindi ComplexSent Catenator:    
    filemenu.add_command(label="Complex", command=lambda:raise_frame(f2))
    fileUpload=Button(f2, text="Upload Complex RelClaus File", fg="blue", command=reltool)
    fileUpload.pack(side = TOP)
    fileUpload=Button(f2, text="Upload Simple RelClaus File", fg="blue", command=reltool2)
    fileUpload.pack(side = TOP)
    fileUpload2=Button(f2, text="Upload Conditional-Clause File", fg="green", command=condtool)
    fileUpload2.pack(side = TOP)
## Help Guidelines:    
    filemenu.add_command(label="Help", command=lambda:raise_frame(f1))
    text=Text(f1, font=('Arial', 14, 'normal') , width=60, height=10)
    text.pack()
    text.insert(END,"Usage Guidelines: \n\n1. Communicator tool: \nIt is an interface that is capable of taking ...user.csv prepared for a Hindi sentence as input and display the most probable options of English Translations for that sentence. \nPlease use the only the \'File\' option inside the pop up window to upload a csv file everytime. \n\n1.a Advanced Mode: \n\nIf the given set of output has only wrong sentences or if you just want to play with the csv information, please click the \'Edit Uploaded CSV\' and edit required entries in the appropriate row and column as per CSV creation guidelines")
    
    
    
    master.config(menu=filemenu)
    master.mainloop()

displayInterface()
