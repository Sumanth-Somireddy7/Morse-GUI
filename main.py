from tkinter import *
from tkinter import messagebox
import getpass
import ctypes
import webbrowser

'''Important to be noticed There are no distinctions between uppercase and lowercase letters used in Morse code. 
There’s no need, and the Morse code does not include upper or lower case letters. As long as the proper spacing is 
used between characters and words, the receiving party can copy and understand the text. Occasional punctuations such 
as the comma and period, or the more commonly used “=” (break between thoughts), all help the transition between 
sentences and paragraphs. '''

MORSE_CODE_DICT = { 'A' :'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher +=  MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher


# Function to decrypt the string
# from morse to english
def decrypt(message):
    # extra space added at the end to access the
    # last morse code
    i = 0
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:

        # checks for space
        if (letter != ' '):

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            citext += letter

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2:

                # adding space to separate words
                decipher += ' '
            else:

                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                                                              .values()).index(citext)]
                citext = ''

    return decipher

def onClick():
    global opLabel
    global opAnswer
    mystr = StringVar()

    if str(e.get()[0].upper()) in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
        result = encrypt(e.get().upper())
        opLabel = Label(root, text="The Morse Code Translation is ", bg='#E6E6FA', font=('Calibri', 20))
        opLabel.pack(pady=50)
        opAnswer = Entry(root, bg = '#FFFF00', textvariable = mystr,  font = ('Calibri',30), width = 80, justify = 'center', state = "readonly")
        mystr.set(result.upper())
        opAnswer.pack(pady=30)
        Translate['state'] = DISABLED

    else:
        result = decrypt(e.get().upper())
        my_text = StringVar()
        my_text.set(result)
        opLabel = Label(root, text="The English Translation is ", bg='#E6E6FA', font=('Calibri', 20))
        opLabel.pack(pady=30)
        opAnswer =Entry(root ,bg = '#FFFF00', textvariable = mystr, font=('Calibri', 30), width = 80, justify = 'center', state = "readonly")
        mystr.set(result.upper())
        opAnswer.pack(pady=30)
        Translate['state'] = DISABLED

#Open Web Browser
def openbrowser():
    url = 'https://github.com/Sumanth-Somireddy7/module5-solution'
    new = 1
    webbrowser.open(url,new)


#Delete Label
def delLabel():
    opLabel.destroy()
    opAnswer.destroy()
    Translate['state'] = NORMAL

#Display function on closing Application
def on_closing():
    messagebox.showinfo("Info", "\nProject by :- Sumanth Somireddy & Komal Kumar Penti \n Guided by :- Mrs. K. SitaKumari Ma'am \n College :- Velagapudi Ramakrishna Siddhartha Engineering College\n Branch :- Information Technology")
    root.destroy()


#Create a Graphical Window

root = Tk()

#Fix the Window Size

root.state('zoomed')


# Improve the GUI Resolution using ctypes module
#ctypes.windll.shcore.SetProcessDpiAwareness(1)


#Add title to the Application

root.title("Morse Code Translation Project")

#Add icon to Tkinter Window

p1 = PhotoImage(file = 'morse-code.png')
root.iconphoto(False, p1)

#Add Background Color to the Window

root.configure(bg = '#E6E6FA')


#Creating a label widget
websitelink = Label(root, text = "Get the source code", font = ('Segoe UI',15), bg = '#E6E6FA', cursor = 'hand2')
username = "Hello  " + str(getpass.getuser())
nameLabel = Label(root,text = username, font = ('Cambria',25), bg = '#E6E6FA')
myLabel = Label(root,text="Welcome to Morse Code Translator", fg = 'blue', font = ('Helvetica',30), bg = '#E6E6FA')
myLabel1 = Label(root,text="Enter Morse Code or English String", bg = '#E6E6FA', font = ('Times New Roman', 20))


#Showing label on to the screen
'''myLabel.pack() #Pack is a geometry manager which fits widgets in rows or columns like in BootStrap'''

nameLabel.pack(pady = 10)
myLabel.pack(pady = 30)
myLabel1.pack(pady = 30)

#Creating an input Field

e = Entry(root, width=90, font = ('Verdana',15), justify = 'center')
e.pack(pady=10)

#Creating Buttons in Application

'''padx and pady are size of the button as x-axis and y-axis respectively'''



Translate = Button(root, text = 'Translate', padx = 30,pady=5,command = onClick  ,fg = '#000000', bg = '#90EE90', font = ('Segoe UI',15), cursor = 'hand2')

'''command parameter tells what to do on clicking the button. Here we call the function myClick(). No need parenthesis.'''

#Translate.grid(row = 10, column = 8)

Translate.pack(pady = 30)


deletetext = Button(root, text = 'Delete Text', padx = 30,pady=5,command = delLabel  ,fg = '#FFFFFF', bg = '#FF0000', font = ('Segoe UI',15))
deletetext.pack(padx = 0.1)
'''We can add padding as argument to ensure clear gaps and spacing'''
websitelink.pack(side = 'bottom', fill = 'x', expand = 'true')
websitelink.bind("<Button-1>", lambda e:openbrowser())

credits = Label(root, text = "Developed by Sumanth Somireddy & Komal Kumar Penti", font = ('Segoe UI',15), bg = '#E6E6FA')
credits.pack(side = 'bottom', fill = 'y', expand = 'true')

#Display message on closing the application


root.protocol("WM_DELETE_WINDOW", on_closing)



#Create looping i.e.. as long as the GUI application is opened, the loop is going to run all the time


root.mainloop()



