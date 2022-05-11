from tkinter import *
semester = Tk()
semester.title('Semestral Grade')
semester.geometry("300x200")

class SemestralGrade:
    def __init__(self, semester):
        self.sem = Label(semester, text="Semestral Grade")
        self.sem.grid(row=1, column=0)

        self.prelim = Label(semester, text="Prelim Grade")
        self.prelim.grid(row=2, column=0)
        self.pre = Entry(semester, bd=3)
        self.pre.grid(row=2, column=1)

        self.midterm = Label(semester, text="Midterm Grade")
        self.midterm.grid(row=4, column=0)
        self.mid = Entry(semester, bd=3)
        self.mid.grid(row=4, column=1)

        self.final= Label(semester, text="Final Grade")
        self.final.grid(row=6, column=0)
        self.fin = Entry(semester, bd=3)
        self.fin.grid(row=6, column=1)

        self.button = Button(semester, text="Semester Grade", command=self.final_mark)
        self.button.grid(row=8, column=0)
        self.score = Entry(semester, bd=3)
        self.score.grid(row=8, column=1)

    def final_mark(self):
        self.score.delete(0, 'end')
        Prelim = int(self.pre.get())
        Midterm = int(self.mid.get())
        Final = int(self.fin.get())
        final_mark = Prelim * .30 + Midterm * .30 + Final * .40

        if float(97 <= final_mark <= 100):
            grade = 1.00
        elif float(93 <= final_mark <= 96.99):
            grade = 1.25
        elif float(89 <= final_mark <= 92.99):
            grade = 1.50
        elif float(85 <= final_mark <= 88.99):
            grade = 1.75
        elif float(82 <= final_mark <= 84.99):
            grade = 2.00
        elif float(79 <= final_mark <= 81.99):
            grade = 2.25
        elif float(76 <= final_mark <= 78.99):
            grade = 2.50
        elif float(73 <= final_mark <= 75.99):
            grade = 2.75
        elif float(70 <= final_mark <= 72.99):
            grade = 3.00
        else:
            grade = 5.00
        self.score.insert(END, str(grade))

mysemester =SemestralGrade(semester)
semester.mainloop()