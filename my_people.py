from tkinter import *
import sqlite3
from add_people import Addpeople
from update_people import Updatepeople
from display_people import Displaypeople
from tkinter import messagebox

con=sqlite3.connect("database.db")
cur=con.cursor()

class Mypeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("450x502+200+150")
        self.title("My People")
        self.resizable(False,False)
        self.top_frame = Frame(self, height=180, bg="#9e32a8")
        self.top_frame.pack(fill=X)

        self.bottom_frame = Frame(self, height=320, bg="yellow")
        self.bottom_frame.pack(fill=X)

        # top_frame
        self.top_image = PhotoImage(file="icons/mypeople.png")
        self.top_image_label = Label(self.top_frame, image=self.top_image, bg="#9e32a8")
        self.top_image_label.place(x=40, y=40)

        self.heading = Label(self.top_frame, text="My People", font="helvetica 26 bold", bg="#9e32a8",
                             fg="Dark orange")
        self.heading.place(x=160, y=70)
        self.scroll=Scrollbar(self.bottom_frame,orient=VERTICAL)

        self.listBox=Listbox(self.bottom_frame,width=30,height=20)
        self.listBox.grid(row=0,column=0,padx=(30,10))

        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.scroll.set)

        persons= cur.execute("select * from 'addressbook'").fetchall()
        # print(persons)
        count = 0
        for person in persons:
            self.listBox.insert(count, str(person[0])+". "+person[1]+" "+person[2])
            count+=1
        self.scroll.grid(row=0, column=1, sticky=N+S)

        # *** ::Buttons:: ***
        button_add=Button(self.bottom_frame,width=12,text="Add",font="Sans 12 bold",command=self.Add_people)
        button_add.grid(row=0,column=2,padx=20,pady=10,sticky=N)

        button_Update = Button(self.bottom_frame,width=12, text="Update",font="Sans 12 bold",command=self.Update)
        button_Update.grid(row=0, column=2, padx=20, pady=50, sticky=N)

        button_Display = Button(self.bottom_frame,width=12, text="Display",font="Sans 12 bold",command=self.Display)
        button_Display.grid(row=0, column=2, padx=20, pady=90, sticky=N)

        button_Delete = Button(self.bottom_frame,width=12, text="Delete",font="Sans 12 bold",command=self.Delete)
        button_Delete.grid(row=0, column=2, padx=70, pady=130, sticky=N)

    def Add_people(self):
        person=Addpeople()
        self.destroy()

    def Update(self):
        selected_people=self.listBox.curselection()
        person=self.listBox.get(selected_people)
        person_id=person.split(".")[0]
        update_person=Updatepeople(person_id)

    def Display(self):
        selected_people = self.listBox.curselection()
        person = self.listBox.get(selected_people)
        person_id = person.split(".")[0]
        display_person = Displaypeople(person_id)

    def Delete(self):
        selected_people = self.listBox.curselection()
        person = self.listBox.get(selected_people)
        person_id = person.split(".")[0]

        query= "delete from addressbook where person_id={}".format(person_id)
        answer= messagebox.askyesno("Warning","Are you sure to delete?")

        if answer==True:
            try:
                cur.execute(query)
                con.commit()
                messagebox.showinfo("Successful","Contact Deleted")
                self.destroy()

            except Exception as e:
                messagebox.showerror("Error",str(e))



