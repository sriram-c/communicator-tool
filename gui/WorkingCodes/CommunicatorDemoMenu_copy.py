#!/bin/bash
#!/usr/bin/python
# -*- coding: utf-8 -*-

import webbrowser
from Tkinter import *
import tkFileDialog
import os
import subprocess
import commands

#######################
## Communicator Tool ##
#######################
class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent        
        self.initUI()

    def initUI(self):

        self.parent.title("Communicator-Interactive-Output")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)        

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)


    def onOpen(self):

        ftypes = [('csv files', '*.csv'), ('All files', '*')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)

    def readFile(self, filename):

        f = open(filename, "r+")
        os.chdir('/home/anusaaraka/create-hindi-parser/chl_to_dmrs')
##        communicatorOut = commands.getoutput("bash run_communicator.sh "+filename)
##        communicatorOut = os.system("bash run_communicator.sh "+str(filename))
		
	global csvText
	csvText = filename
        communicatorOut = subprocess.check_output(['bash run_communicator.sh '+filename], shell=True)
        return filename + "\n" + "\n" + communicatorOut

#####################################	
    	

def main():

    root = Tk()
    ex = Example(root)
    root.geometry("300x250+300+300")
    root.mainloop()
    

##################
## Rel Analyzer ##
##################


def rbind():
    global col1
    col1=[]
    global col2
    col2=[]
    for row in x:
        col1.append(row.split('\t')[0])
	col2.append(row.split('\t')[1])

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
        fileMenu.add_command(label="Open", command=self.onOpen)
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
	
	relWrdRow = col2[col1.index("r.w.g")].split('\n')[0].split(' - ')
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
        fileMenu.add_command(label="Open", command=self.onOpen)
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
master.title("AnuTransKit")

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
    fileUpload=Button(f2, text="Upload RelClaus File", fg="blue", command=reltool)
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
