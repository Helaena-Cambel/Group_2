from tkinter import*
from tkinter import ttk
window = Tk()

# Window
window.geometry("300x100")
window.title("Major Subjects")

# List Box
data = "reading", "writing", "arithmetic", "coding"
lb = Listbox(window, height = 5, selectmode = "single")
for num in data:
   lb.insert(END, num)
lb.place(x=85, y=10)

window.mainloop()
