from tkinter import*
from tkinter import ttk
window = Tk()

# Window
window.geometry("400x150")
window.title("Label")

# Label
label = Label(window, text = "Laboratory Activity 5\nSubmitted to: Mam Sayo")
label.pack(pady=60)

window.mainloop()
