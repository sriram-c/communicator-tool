
# User Interface Design

import webbrowser
from Tkinter import *
import tkFileDialog

############

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent        
        self.initUI()

    def initUI(self):

        self.parent.title("File dialog")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)        

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)


    def onOpen(self):

        ftypes = [('Python files', '*.py'), ('All files', '*')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)

    def readFile(self, filename):

        f = open(filename, "r")
        text = f.read()
        return text



def main():

    root = Tk()
    ex = Example(root)
    root.geometry("300x250+300+300")
    root.mainloop()  

############

master = Tk()
master.title("AnuTransKit")

def displayInterface():

##############
## Positioning all the FRAMES ##

### Frame 1 :::
    frame1 = Frame(master, borderwidth=10)
    frame1.pack(fill=X)
    useridLabel= Label(frame1, text="Insert your text below:", anchor=N, justify=CENTER)
    useridLabel.pack(anchor=N)

## 1.Input txt file containing IndianLg Data
# Entry Options:
    
    # a. Typing in Entry Box

    txtentry= Entry(frame1, width=50)
    txtentry.pack(side=TOP)
    
    # b. Upload of Txt File (value is stored in the variable "text" usable later) (Socket)

    fileUpload=Button(frame1, text="Upload Text", fg="blue", command=main)
    fileUpload.pack(side = TOP)    

##  User CSV Generation:
    # Run parser subprocess
    # Collect output from parser
    # Run Grouping

    # Check validity of parses with a Human User.
    
## Identifiers
    # PropNoun
    # Complex Pred
    # Noun Compound


## 2. Submit Sentence-wise RawSent (through loop) to parser for "Paninian Parser" for parsed/analyzed output and store that in a variable.
    # Consult Convention for Parser Input Symbols and Pattern.(Roja)

## 3. Take the output values from (2) and detect pattern for multiplicity of Karaka for each word in that variable (Socket1).


## 4. Match the detected multiple karaka associated word with "Word-to-Sentence_Sample" (Socket2).

#    a. Fetch Word -> Sent pair samples from external source

#        i.  Connect to Word_Sent Data base link.

#        ii. Match the currently detected words, with those in Database

#        iii.Fetch meaning/sent_example

#    b. Arrangement:

#       i. List format variableWord=["meaning_1", "meaning_2", "..."]

#       ii.Extract a Word: Meaning set pair




## 5. Show the "word" with all "Sentence Samples" as Option_Buttons


## 6. Show each "sample sentence" for the word as option Button


## 7. Using <get> create desired value from the clicked button


#    a. Optimisation of Disambiguation of Parser Output(Modify Parser_Input Capabilities(pipeline))


## 8. Generate the {word:value} pair for that word in the context.


## 9. Store that paired_value in a variable (Socket3)


## 10.Send the value from the variable to a Database outside this function. (Sense Value match )

    # Send Validated data to Parser again
    # Collect output

##  Generate User CSV
    # ...
    # ...

## Submit generated User CSV to Communicator tool (as subprocess).

    # Collect generated English Sentences
    # Provide the options for a Human Validator to choose as the closest translation for the given sentence.
    # Collect the choice and store as the first completely translated sentence.
        # Innitially create a txt file and write all outputs to that file in append mode.



    


    mainloop()

displayInterface()
