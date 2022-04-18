from tkinter import *
window=Tk()
window.title("Text Field")
Ent=Entry(window)
Ent.place(x=60, y=50)
Ent.config(font=('Arial',12))
window.geometry("300x150+10+20")
window.mainloop()

