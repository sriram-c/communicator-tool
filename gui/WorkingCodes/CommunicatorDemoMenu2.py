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
##########################
## 1. Communicator Tool ##
##########################

CommunicatorPath='/home/mangal/communicator-tool'


class Example(Frame): # FrameClass in which the given button will open the File Dialogue Interface to upload a usercsv
    comOut1List=[]
     
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
        
        directory = os.path.dirname(os.path.abspath(filename))
        os.chdir(CommunicatorPath) # Target the directory to whichever folder location the run_communicator.sh file is located
        sentname = filename.split('/')[len(filename.split('/'))-1]
        sentname = 'Sentence: '+sentname.replace('_user.csv','').replace('_',' ')
        outlist=[]
        if var0.get()==1:
            outlist.append("Work on Hindi is in progress \n...\n")
       
        if var1.get()==1:
            communicatorOut = subprocess.check_output(['bash run_communicator.sh '+filename], shell=True) # Store the output of the communicator.sh command that has been run upon the filename(i.e., the user.csv).
            
            outlist.append(sentname + "\n" + "\n" + communicatorOut) # In the popup window, displays the list of probable english sentences preceded by the steps of executions (advanced level information).
            
        
            
        finaloutput = "\n".join(outlist)
        
        comOut1List=[]
              
        for sent in finaloutput.split('\n')[len(finaloutput.split('\n'))-2:None:-1]:
            if ' ' not in sent:
                break
            
            else:
                if ' ' in sent:
                    comOut1List.append(sent)
        
        #my_output = comOut1List[0]# first item of output.            
        #return my_output #gives only the first output of the sentence
        
        my_output = '\n'.join(comOut1List)# all items of output.                    
        #return my_output # gives all the outputs
        
        def popupeditor(filelocation):
            os.system('gedit -s '+ filelocation)

        
        #if len(my_output) != 0:
            #return my_output
        global my_finaloutput

        if len(my_output) > 0:
            
            my_finaloutput = my_output
            
        elif len(my_output) == 0:
            os.chdir(CommunicatorPath)
            sentname = filename.split('/')[len(filename.split('/'))-1]
    
            newdmrsfile= 'output/'+sentname.replace('_user.csv','')+'_dev.csv_new_dmrs.txt'
            popupeditor(newdmrsfile)
            
                    
            my_finaloutput = subprocess.check_output(['bash run_mod_dmrs.sh '+sentname.replace('_user.csv','')+"_dev.csv"], shell=True)
            
        return my_finaloutput+'\n'
            #return result_mod_dmrs
        
        #os.chdir(directory)

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


