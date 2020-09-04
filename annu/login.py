from tkinter import *
from tkinter import messagebox
import pymysql

from registration import registration
from students import students


class LoginView:
    def __init__(self):
        self.window = Tk()
        self.window.title("User Login")
        self.window.configure(background='red')
        self.window.geometry("600x300+500+200")
        #=======Frame===================
        self.frame_heading = Frame(self.window)
        self.frame_heading.pack()
        self.un = StringVar()
        self.pw = StringVar()
        self.frame_login = Frame(self.window, bg='yellow')
        self.frame_login.pack()
        #===========Label============
        self.label_un = Label(self.frame_login, font=('Calibri',20, 'bold'), bg='red', text="Username")
        self.label_un.grid(row=0, column=0, pady=10, padx=10, sticky=W)
        #============Entry=================
        self.entry_un = Entry(self.frame_login, textvariable=self.un, font=('arial', 10, 'bold'),bd=5,relief=GROOVE)
        self.entry_un.grid(row=0, column=1, padx=10, pady=10)
        #============Label==================
        self.label_pw = Label(self.frame_login, font=('Calibri', 20, 'bold'), bg='red', text="Password")
        self.label_pw.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        #===========Entry====================
        self.entry_pw = Entry(self.frame_login, show='*', textvariable=self.pw, font=('arial', 10, 'bold'),bd=5,relief=GROOVE)
        self.entry_pw.grid(row=1, column=1, padx=10, pady=10)
        #========Button==========
        self.btn_login = Button(self.frame_login, bg='red', text="Log In", font=('Calibri', 20, 'bold'),
                                command=self.on_login_click)
        self.btn_login.grid(row=2, column=0)
        self.btn_regis = Button(self.frame_login, bg='red', text="Sign Up", font=('Calibri', 20, 'bold'),
                                command=self.signup)
        self.btn_regis.grid(row=2, column=1)
        self.window.mainloop()
        #======Function=============
    def on_login_click(self):
        if self.un.get() == '' or self.pw.get() == '':
            messagebox.showwarning('Error', 'All Fields Are Required')
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', database='student')
                cur = con.cursor()
                cur.execute('select * from users where username=%s and password=%s', (self.un.get(), self.pw.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror('Error', 'Invalid Id Or Password')
                else:
                    messagebox.showinfo('Success', 'Welcome')
                    self.window.destroy()
                    iv=students()
            except Exception as e:
                print(e)
                return False
    def signup(self):
        messagebox.showinfo('Success', 'Going To The Registration Form')
        self.window.destroy()
        iv=registration()

LoginView()