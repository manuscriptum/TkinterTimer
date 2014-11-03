from Tkinter import *
import tkMessageBox

class TkinterTimer:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

        self.label_text = var = StringVar()
        self.label_text.set("25")
        self.label = Label(frame, textvariable=self.label_text, relief=RAISED)
        self.label.pack(side=LEFT)

        master.mainloop()

    def say_hi(self):
        tkMessageBox.showinfo("Say Hello", "Hello World")

TkinterTimer(Tk())
