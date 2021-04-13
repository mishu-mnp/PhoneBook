from tkinter import *
import sqlite3
from tkinter import messagebox

con=sqlite3.connect("database.db")
cur=con.cursor()


class Addpeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("500x500+250+150")
        self.title("Add New Person")
        self.resizable(False,False)

        self.top_frame = Frame(self, height=180, bg="#9e32a8")
        self.top_frame.pack(fill=X)

        self.bottom_frame = Frame(self, height=320, bg="yellow")
        self.bottom_frame.pack(fill=X)

        # top_frame
        self.top_image = PhotoImage(file="icons/addpeople.png")
        self.top_image_label = Label(self.top_frame, image=self.top_image, bg="#9e32a8")
        self.top_image_label.place(x=40, y=40)

        self.heading = Label(self.top_frame, text="Add New People", font="helvetica 26 bold", bg="#9e32a8",
                             fg="Dark orange")
        self.heading.place(x=160, y=70)


        #name
        self.label_name=Label(self.bottom_frame,text="Name",width=7,font="verdana 12 bold",bg="#f54242",fg="#42f542")
        self.label_name.place(x=20,y=30)

        self.entry_name=Entry(self.bottom_frame,width=35,bd=2,bg="white")
        self.entry_name.insert(INSERT,"enter name")
        self.entry_name.place(x=120,y=30)

        #surname
        self.label_surname = Label(self.bottom_frame, text="Surname", font="verdana 12 bold", bg="#f54242", fg="#42f542")
        self.label_surname.place(x=20, y=70)

        self.entry_surname = Entry(self.bottom_frame, width=35, bd=2, bg="white")
        self.entry_surname.insert(INSERT, "enter surname")
        self.entry_surname.place(x=120, y=70)

        #email
        self.label_email = Label(self.bottom_frame, text="Email Id",width=7, font="verdana 12 bold", bg="#f54242", fg="#42f542")
        self.label_email.place(x=20, y=110)

        self.entry_email = Entry(self.bottom_frame, width=35, bd=2, bg="white")
        self.entry_email.insert(INSERT, "enter email")
        self.entry_email.place(x=120, y=110)

        #contact number
        self.label_number = Label(self.bottom_frame, text="Number",width=7, font="verdana 12 bold", bg="#f54242", fg="#42f542")
        self.label_number.place(x=20, y=150)

        self.entry_number = Entry(self.bottom_frame, width=35, bd=2, bg="white")
        self.entry_number.insert(INSERT, "enter number")
        self.entry_number.place(x=120, y=150)

        #address
        self.label_address = Label(self.bottom_frame, text="Address",width=7, font="verdana 12 bold", bg="#f54242", fg="#42f542")
        self.label_address.place(x=20, y=190)

        self.entry_address = Text(self.bottom_frame, width=30,height=5, bd=2, bg="white")
        self.entry_address.insert(INSERT, "enter address")
        self.entry_address.place(x=120, y=190)

        #button
        button_save=Button(self.bottom_frame,text="Save",width=7,font="verdana 10 bold",bg="light green",fg="black",command=self.add_people)
        button_save.place(x=150,y=285)


    def add_people(self):

        name=self.entry_name.get()
        surname=self.entry_surname.get()
        email=self.entry_email.get()
        contact=self.entry_number.get()
        address=self.entry_address.get(1.0,END)

        if id and name and surname and email and contact and address != " ":
            try:
                query="insert into 'addressbook'(person_name,person_surname,person_email,person_contact,person_address) values(?,?,?,?,?)"
                cur.execute(query, (name, surname, email, contact, address))
                con.commit()
                messagebox.showinfo("Successful", "Contact Added")
            except Exception as e:
                messagebox.showerror("Error:", str(e))
        else:
            messagebox.showerror("Error", "fill all details first", icon="warning")
