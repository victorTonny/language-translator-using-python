# hello-world

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
