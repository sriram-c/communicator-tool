import webbrowser
from Tkinter import *
import tkFileDialog
import os
import subprocess
import commands

#################

class CsvTask(Frame):

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

        f = open(filename, "r")
        text = f.read()
        os.chdir('/home/anusaaraka/create-hindi-parser/chl_to_dmrs')
##        communicatorOut = commands.getoutput("bash run_communicator.sh "+filename)
##        communicatorOut = os.system("bash run_communicator.sh "+str(filename))
        communicatorOut = subprocess.check_output(['bash run_communicator.sh '+filename], shell=True)
        return communicatorOut

##  2. Run Communicator.sh on the uploaded csv file and store output in variable.

    #   a. set working directory to the location for run_communicator.sh

##        os.chdir('/home/anusaaraka/create-hindi-parser/chl_to_dmrs')
##        communicatorOut = subprocess.check_output(['bash run_communicator.sh '+text])
##
##        return communicatorOut



def processCsv():

    root = Tk()
    ex = CsvTask(root)
    root.geometry("300x250+300+300")
    root.mainloop()
    
def processFolder():
 

####################
    
master = Tk()
master.title("AnuTransKit")

###################

def displayInterface():

    frame1 = Frame(master, borderwidth=10)
    frame1.pack(fill=X)
    useridLabel= Label(frame1, text="Type your text below:", anchor=N, justify=CENTER)
    useridLabel.pack(anchor=N)

## 1.Input txt file containing IndianLg Data
# Entry Options:
    
    # a. Typing in Entry Box

    txtentry= Entry(frame1, width=50)
    txtentry.pack(side=TOP)
    
    # b. Upload Folder containing multiple UserCSV text files
    getFolder=Button(frame1, text="Upload UserCSV Folder", fg="blue", command=processFolder)
    getFolder.pack(side = TOP)

    # c. Upload of single UserCSV text file (value is stored in the variable "text" usable later) (Socket)

    fileUpload=Button(frame1, text="Upload UserCSV Text", fg="blue", command=processCsv)
    fileUpload.pack(side = TOP)

    mainloop()

displayInterface()
