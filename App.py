'''
    This script was written in python 3.x.
    In order to run this script, please make sure your python version is 3.x or above.

    How to run:
        python App.py

    or if it doesn't work use this one:
        python3 App.py

    Author: Udin <just.udin@yahoo.com>

'''

from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Frame, Label, Entry

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Calculator by Udin")
        self.pack(fill=BOTH, expand=True)
        global value
        value = 0
        global num1
        num1 = StringVar()
        global num2
        num2 = StringVar()
        global res
        res = StringVar()

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Input Number 1 :", width=15)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(frame1,textvariable=num1)
        entry1.pack(fill=X, padx=5, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Input Number 2 :", width=15)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        entry2 = Entry(frame2,textvariable=num2)
        entry2.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=X)

        btnplus = Button(frame3, text="+", width=8, command=self.plus)
        btnplus.pack(side=LEFT, anchor=N, padx=5, pady=5)

        btnminus = Button(frame3, text="-", width=8, command=self.minus)
        btnminus.pack(side=LEFT, anchor=N, padx=5, pady=5)

        btnmul = Button(frame3, text="*", width=8, command=self.mul)
        btnmul.pack(side=LEFT, anchor=N, padx=5, pady=5)

        btndiv = Button(frame3, text="/", width=8, command=self.div)
        btndiv.pack(side=LEFT, anchor=N, padx=5, pady=5)

        frame4 = Frame(self)
        frame4.pack(fill=X)

        lbl3 = Label(frame4, text="Result :", width=10)
        lbl3.pack(side=LEFT, padx=5, pady=5)

        result = Entry(frame4,textvariable=res)
        result.pack(fill=X, padx=5, expand=True)

    def errorMsg(self,msg):
        if msg == 'error':
            tkinter.messagebox.showerror('Error!', 'Something went wrong! Maybe invalid entries')
        elif msg == 'divisionerror':
            tkinter.messagebox.showerror('Division Error', 'The value of input number 2 is 0. No dividing by 0')

    def plus(self):
        try:
            value = float(num1.get()) + float(num2.get())
            res.set(self.makeAsItIs(value))
        except:
            self.errorMsg('error')

    def minus(self):
        try:
            value = float(num1.get()) - float(num2.get())
            res.set(self.makeAsItIs(value))
        except:
            self.errorMsg('error')

    def mul(self):
        try:
            value = float(num1.get()) * float(num2.get())
            res.set(self.makeAsItIs(value))
        except:
            self.errorMsg('error')

    def div(self):
        # checks if user is trying to divide by zero
        if num2.get() == '0':
            self.errorMsg('divisionerror')
        elif num2.get() != '0':
            try:
                value = float(num1.get()) / float(num2.get())
                res.set(self.makeAsItIs(value))
            except:
                self.errorMsg('error')

    def makeAsItIs(self, value):
        if (value == int(value)):
            value = int(value)
        return value

def main():
    root = Tk()
    root.geometry("300x140")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()