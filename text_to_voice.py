from tkinter import *
from tkinter import Tk,Label,Entry
import pyttsx3
import time
#____________init_____________

def start():
        txt=E1.get()
        convertor=pyttsx3.init()
        convertor.setProperty('rate',110)
        convertor.say(txt)
        convertor.runAndWait()
        time.sleep(2)


root=Tk()
root.title('Text to voice')
root.geometry("400x400")
root.configure(bg= "gold")


#__________________Design__________


lbl=Label(root, text='INSERT your text  ',bd=5,padx=10,pady=10,width=100,highlightthickness=0,fg="black",font=("Times new roman",20)).pack()
E1 = Entry(root,width=50,font=50, bd = 5)
E1.pack(pady=5)


# Button
Button(root, text='START', bg="yellow", bd=1, command=start).pack()
root.mainloop()