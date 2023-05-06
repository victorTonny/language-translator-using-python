# Hi, I am Victor

This is my first repository created on Github which is Language Translator using python and Tkinter module.

# The following are the step by step guide to follow inorder to create language translation.

# Step1: You need to Install necessary libraries and packages
## **Python 3.x**
You need to have version of python 3 plus to run this

##**tkinter module**
Tkinter is a standard Python library (in Python 2.x and 3.x) that provides a simple and efficient way to create graphical user interfaces (GUIs) for desktop applications. It is based on the Tk GUI toolkit, which was developed originally for the Tcl scripting language.

##**googletrans module:**
googletrans this  is a free and open-source Python library that provides a simple interface to Google Translate API. With googletrans, you can easily translate text from one language to another using Google's machine translation service.

The library allows you to specify the source language and the target language, and it can automatically detect the source language if it's not specified. It can also translate entire paragraphs or documents, not just single words or phrases.

googletrans is built on top of the Google Translate website and uses the same translation engine as the website. It can be used for both personal and commercial applications, as it doesn't require an API key or any authentication to use.
  #Xvfb (X Virtual Frame Buffer); This Xvfb is a display server implementation that performs graphical operations in memory instead of rendering to a physical display. It allows running graphical applications without a physical display or monitor attached to the computer.


from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

### CREATE VIRTUAL DISPLAY ###
!apt-get install -y xvfb # Install X Virtual Frame Buffer
import os
os.system('Xvfb :1 -screen 0 1600x1200x16  &')    # create virtual display with size 1600x1200 and 16 bit color. Color can be changed to 24 or 8
os.environ['DISPLAY']=':1.0'    # tell X clients to use our virtual DISPLAY :1.0.

root = Tk()
root.geometry('1100x320')
root.resizable(0,0)
root['bg'] = 'skyblue'

root.title('Language Translator by Belontech')
Label(root, text="Language Translator", font = "Aerial 20 bold").pack()

Label(root, text="Enter text", font="Aeerial 13 bold", bg='white smoke').place(x=165, y=90)

Input_text = Entry(root, width=60)
Input_text.place(x=30, y=130)
Input_text.get()

Label(root, text = "Output", font='aerial 13 bold', bg='white smoke').place(x=700, y=90)
Output_text = Text(root, font='Arial 10', height=7, wrap=WORD, padx=5,pady=5, width=50)
Output_text.place(x=600, y=130)

language = list(LANGUAGES.values())
dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.set('choose language')

def Translate():
    translator = Translator
    translated = translator.translate(text=Input_text.get(), dest=dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)
trans_button = Button(root, text='Translate', font='arial 12 bold', pady=5, command=Translate, bg='orange', activebackground='green')
trans_button.place(x=445, y=180)
root.mainloop()
