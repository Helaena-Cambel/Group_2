from tkinter import *

lorenzo=Tk()
lorenzo.title("Button ")
L1=Label( text="<--- Click to change the color of the button.", font=40)
L1.grid(row=2, column=5)
L1=Label( text="")
L1.grid(row=1, column=0)

def C1():
    B1 = Button(lorenzo, text="Color", font=40, bg='#FFFF00', fg='#FF0000')
    B1.grid(row=2, column=1)

B1=Button(lorenzo, text="Color", font=40, bg='#0000FF', fg='#FF0000', command=C1)
B1.grid(row=2, column=1)

LF=Label(lorenzo)
LF.grid(row=3, column=1)

lorenzo.mainloop()

    