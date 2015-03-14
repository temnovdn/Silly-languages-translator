#This translator will translate provided sentence to Opish, Turkey Irish or
#Pig Latin.

from pig_latin import *
from opish import *
from turkey_irish import *
from Tkinter import *


#Translate button handler
def translate_button_clicked():

    global language, text_input
      
    text = text_input.get('1.0', END)
    
    if language.get() == 'Opish':
        translated = opish(text)
        Label(root, text = translated).pack()
        
    elif language.get() == 'Pig Latin':
        translated = sentence_pig_latin(text)
        Label(root, text = translated).pack()
        
    elif language.get() == 'Turkey Irish':
        translated = turkey_irish(text)
        Label(root, text = translated).pack()
    else:
        Label(root, text = "Language condition error").pack()

##def translate_button_clicked():
##    text = text_input.get('1.0', END)    
##    translated = opish(text)
##    Label(root, text = translated).pack()

#root creation
root = Tk()
root.title("Silly languages translator")
root.geometry('500x600+300+200')

#Text input field
text_input = Text(root, height = 8, width = 45, font = 'Arial 14', wrap = WORD)
text_input.pack()

#Initialisation of language variable
language = StringVar()
language.set('Opish')

#Radiobuttons for language selection
Label(root, text = 'Please select a silly language to translate:').pack(anchor = W)
Radiobutton(root, text = 'Opish', variable = language, value = 'Opish').pack(anchor=W)
Radiobutton(root, text = 'Pig Latin', variable = language, value = 'Pig Latin').pack(anchor=W)
Radiobutton(root, text = 'Turkey Irish', variable = language, value = 'Turkey Irish').pack(anchor=W)


#Translate button
translate = Button(root, text='Translate!', command = translate_button_clicked)
translate.pack(side = 'bottom')

root.mainloop()