# def coldict(linelist):
#     global headerdict
#     headerdict = {}
#     for row in linelist:
#         headerdict[row.split('\t')[0]] = row.split('\t')[1].strip('\n')



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
        os.chdir(CommunicatorPath)
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
            outputdic[key] = {}

            if len(key) == 2: # fetches the keys such as "s1", "s2" etc. and stores them as keys of the dict
                sent = headerdict[key]
                outputdic[key]['info'] = sent

                indexdic = {} # To fetch any indexed word in the sentences and stores them as id:word pair in dictionary format (inside indexdic)
                for num in '123456789':
                    if num in sent:
                        indexed_word = re.findall('\S+'+num, sent)
                        indexed_word = indexed_word[0].replace('-'+num,'')
                           
                        indexdic[num] = indexed_word
                        outputdic[key]['info'] = outputdic[key]['info'].replace('-'+num,'')
                        for char in '~@#$^*_-+}{[]':
                            if char in outputdic[key]['info']:
                                outputdic[key]['info'] = outputdic[key]['info'].replace(char,' ')


                outputdic[key]['csvfile'] = outputdic[key]['info'].replace(' ','_')+'_user.csv'



                outputdic[key]['indices'] = indexdic
                outputdic[key]['execoutput'] = 'blank'

                #return outputdic[key]['csvfile']




            if '.g' in key and len(key) > 3: # matches keys such as "s1.g", "s2.g'" and so on.
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

                    sentid = key.split('.')[0]

                    comOutList_line1 = comOutList[0]

                    sentcsv = sentusercsv.replace('user.csv','dev.csv')

                    indexdic = {}

                    csv = open(CommunicatorPath+'/output/'+sentcsv,'r')

                    csvlines = csv.readlines()

                    for index in outputdic[sentid]['indices']:
                        indexedword = outputdic[sentid]['indices'][index]

                        for value in csvlines[0].split(','): # takes the 2nd row of dev.csv
                            if indexedword.split(' ')[-1] in value: # if the last indexed word is found in that column
                                valueindex = csvlines[0].split(',').index(value)
                                engword = csvlines[1].split(',')[valueindex]

                            #splitsent = comOutList_line1.split(engword)
                                execoutput = comOutList_line1.replace(engword,engword+'-'+index)
                                
                                outputdic[key]['execoutput'] = communicatorOut #execoutput
                            
                #devcsv.close()

                    outputdic[key]['indices'] = indexdic



                if 's(' in value:

                    splitvalue = value.split(',')
                    splitvalue1 = splitvalue[0]
                    splitvalue2 = splitvalue[1]

                    sentid = splitvalue2[0:value.index(')')]

                    sentence = outputdic[sentid]['execoutput']

                    indexdic = {}

                    for indexedword in re.findall(r"\S+-\d+", sentence):
                        for index in re.findall(r"-\d+",indexedword):
                            word = indexedword.replace(index)

                            indexdic[index]=word

                    outputdic[key]['indices'] = indexdic

                    index = splitvalue1[splitvalue1.index('*')+1:len(splitvalue1)]

                    word = outputdic[key]['indices'][index]

                    splitoutput = sentence.split(word)

                    for item in splitoutput:
                        if item == '':
                            splitoutput[splitoutput.index(item)]=word

                    part = splitvalue2[splitvalue2.index('[')+1:len(splitvalue2)-1]

                    outputdic[key]['execoutput'] = splitoutput[int(part)-1]

                if 'd(' in value:

                    splitvalue = value.split(',')
                    splitvalue1 = splitvalue[0]
                    splitvalue2 = splitvalue[1]

                    sentid = splitvalue2[0:value.index(')')]

                    sentence = outputdic[sentid]['execoutput']

                    indexdic = {}

                    for indexedword in re.findall(r"\S+-\d+", sentence):
                        for index in re.findall(r"-\d+",indexedword):
                            word = indexedword.replace(index)

                            indexdic[index]=word

                    outputdic[key]['indices'] = indexdic

                    index = splitvalue1[splitvalue1.index('*')+1:len(splitvalue1)]

                    word = outputdic[key]['indices'][index]

                    outputdic[key]['execoutput'] = sentence.replace(word,'')


                if 'a(' in value:

                    splitvalue = value.split(',')
                    splitvalue1 = splitvalue[0]
                    splitvalue2 = splitvalue[1]

                    sentid = splitvalue2[0:value.index(')')]

                    sentence = outputdic[sentid]['execoutput']

                    if '^' in splitvalue1:
                        word = splitvalue1[splitvalue1.index('^')+1:len(splitvalue1)]
    
                        outputdic[key]['execoutput'] = word+' '+sentence

            #return outputdic
            
            if key == 's.g': # matches keys such as "s1.g", "s2.g'" and so on.
                value = headerdict[key]['info']
                keylist = value.split('+')
                #return value.split('+')
                outputdic[key]['info'] = value
                #return outputdic[key]['info']
                #return outputdic

                outputlist = []

                for word in keylist:
                    if '.g' in word:
                        outputlist.append(outputdic[word]['execoutput'])
                    #else:
                        #outputlist.append(word)
                        
                
                #return outputlist
                outputdic[key]['execoutput'] = ' '.join(outputlist)


        return outputdic['s.g']['execoutput']

                #######################

                #######################

                #######################





    








        
    #return relsentset, '\n\n', sg
    
    # Do operations according to types of key in the dictionary
    
    





    
        
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
        os.chdir(CommunicatorPath)
        
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
    f3 = Frame(master, borderwidth=10)
    f4 = Frame(master, borderwidth=10)
    #frame1 = Frame(master, borderwidth=10)
##
##
    for frame in (f1, f2, f3):
        frame.grid(row=0, column=0, sticky='news')

    def raise_frame(frame):
        frame.tkraise()

    filemenu = Menu(master)
    #filemenu.add_command(label="ComTool", command=lambda:raise_frame(f3))

    #useridLabel= Label(frame1, text="Insert your text below:\n", anchor=N, justify=CENTER)
    #useridLabel.pack(anchor=N,)



