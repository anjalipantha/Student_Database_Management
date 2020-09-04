import tkinter
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import pymysql


class students:
    def __init__(self):
        self.root = Tk()
        self.root.title("STUDENT MANAGEMENT SYSTEM")
        self.root.geometry("1350x800+0+0")

        title = Label(self.root, text="STUDENT MANAGEMENT SYSTEM", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"), bg="yellow", fg="black")

        title.pack(side=TOP, fill=X)

        # ============All Variables===========
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.address_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        # ==========Manage Frame=============================

        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="yellow")
        Manage_Frame.place(x=20, y=100, width=450, height=690)

        m_title = Label(Manage_Frame, text="Manage Student", bg="yellow", fg="black",
                        font=("times new roman", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=10, sticky="w")

        lbl_roll = Label(Manage_Frame, text="Roll No:", bg="yellow", fg="black", font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_Roll = Entry(Manage_Frame, textvariable=self.Roll_No_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(Manage_Frame, text="Name:", bg="yellow", fg="black", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_Name = Entry(Manage_Frame, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_Name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_Email = Label(Manage_Frame, text="Email:", bg="yellow", fg="black", font=("times new roman", 20, "bold"))
        lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_Email = Entry(Manage_Frame, textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_Gender = Label(Manage_Frame, text="Gender:", bg="yellow", fg="black", font=("times new roman", 20, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        #======Combo Gender====================================

        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=("times new roman", 14, "bold"),
                                    state='readonly')
        combo_gender['values'] = ("Male", "Female", "Others")
        combo_gender.grid(row=4, column=1, padx=10, pady=10)

        lbl_Contact = Label(Manage_Frame, text="Contact:", bg="yellow", fg="black",
                            font=("times new roman", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_Contact = Entry(Manage_Frame, textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5,
                            relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_dob = Label(Manage_Frame, text="D.O.B:", bg="yellow", fg="black", font=("times new roman", 20, "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_dob = Entry(Manage_Frame, textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5,
                        relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_Adress = Label(Manage_Frame, text="Address:", bg="yellow", fg="black", font=("times new roman", 20, "bold"))
        lbl_Adress.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_Address = Entry(Manage_Frame, textvariable=self.address_var,width=29,font=("times new roman", 10, 'bold'),bd=5,relief=GROOVE)
        self.txt_Address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        # =======Buttons Frame=======================

        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="yellow")
        btn_Frame.place(x=10, y=550, width=410)

        Addbtn = Button(btn_Frame, text="Add", command=self.add_students, width=10)
        Addbtn.grid(row=0, column=0, padx=10, pady=2)
        updatebtn = Button(btn_Frame, text="Update", command=self.update, width=10).grid(row=0, column=1, padx=10,
                                                                                         pady=2)
        deletebtn = Button(btn_Frame, text="Delete", command=self.delete_data, width=10).grid(row=0, column=2, padx=10,
                                                                                              pady=2)
        clearbtn = Button(btn_Frame, text="Clear", command=self.clear_data, width=10).grid(row=0, column=3, padx=10,
                                                                                           pady=2)

        # ============Detail frame===========================
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="yellow")
        Detail_Frame.place(x=500, y=100, width=830, height=690)

        lbl_search = Label(Detail_Frame, text="Search By:", bg="yellow", fg="black", font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20)

        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by, width=7,
                                    font=("times new roman", 14, "bold"), state='readonly')
        combo_search['values'] = ("Roll", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_Search = Entry(Detail_Frame, textvariable=self.search_txt, font=("times new roman", 10, "bold"), bd=5,
                           relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")
        # =========Button=====================================
        searchbtn = Button(Detail_Frame, text="Search", command=self.search_data, width=10).grid(row=0, column=3,
                                                                                                 padx=10, pady=10)
        showallbtn = Button(Detail_Frame, text="Show all", command=self.fetch, width=10).grid(row=0, column=4, padx=10,
                                                                                              pady=10)

        # ========Table Frame=================================
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="yellow")
        Table_Frame.place(x=10, y=70, width=805, height=605)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(Table_Frame,
                                          columns=("roll", "name", "email", "gender", "contact", "dob", "address"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("contact", text="Contact")
        self.student_table.heading("dob", text="D.O.B")
        self.student_table.heading("address", text="Address")
        self.student_table['show'] = 'headings'
        self.student_table.column("roll", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("contact", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("address", width=180)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind('<ButtonRelease-1>', self.get_cursor)
        self.root.mainloop()

    def add_students(self):
        try:
            if self.Roll_No_var.get() != '' and self.name_var.get() != '' and self.email_var.get() != '' and \
                    self.gender_var.get() != '' and self.contact_var.get() != '' and self.dob_var.get() != '' and \
                    self.address_var.get() != '':

                con = pymysql.connect(host="localhost", user="root", password="", database="student")
                cur = con.cursor()
                cur.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s)', (
                    self.Roll_No_var.get(), self.name_var.get(), self.email_var.get(), self.gender_var.get(),
                    self.contact_var.get(), self.dob_var.get(), self.address_var.get()))
                con.commit()
                self.fetch()
                self.clear()
                con.close()
                messagebox.showinfo('Success', 'Added Successfully')
            else:
                messagebox.showerror('Error', 'Fill All the fields')

        except Exception as a:
            print(a)

    def fetch(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="student")
        cur = con.cursor()
        cur.execute('select * from student')
        data = cur.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in data:
                self.student_table.insert('', END, values=row)
                con.commit()
        con.close()

    def get_cursor(self, ev):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.address_var.set(row[6])

    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.address_var.set("")

    def clear_data(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.address_var.set("")

    def update(self):

        if self.Roll_No_var.get() != '' and self.name_var.get() != '' and self.email_var.get() != ''\
                and self.gender_var.get() != '' and self.contact_var.get() != '' and self.dob_var.get() != '' and\
                self.address_var.get() != '':

            con = pymysql.connect(host="localhost", user="root", password="", database="student")
            cur = con.cursor()
            cur.execute(
                "update student set name = %s, email = %s,  gender= %s, contact= %s, dob= %s, address= %s where roll = %s",
                (
                    self.name_var.get(), self.email_var.get(), self.gender_var.get(),
                    self.contact_var.get(), self.dob_var.get(), self.address_var.get(), self.Roll_No_var.get()))
            con.commit()
            self.fetch()
            self.clear()
            con.close()
            messagebox.showinfo('Success', 'Updated Successfully')
        else:
            messagebox.showerror('Error', 'Fill All the fields')

    def delete_data(self):
        if self.Roll_No_var.get() != '' and self.name_var.get() != '' and self.email_var.get() != '' \
                and self.gender_var.get() != '' and self.contact_var.get() != '' and self.dob_var.get() != '' and self\
                .address_var.get() != '':

            con = pymysql.connect(host="localhost", user="root", password="", database="student")
            cur = con.cursor()
            cur.execute(f"delete from student where roll=%s",(self.Roll_No_var.get()))
            con.commit()
            con.close()
            self.fetch()
            self.clear()
            messagebox.showinfo('Success', 'Deleted Successfully')
        else:
            messagebox.showerror('Error','All fields are empty')

    def search_data(self):
        try:
            if self.search_txt.get() != "":
                con = pymysql.connect(host="localhost", user="root", password="", database="student")
                cur = con.cursor()
                cur.execute(
                    "select * from student where " + self.search_by.get() + "  like '" + self.search_txt.get() + "%' ")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert('', END, values=row)
                    con.commit()
                con.close()

            else:
                messagebox.showerror("Empty", "It cannot be empty")

        except Exception as e:
            print(e)





# ob = students()
