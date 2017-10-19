##################################
# import data from googleSpreadsheet into a local variable 'sheet'!

import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name, open and store each required sheet in the workbook into different variables.

Database = client.open("Word_db")

sheet = Database.worksheet("Sheet1") # Word2Word Data
sheet2 = Database.worksheet("Sheet2") # User_info
#################################

# Extract all of the values in python_dictionary format.

list_of_hashes = sheet.get_all_records(head=1) # Word2Word Data

list_of_hashes2 = sheet2.get_all_records(head=1) # User_info


################################
#take items from each key of dictionary and store them into a variable_name identical with the key.

# Extract all column items from Word2Word Datasheet
Sl=[]
for item in list_of_hashes:
	Sl.append(item['Sl'])

Lang=[]
for item in list_of_hashes:
	Lang.append(item['Lang'])

Synset=[]
for item in list_of_hashes:
	Synset.append(item['Synset'])

Gloss=[]
for item in list_of_hashes:
	Gloss.append(item['Gloss'])

Example=[]
for item in list_of_hashes:
	Example.append(item['Example'])

Lang2=[]
for item in list_of_hashes:
	Lang2.append(item['Lang2'])

U_id=[]
for item in list_of_hashes:
	U_id.append(item['U_id'])

U_Entry=[]
for item in list_of_hashes:
	U_Entry.append(item['U_Entry'])

R_A=[]
for item in list_of_hashes:
	R_A.append(item['R_A'])

R_R=[]
for item in list_of_hashes:
	R_R.append(item['R_R'])

R_M=[]
for item in list_of_hashes:
	R_M.append(item['R_M'])

R_D=[]
for item in list_of_hashes:
	R_D.append(item['R_D'])

R_Comment=[]
for item in list_of_hashes:
	R_Comment.append(item['R_Comment'])

U_Date=[]
for item in list_of_hashes:
	U_Date.append(item['U_Date'])
		
R_Date=[]
for item in list_of_hashes:
	R_Date.append(item['R_Date'])

Flag=[]
for item in list_of_hashes:
	Flag.append(item['Flag'])

# Extract all column items from User_info Datasheet

user_id=[]
for item in list_of_hashes2:
	user_id.append(item['user_id'])

name=[]
for item in list_of_hashes2:
	name.append(item['name'])

passwd=[]
for item in list_of_hashes2:
	passwd.append(item['passwd'])

bio_dat=[]
for item in list_of_hashes2:
	bio_dat.append(item['bio_dat'])

email=[]
for item in list_of_hashes2:
	email.append(item['email'])

total_entries=[]
for item in list_of_hashes2:
	total_entries.append(item['total_entries'])

total_rejected=[]
for item in list_of_hashes2:
	total_rejected.append(item['total_rejected'])

total_valid=[]
for item in list_of_hashes2:
	total_valid.append(item['total_valid'])


 #############################
 ##  USER_INTERFACE DESIGN  ##
 #############################

import webbrowser
from Tkinter import *

master = Tk()
master.title("Translation Interface")

def displayInterface():

##############
## Positioning all the FRAMES ##

### Frame 1 (Packing Username and Password and Login features)
    frame1 = Frame(master)
    frame1.pack(fill=X)
    useridLabel= Label(frame1, text=" LOGIN:  Username")
    useridLabel.pack(side=LEFT)
    
    username= Entry(frame1)
    username.pack(side=LEFT)

    gap= Label(frame1, text="  ")
    gap.pack(side=LEFT)

    passwordLabel= Label(frame1, text="Password")
    passwordLabel.pack(side=LEFT)
 
    password= Entry(frame1, show='*')
    password.pack(side=LEFT)

###
        
    gap2= Label(frame1, text="     ")
    gap2.pack(side=LEFT)

###

    gap2= Label(frame1, text=" ")
    gap2.pack(side=LEFT)


### Frame 2 (Packing Validity View and New Task View options)
    frame2 = Frame(master)
    frame2.pack(fill=X)