## Hindi ComplexSent Catenator:    
    filemenu.add_command(label="Complex", command=lambda:raise_frame(f2))
    fileUpload=Button(f2, text="Upload Multiple-RelClaus File", fg="blue", command=reltool)
    fileUpload.pack(side = TOP)
    fileUpload=Button(f2, text="Upload Single-Embeded-RelClaus File", fg="blue", command=reltool2)
    fileUpload.pack(side = TOP)
    fileUpload2=Button(f2, text="Upload Conditional-Clause File", fg="green", command=condtool)
    fileUpload2.pack(side = TOP)
    # Multilingual Generator    
    filemenu.add_command(label="MultiLing", command=lambda:raise_frame(f3))
    
    ## 1.Input txt file containing IndianLg Data
    # Entry Options:
    
    # a. Typing in Entry Box

    txtentry= Entry(f3, width=50)
    txtentry.grid(row=0, column=0, sticky=W, pady=4)
    
    # b. Upload of Txt File (value is stored in the variable "text" usable later) (Socket)

    #fileUpload=Button(frame1, text="Upload User-CSV", fg="blue", command=main)
    #fileUpload.pack(side = TOP, anchor=N)
    
    Button(f3, text='Edit Input CSV', command=csvEditor).grid(row=9, column=0, sticky=W, pady=4)
    #fileUpload=Button(f3, text="Edit Uploaded CSV", fg="brown", command=csvEditor)
    #fileUpload.pack(side = TOP, anchor=N)
    
    def var_states():
##    for value in [var0.get(), var1.get(), var2.get(), var3.get(), var4.get(), var5.get()]:
##        if value == 1:
##            print "my value is 1", eval("var0.get()")
        main()
        #if var0.get()==1:
         #   tkMessageBox.showinfo("Information","This is a Hindi Sentence")

#            print "Hin: Hindi Hindi Hindi Hindi Hindi Hindi"
        #if var1.get()==1:
         #   main()
          #  print "Hello English"
        if var2.get()==1:
            print "Ger: German German German German German German"
        if var3.get()==1:
            print "Ban: In Progress"
        if var4.get()==1:
            print "Mar: Marathi Marathi Marathi In Progress"
        if var5.get()==1:
            print "Tam: Tamil Tamil Tamil In Progress"
        elif var1.get() + var2.get()== 0 :
            print "Please select atleast one output language"
        print "-=- -=- -=- -=- End of Translation Process -=- -=- -=- -=-"
    
    #print("\n\nEnglish: %d\nGerman: %d" % (var1.get(), var2.get()))

    Label(f3, text="Choose one or more Output language(s):").grid(row=1, column=0, sticky=W)
    global var0
    var0 = IntVar()
    Checkbutton(f3, text="Hindi", variable=var0).grid(row=2, column=0, sticky=W)
    global var1
    var1 = IntVar()
    Checkbutton(f3, text="English", variable=var1).grid(row=3, column=0, sticky=W)
    global var2
    var2 = IntVar()
    Checkbutton(f3, text="German", variable=var2).grid(row=4, column=0, sticky=W)
    global var3
    var3 = IntVar()
    Checkbutton(f3, text="Bangla", variable=var3).grid(row=5, column=0, sticky=W)
    global var4
    var4 = IntVar()
    Checkbutton(f3, text="Marathi", variable=var4).grid(row=6, column=0, sticky=W)
    global var5
    var5 = IntVar()
    Checkbutton(f3, text="Tamil", variable=var5).grid(row=7, column=0, sticky=W)


    Button(f3, text='Upload Input', command=var_states).grid(row=8, sticky=W, pady=4)
#    fileUpload=Button(f3, text="Choose Language Below", fg="blue")
#    fileUpload.pack(side = TOP)
## Help Guidelines:    
    filemenu.add_command(label="Help", command=lambda:raise_frame(f1))
    text=Text(f1, font=('Arial', 14, 'normal') , width=60, height=10)
    text.pack()
    text.insert(END,"Usage Guidelines: \n\n1. Communicator tool: \nIt is an interface that is capable of taking ...user.csv prepared for a Hindi sentence as input and display the most probable options of English Translations for that sentence. \nPlease use the only the \'File\' option inside the pop up window to upload a csv file everytime. \n\n1.a Advanced Mode: \n\nIf the given set of output has only wrong sentences or if you just want to play with the csv information, please click the \'Edit Uploaded CSV\' and edit required entries in the appropriate row and column as per CSV creation guidelines")
    
    
    
    master.config(menu=filemenu)
    master.mainloop()

displayInterface()
