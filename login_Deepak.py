from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
#import loginDatabase
import sqlite3
#---------------------------------

#CREATE DATABASE StudentLogin IF NOT EXISTS;
with sqlite3.connect('StudentLogin.db') as db:
    cur = db.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS "Login" (   "id" INTEGER NOT NULL,"username"	TEXT NOT NULL,"password"	TEXT NOT NULL,PRIMARY KEY("id" AUTOINCREMENT));')
cur.execute('select * from Login')
db.commit()
db.close()


#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System".upper())
        self.root.geometry("1250x690+55+0")
        #----------------------------------------------BG IMAGE BLOCK----------------------------------------------------
        #-------------------------------------------------------------------------------------
        #self.bg=ImageTk.PhotoImage(file="/images/log.png")#G:\\DEEPAK\\2. PYTHON\\@ FINAL PROJECTS @\\1. STUDENT LOGIN PAGE\\bird bg3.jpg
        self.bg_image=Label(self.root)#,image=self.bg
        self.bg_image.place(x=0,y=0)
        self.root.resizable(False,False)

        #==================variables=====================
        #-----LOGIN VARIABLES
        self.username=StringVar()
        self.password=StringVar()
        #-----NEW USER VARIABLES
        

        #-----------------------------------------------LOGIN FRAME----------------------------------------------------
        #--------------------------------------------------------------------------------------------------------------
        self.con = sqlite3.connect('StudentLogin.db')
        self.cursor = self.con.cursor()
        

        Frame_login=Frame(self.root,bg='white')
        Frame_login.place(x=140,y=150,height=410,width=500)

        title=Label(Frame_login,text='Login Here',fon=('impact',35,'bold'),bg='white',fg='orange')
        title.place(x=110,y=0)
        desc=Label(Frame_login,text='Student Login System',fon=('Goudy',15,'bold'),bg='white',fg='orange')
        desc.place(x=110,y=70)


        lbl_username=Label(Frame_login,text='Username',fon=('times new roman',25,'bold'),bg='white',fg='gray')
        lbl_username.place(x=110,y=120)
        
        
        self.txt_username=Entry(Frame_login,textvariable=self.username,font=('times new roman',15),bg='lightgray')
        self.txt_username.focus()
        self.txt_username.place(x=110,y=170,height=35,width=280)


        lbl_password =Label(Frame_login,text='Password',fon=('times new roman',25,'bold'),bg='white',fg='gray')
        lbl_password.place(x=110,y=220)

        self.txt_password=Entry(Frame_login,show='*',textvariable=self.password,font=('times new roman',15),bg='lightgray')
        self.txt_password.place(x=110,y=270,height=35,width=280)


        forgetbtn=Button(Frame_login,text="Forget Password ?",bg='white',fg='orange',bd=0,font=('times new roman',15))
        forgetbtn.place(x=110,y=310)

        newuserbtn=Button(Frame_login,command=self.new_student,text="New Student",bg='white',fg='orange',bd=0,font=('times new roman',15))
        newuserbtn.place(x=110,y=345)


        loginbtn=Button(self.root,command=self.login,text="Login",fg='white',bg='orange',font=('times new roman',25),width=15)
        loginbtn.place(x=260,y=530)


#--------------------------LOGIN BUTTON FUNCTION--------------------------------
#-------------------------------------------------------------------------------

    def login(self):
        with sqlite3.connect('StudentLogin.db') as db:
            cur = db.cursor()
        find_user = ('SELECT * FROM Login WHERE username=? AND password=?')
        cur.execute(find_user,[self.username.get(), self.password.get()])
        results = cur.fetchall()
        if results:
            messagebox.showinfo('Login Info','Successfully Login')
            self.log()
        elif results == '':
            messagebox.showwarning('Login Warning', 'All Fields are required')
        else:
            messagebox.showerror(' Login Error', 'Username or password is incorrect')
            self.log()
            self.txt_username.focus()
    def log(self):
        self.username.set('')
        self.password.set('')

#====================== NEW LOGIN FUNCTION =================================

#---------------------------NEW STUDENT FUNCTION---------------------------------
#----------------------------------------------------------------------------------
    def new_student(self):
        self.new_student=Frame(self.root,bg='white')
        self.new_student.place(x=140,y=50,height=600,width=510)
        
        title=Label(self.new_student,text='New Student',fon=('impact',30,'bold'),bg='white',fg='orange')
        title.place(x=110,y=0)
        
        lbl_name=Label(self.new_student,text='Name ',fon=('times new roman',20,'bold'),bg='white',fg='gray')
        lbl_name.place(x=110,y=65)
        
        self.txt_name=Entry(self.new_student,font=('times new roman',15),bg='lightgray')
        self.txt_name.place(x=110,y=110,height=30,width=280)

        username_lbl=Label(self.new_student,text='Username ',fon=('times new roman',20,'bold'),bg='white',fg='gray')
        username_lbl.place(x=110,y=145)
        
        self.username_entry=Entry(self.new_student,font=('times new roman',15),bg='lightgray')
        self.username_entry.place(x=110,y=190,height=30,width=280)

        mobile_lbl=Label(self.new_student,text='Mobile ',fon=('times new roman',20,'bold'),bg='white',fg='gray')
        mobile_lbl.place(x=110,y=225)
        
        self.mobile_entry=Entry(self.new_student,font=('times new roman',15),bg='lightgray')
        self.mobile_entry.place(x=110,y=270,height=30,width=280)

        pass_lbl=Label(self.new_student,text='Password ',fon=('times new roman',20,'bold'),bg='white',fg='gray')
        pass_lbl.place(x=110,y=305)
        
        self.pass_entry=Entry(self.new_student,font=('times new roman',15),bg='lightgray')
        self.pass_entry.place(x=110,y=350,height=30,width=280)

        lbl_confirm_pass_lbl=Label(self.new_student,text='Confirm Password ',fon=('times new roman',20,'bold'),bg='white',fg='gray')
        lbl_confirm_pass_lbl.place(x=110,y=385)
        
        self.confirm_pass_entry=Entry(self.new_student,font=('times new roman',15),bg='lightgray')
        self.confirm_pass_entry.place(x=110,y=430,height=30,width=280)

        self.register_btn=Button(self.root,command=self.register,text="Register",fg='white',bg='orange',font=('times new roman',20),width=15)
        self.register_btn.place(x=280,y=620)
        
        back_btn=Button(self.new_student,command = self.back_func,text="<<<",bd=0,fg='orange',bg='white',font=('times new roman',20),width=5)
        back_btn.place(x=10,y=5)

        
#---------------------------BACK REGISTER FRAME ---------------------------------
#----------------------------------------------------------------------------------   
    def back_func(self):
        self.new_student.place_forget()
        self.register_btn.place_forget()
        #self.root()

#---------------------------REGISTER ACTION ---------------------------------
#----------------------------------------------------------------------------------
    def register(self):
        with sqlite3.connect('StudentLogin.db') as db:
            cur = db.cursor()
            
        insert = 'INSERT INTO Login (username,password) VALUES (?,?)'
        cur.execute(insert,[self.username_entry.get(),self.pass_entry.get()])
        db.commit()
        
        messagebox.showinfo('Message','Congratulations')




        
#------------------------------------------------------------------------------------------------------------------
root = Tk()
obj = Login(root)
root.mainloop()
