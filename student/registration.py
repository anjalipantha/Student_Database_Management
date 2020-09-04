import tkinter
from tkinter import messagebox
from tkinter import *
import pymysql

class registration:
    def __init__(self):
        self.window = Tk()
        self.window.title("Registration")
        self.window.configure(background='yellow')
        self.window.geometry("1000x500")
        self.frame_heading = Frame(self.window)
        self.frame_heading.pack()
        self.label_name = Label(self.frame_heading, bg='red', text="Registration", font=('Arial', 20, 'bold'))
        self.label_name.pack()
        self.frame_login = Frame(self.window, bg='grey')
        self.frame_login.pack()
        self.label_un = Label(self.frame_login, font=('Calibri', 20, 'bold'), bg='red', text="Username")
        self.label_un.grid(row=0, column=0, pady=10, padx=10, sticky=W)
        self.entry_un = Entry(self.frame_login, font=('arial', 10, 'bold'),bd=5,relief=GROOVE)
        self.entry_un.grid(row=0, column=1, padx=10, pady=10)
        self.label_pw = Label(self.frame_login, font=('Calibri', 20, 'bold'), bg='red', text="Password")
        self.label_pw.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.entry_pw = Entry(self.frame_login, show='*', font=('arial', 10, 'bold'),bd=5,relief=GROOVE)
        self.entry_pw.grid(row=1, column=1, padx=10, pady=10)
        self.label_n = Label(self.frame_login, font=('Calibri', 20, 'bold'), bg='red', text="Name")
        self.label_n.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        self.entry_n = Entry(self.frame_login, font=('arial', 10, 'bold'),bd=5,relief=GROOVE)
        self.entry_n.grid(row=2, column=1, padx=10, pady=10)
        self.label_a = Label(self.frame_login, font=('Calibri', 20, 'bold'), bg='red', text="Address")
        self.label_a.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        self.entry_a = Entry(self.frame_login, font=('arial', 10, 'bold'),bd=5,relief=GROOVE)
        self.entry_a.grid(row=3, column=1, padx=10, pady=10)
        self.label_p = Label(self.frame_login, font=('Calibri', 20, 'bold'), bg='red', text="Phone")
        self.label_p.grid(row=4, column=0, padx=10, pady=10, sticky=W)
        self.entry_p = Entry(self.frame_login, font=('arial', 10, 'bold'),bd=5,relief=GROOVE)
        self.entry_p.grid(row=4, column=1, padx=10, pady=10)
        self.label_e = Label(self.frame_login, font=('Calibri', 20, 'bold'), bg='red', text="Email")
        self.label_e.grid(row=5, column=0, padx=10, pady=10, sticky=W)
        self.entry_e = Entry(self.frame_login, font=('arial', 10, 'bold'),bd=5,relief=GROOVE)
        self.entry_e.grid(row=5, column=1, padx=10, pady=10)
        # self.label_t = Label(self.frame_login, font=('Calibri', 15, 'bold'), bg='grey', text="Type")
        # self.label_t.grid(row=6, column=0, padx=10, pady=10, sticky=W)
        #
        # self.entry_t = Entry(self.frame_login, font=('arial', 10, 'bold'))
        # self.entry_t.grid(row=6, column=1, padx=10, pady=10)
        self.btn_regis = Button(self.frame_login, bg='grey', command=self.submit, text="Submit",
                                font=('Calibri', 20, 'bold'))
        self.btn_regis.grid(row=7, column=1)
        self.btn_back = Button(self.frame_login, bg='grey', text="Back", command=self.back,
                               font=('Calibri', 20, 'bold'))
        self.btn_back.grid(row=7, column=0)
        self.btn_reset = Button(self.frame_login, text='Reset', bg='grey', font=('Calibri', 20, 'bold'), fg='black',
                                command=self.reset)
        """Allows user to clear the entry box."""
        self.btn_reset.grid(row=7, column=2)
        self.window.mainloop()
    def reset(self):
        if self.entry_un.get() != '' and self.entry_pw.get() != '' and self.entry_n.get() != '' and \
                self.entry_a.get() != '' and self.entry_p.get() != '' and self.entry_e.get() != '':
            self.entry_un.delete(0, END)
            self.entry_pw.delete(0, END)
            self.entry_n.delete(0, END)
            self.entry_a.delete(0, END)
            self.entry_p.delete(0, END)
            self.entry_e.delete(0, END)
        else:
            tkinter.messagebox.showerror('Error', 'Please Fill Out The All Empty Boxes.')
    def back(self):
        messagebox.showinfo('Back', 'Going To The Sign In ')
        self.window.destroy()
        import login
    def clear(self):
        self.entry_un.delete(0, END)
        self.entry_pw.delete(0, END)
        self.entry_n.delete(0, END)
        self.entry_a.delete(0, END)
        self.entry_p.delete(0, END)
        self.entry_e.delete(0, END)
    def submit(self):
        if self.entry_un.get() == '' or self.entry_pw.get() == '' or self.entry_n.get() == '' or self.entry_a.get() ==\
                '' or self.entry_p.get() == '' or self.entry_e.get() == '':
            messagebox.showwarning('Error', 'All Fields Are Required')
        else:
            messagebox.showinfo('Success', 'Register Successfully')
            try:
                con = pymysql.connect(host='localhost', user='root', password='', database='student')
                cur = con.cursor()
                cur.execute("insert into users (username,password,name,address,phone,email)"
                            " values(%s,%s,%s,%s,%s,%s)",
                            (self.entry_un.get(),
                             self.entry_pw.get(),
                             self.entry_n.get(),
                             self.entry_a.get(),
                             self.entry_p.get(),
                             self.entry_e.get()))
                con.commit()
                con.close()
                self.clear()
                self.window.destroy()
                import login
            except Exception as es:
                messagebox.showerror('Error', f'Error due to: {str(es)}')

# registration()