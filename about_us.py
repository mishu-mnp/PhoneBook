from tkinter import *

class About_us(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x500+200+150")
        self.title("About Us")
        self.resizable(False,False)
        self.frame = Frame(self, height=500, bg="orange")
        self.frame.pack(fill=BOTH)

        self.texts=Label(self.frame,text="Here is something About Us"
        "\n This is my new Application made to store your details"
        "\n Hope you all will enjoy this Application...Thank You"
        "\n Thanks to Tech-gram Academy for his wonderful GUI series based on Python and you are a very good Tutor... :)",
        bg="orange",fg="purple",font="helvetica 8 bold")
        self.texts.place(x=10,y=20)