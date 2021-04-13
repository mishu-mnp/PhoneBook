from tkinter import *
import datetime
from my_people import Mypeople
from add_people import Addpeople
from about_us import About_us
date=datetime.datetime.now().date()
format_date=date.strftime("%d-%m-20%y")


class Application(object):

    def get_new_window(self):
        self.new_window = Toplevel()
        self.new_window.title("My people")

    def __init__(self,master):
        self.master=master

        # Frames
        self.top_frame=Frame(master,height=180,bg="#9e32a8")
        self.top_frame.pack(fill=X)


        self.bottom_frame=Frame(master,height=400,bg="yellow")
        self.bottom_frame.pack(fill=X)

        # top_frame
        self.top_image=PhotoImage(file="icons/icony.png")
        self.top_image_label=Label(self.top_frame,image=self.top_image,bg="#9e32a8")
        self.top_image_label.place(x=40,y=40)

        self.heading=Label(self.top_frame,text="My PhoneBook",font="helvetica 24 bold",bg="#9e32a8",
                           fg="Dark orange")
        self.heading.place(x=150,y=70)
        self.date_label=Label(self.top_frame,text="Date:"+format_date,bg="#9e32a8",font="helvetica 15 bold")
        self.date_label.place(x=330,y=130)

        #  *** ::Buttons:: ***
        self.my_people=Button(self.master, text="My people", width=10, font="helvetica 20 bold", bg="white",
                               fg="blue", command=self.My_people)
        self.my_people.place(x=150,y=220)

        self.add_people=Button(self.master,text="Add people",width=10, font="helvetica 20 bold",bg="white",
                                fg="blue",command=self.Add_people)
        self.add_people.place(x=150,y=290,)

        self.about_us = Button(self.master, text="About us", width=10, font="helvetica 20 bold", bg="white",
                                 fg="blue",command=self.About_us)
        self.about_us.place(x=150, y=360)


    def My_people(self):
        people=Mypeople()


    def Add_people(self):
        peoples=Addpeople()

    def About_us(self):
        about_window=About_us()


def main():
    root=Tk()
    app=Application(root)
    root.title("PhoneBook App")
    root.resizable(False,False)
    root.geometry("500x550+100+100")
    root.mainloop()


if __name__=="__main__":
    main()