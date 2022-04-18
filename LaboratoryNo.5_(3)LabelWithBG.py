from tkinter import *

win=Tk()
win.geometry("300x100")
win.title("Father of Computer")

text=Text(win, font=('Arial', 20))
text.insert(INSERT, "\n      Charles Babbage")

text.tag_add("start", "2.6","2.99")
text.tag_configure("start", background="cyan", foreground="black")
text.pack()

win.mainloop()