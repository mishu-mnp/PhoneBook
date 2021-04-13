from tkinter import *
import sqlite3
from add_people import Addpeople
from tkinter import messagebox
con=sqlite3.connect("database.db")
cur=con.cursor()


class Updatepeople(Toplevel):
    def __init__(self,person_id):
        Toplevel.__init__(self)

        self.geometry("450x502+200+150")
        self.title("Update People")
        self.resizable(False, False)


        query= "select * from addressbook where person_id='{}'".format(person_id)
        result=cur.execute(query).fetchone()
        print(result)
        self.person_id=person_id

        person_name=result[1]
        person_surname=result[2]
        person_email=result[3]
        person_number=result[4]
        person_address=result[5]

        self.top_frame = Frame(self, height=180, bg="#9e32a8")
        self.top_frame.pack(fill=X)

        self.bottom_frame = Frame(self, height=320, bg="yellow")
        self.bottom_frame.pack(fill=X)

        # top_frame
        self.top_image = PhotoImage(file="icons/addpeople.png")
        self.top_image_label = Label(self.top_frame, image=self.top_image, bg="#9e32a8")
        self.top_image_label.place(x=40, y=40)

        self.heading = Label(self.top_frame, text="Update Person", font="helvetica 26 bold", bg="#9e32a8",
                             fg="Dark orange")
        self.heading.place(x=160, y=70)


        # name
        self.label_name = Label(self.bottom_frame, text="Name", width=7, font="verdana 12 bold", bg="#f54242",
                                fg="#42f542")
        self.label_name.place(x=20, y=30)

        self.entry_name = Entry(self.bottom_frame, width=35, bd=2, bg="white")
        self.entry_name.insert(INSERT,person_name)
        self.entry_name.place(x=120, y=30)

        # surname
        self.label_surname = Label(self.bottom_frame, text="Surname", font="verdana 12 bold", bg="#f54242",
                                   fg="#42f542")
        self.label_surname.place(x=20, y=70)

        self.entry_surname = Entry(self.bottom_frame, width=35, bd=2, bg="white")
        self.entry_surname.insert(INSERT,person_surname)
        self.entry_surname.place(x=120, y=70)

        # email
        self.label_email = Label(self.bottom_frame, text="Email Id", width=7, font="verdana 12 bold", bg="#f54242",
                                 fg="#42f542")
        self.label_email.place(x=20, y=110)

        self.entry_email = Entry(self.bottom_frame, width=35, bd=2, bg="white")
        self.entry_email.insert(INSERT,person_email)
        self.entry_email.place(x=120, y=110)

        # contact number
        self.label_number = Label(self.bottom_frame, text="Number", width=7, font="verdana 12 bold", bg="#f54242",
                                  fg="#42f542")
        self.label_number.place(x=20, y=150)

        self.entry_number = Entry(self.bottom_frame, width=35, bd=2, bg="white")
        self.entry_number.insert(INSERT,person_number)
        self.entry_number.place(x=120, y=150)

        # address
        self.label_address = Label(self.bottom_frame, text="Address", width=7, font="verdana 12 bold", bg="#f54242",
                                   fg="#42f542")
        self.label_address.place(x=20, y=190)

        self.entry_address = Text(self.bottom_frame, width=30, height=5, bd=2, bg="white")
        self.entry_address.insert(INSERT,person_address)
        self.entry_address.place(x=120, y=190)

        # button
        button_save = Button(self.bottom_frame, text="Update ", width=7, font="verdana 10 bold", bg="light green",
                             fg="black", command=self.update_person)
        button_save.place(x=150, y=285)

    def update_person(self):

        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        contact = self.entry_number.get()
        address = self.entry_address.get(1.0, END)
        query= "update addressbook set person_name='{}',person_surname='{}',person_email='{}',person_contact='{}',person_address='{}' where person_id={}".format(name,surname,email,contact,address,self.person_id)

        try:
            cur.execute(query)
            con.commit()
            messagebox.showinfo("Updated","Information is updated successfully")

        except Exception as e:
            print(e)