### Frame 3 (Packing Text Viewer box in a scrollable list format)

    frame3= Frame(master)
    frame3.pack(fill=BOTH, expand = True)

    scrollbar = Scrollbar(frame3)
    scrollbar.pack(side = RIGHT, fill=Y)

    listbox1= Listbox(frame3, yscrollcommand = scrollbar.set)
    listbox1.pack(fill=BOTH, expand=TRUE)
    scrollbar.config(command=listbox1.yview)

### Frame 4 (Entry, Skip and Comment Buttons)
    
    frame4= Frame(master)
    frame4.pack(fill=X)
    
    usrEntryLabel= Label(frame4, text=" Answer: ")
    usrEntryLabel.pack(side=LEFT)

    usrEntry= Entry(frame4)
    usrEntry.pack(side=LEFT)

    gap= Label(frame4, text="  ")
    gap.pack(side=LEFT)


    usEntryLabel= Label(frame4, text=" Comment: ")
    usEntryLabel.pack(side=LEFT)

    cmntEntry= Entry(frame4)
    cmntEntry.pack(side=LEFT)
    
    gap= Label(frame4, text="  ")
    gap.pack(side=LEFT)    

### Frame 5 (Packing the Dictionary Option Buttons)

    frame5= Frame(master)
    frame5.pack(fill=X)
    
    spacerFrame = Frame ( frame5 , bg="grey", borderwidth =10)
    spacerFrame.pack(fill=X)

    dictLabel= Label(frame5, text=" DICTIONARY VIEWER: ")
    dictLabel.pack(side=LEFT)


### Frame 6 (Packing the space for displaying Dictionaries)
#   frame6= Frame(master)
#   frame6.pack(fill=BOTH, expand=True)

#   scrollbar = Scrollbar(frame6)
#   scrollbar.pack(side = RIGHT, fill=Y)

#   listbox2= Listbox(frame6, yscrollcommand = scrollbar.set)
#   listbox2.pack(fill=BOTH, expand=TRUE)
#   scrollbar.config(command=listbox2.yview)

################

## COMMANDS TO EXECUTE ON BUTTON CLICK ##

    usrlogin=['F']

    def login():

        usr= username.get()
        pwd= password.get()

        if usr in user_id:
            pwdIndex = user_id.index(usr)
            if pwd == passwd[pwdIndex]:
                usrlogin[0]= 'T'
                listbox1.insert(END, "Login Successful!", "Please proceed as instructed.", "- - -    - - -")
            else:
                listbox1.insert(END, "Username & Password donot match","Please enter your details again")
        else:
            listbox1.insert(END, "Username & Password donot match","Please enter your details again")
            
### Logout

    def logout():
        if 'T' in usrlogin:
            usrlogin[0]= 'F'
            listbox1.insert(END, "You have successfully logged out!", "To start entry, please login again.")
        else:
            listbox1.insert(END, "First you have to login!")


##  Previous Valid Entries

    def valid_corrections():
        usr= username.get()
        if 'T' in usrlogin:
            usrIndex = user_id.index(usr)

            usrEntry = total_entries[usrIndex]
            usrRejected = total_rejected[usrIndex]
            usrvalidity = total_valid[usrIndex]
            
            listbox1.insert(END, '---', "UserID: " + str(usr), "Total Entries: " + str(usrEntry), "Rejected Entries: "+ str(usrRejected), "Valid Entries: " + str(usrvalidity), '---')
        else:
            listbox1.insert(END, "Please LOGIN to view Previous Entry Validity")



## Get New Tasks

    submit_status=['F']
    current_row=[0]

    def new_task():
        usr=username.get()
        if 'T' in usrlogin:
            for data in Flag:
                if data != 'used': 
                      
                    FlagIndex = Flag.index(data) # Take index of row at Flag #
                    Flag[FlagIndex]= 'used' # Keep the tag of current data to avoid repetition even if Translator Skips this row

                    row_index= FlagIndex+2 # Row index in Google_Spreadsheet = Dictionaryformat value index + 2 #
                    sheet.update_cell(row_index, 15, 'used') # Flag is in 15th Column #

                    listbox1.insert(END, "Language: ", "   "+Lang[FlagIndex], "Synset:", "   "+Synset[FlagIndex], "Gloss: ", "   "+Gloss[FlagIndex] , "Example: ", "   "+Example[FlagIndex], "Please enter your translation below.", "- - -   - - -", '')

                    current_row[0] = row_index # store the row_index in current row for other functions outside this definition.
                    break                    
        else:
            listbox1.insert(END, "Please LOGIN to get New Tasks") 

    def submit():
        usr=username.get()
        answer = usrEntry.get()
        comment = cmntEntry.get()
        date_time= datetime.datetime.now().ctime()
        row_index = current_row[0]

        sheet.update_cell(row_index, 7, answer+comment)
        sheet.update_cell(row_index, 13, date_time)
        sheet.update_cell(row_index, 16, usr)

    def skip():
        sheet.update_cell(current_row[0], 15, '')

##  Dictionary Viewing
    

    def dictionary_data():
        url = 'http://www.dictionary.com/'
        webbrowser.open_new(url)

    def oxford_data():
        url = 'https://en.oxforddictionaries.com/'
        webbrowser.open_new(url)

    def cambridge_data():
        url = 'http://dictionary.cambridge.org/'
        webbrowser.open_new(url)

    def shabdakosh_data():
        url = 'http://www.shabdkosh.com/'
        webbrowser.open_new(url)

    def shabdanjali_data():
        url = 'http://ltrc.iiit.ac.in/onlineServices/Dictionaries/Dict_Frame.html'
        webbrowser.open_new(url)

###################

## CREATING BUTTONS CONTAINING EXECUTION COMMANDS  ##

## Login

    login=Button(frame1, text="LOGIN", fg="blue", command=login)
    login.pack(side = LEFT)

## Logout

    logout=Button(frame1, text="LOGOUT", fg="red", command=logout)
    logout.pack(side = LEFT)

## Previous Entry Validity

    feedback=Button(frame2, text="Prev Entry Validity", fg="blue", command=valid_corrections)
    feedback.pack(side = LEFT)

## New Task Click

    new_taskBut=Button(frame2, text="New Task", fg="blue", command=new_task)
    new_taskBut.pack(side = LEFT)

## Submit

    submitBut=Button(frame4, text="Submit", fg="blue", command= lambda: submit() & new_task()) # combine multiple commands for one button with lambda
    submitBut.pack(side = LEFT)

## Skip

    skipBut=Button(frame4, text="Skip", fg="blue", command= lambda: skip() & new_task())
    skipBut.pack(side = LEFT)

##  Dictionary Buttons:

##  Dictionary.com
    dictionary=Button(frame5, text="Dictionary.com", fg="blue", command=dictionary_data)
    dictionary.pack(side = LEFT, fill=X, expand=True)

##  Oxford Dictionary
    oxford=Button(frame5, text="Oxford", fg="blue", command=oxford_data)
    oxford.pack(side = LEFT, fill=X, expand=True)

##  Cambridge Dictionary
    cambridge=Button(frame5, text="Cambridge", fg="blue", command=cambridge_data)
    cambridge.pack(side = LEFT, fill=X, expand=True)

##  Shabdkosh Dictionary
    shabdakosh=Button(frame5, text="Shabdakosh", fg="blue", command=shabdakosh_data)
    shabdakosh.pack(side = LEFT, fill=X, expand=True)

##  Shabdanjali Dictionary
    shabdanjali=Button(frame5, text="Shabdanjali", fg="blue", command=shabdanjali_data)
    shabdanjali.pack(side = LEFT, fill=X, expand=True)
    
    mainloop()

displayInterface()
