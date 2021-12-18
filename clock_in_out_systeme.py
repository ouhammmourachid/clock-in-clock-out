from sqlite3.dbapi2 import connect
import tkinter as tk
from tkinter import Label, messagebox
import sqlite3

Next = 0


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#fa7e61")
        Frame_login = tk.Frame(self, bg="#faff81")
        Frame_login.place(x=380, y=110, height=300, width=320)

        L1 = tk.Label(Frame_login,
                      text="Username",
                      font=("Goudy old style", 10, "bold"),
                      fg="black",
                      bg="#faff81").place(x=30, y=90)
        T1 = tk.Entry(Frame_login, font=("times new roman", 15))
        T1.place(x=30, y=120, width=250, height=35)

        L2 = tk.Label(Frame_login,
                      text="Password",
                      font=("Goudy old style", 10, "bold"),
                      fg="black",
                      bg="#faff81").place(x=30, y=160)
        T2 = tk.Entry(Frame_login, font=("times new roman", 15), show="*")
        T2.place(x=30, y=190, width=250, height=35)

        def verify():
            # sqle3 for login
            db = sqlite3.connect("database.db")
            db.row_factory = sqlite3.Row
            cursor = db.execute("select * from admin")
            for row in cursor:
                if row['username'] == str(T1.get()):
                    a=row
            try:
                if a['password']==str(T2.get()):
                    T1.delete(0, "end")
                    T2.delete(0, "end")
                    controller.show_frame(HomePage)

                else:
                    T1.delete(0, "end")
                    T2.delete(0, "end")
                    messagebox.showinfo(
                        "Error",
                        "Please provide correct username and password!!")
            except:
                T1.delete(0, "end")
                T2.delete(0, "end")
                messagebox.showinfo("Error","Please provide correct username and password!!")

            db.close()

        Login_btn = tk.Button(Frame_login,
                              text="Login",
                              fg="black",
                              bg="#6e44ff",
                              font=("times new roman", 20),
                              command=verify).place(x=100,
                                                    y=245,
                                                    width=125,
                                                    height=40)
        esc1 = tk.Label(Frame_login,
                        text="  Admin Login Area  ",
                        font=("Goudy old style", 20, "bold"),
                        fg="#2b4162",
                        bg="#faff81").place(x=0, y=15)
        esc2 = tk.Label(Frame_login,
                        text=" --------------------------- ",
                        font=("Goudy old style", 20, "bold"),
                        fg="black",
                        bg="#faff81").place(x=0, y=50)


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg="#a3cef1")
        tk.Label(self,
                 text="{ home page }",
                 font=("Goudy old style", 20, "bold"),
                 fg="black",
                 bg="#a3cef1").place(x=400, y=0)

        def Home():
            controller.show_frame(HomePage)

        def Exit():
            controller.show_frame(LoginPage)

        def Setting():
            controller.show_frame(SettingPage)

        def Employee():
            controller.show_frame(EmployeePage)

        def Statistic():
            controller.show_frame(StatisticsPage)

        T1 = tk.Button(self,
                       text="home",
                       fg="black",
                       bg="#6e44ff",
                       font=("times new roman", 15),
                       command=Home).place(x=950, y=150, width=100, height=40)
        T2 = tk.Button(self,
                       text="exit",
                       fg="black",
                       bg="#6e44ff",
                       font=("times new roman", 15),
                       command=Exit).place(x=950, y=200, width=100, height=40)
        T3 = tk.Button(self,
                       text="settings",
                       fg="black",
                       bg="#6e44ff",
                       font=("times new roman", 15),
                       command=Setting).place(x=950,
                                              y=250,
                                              width=100,
                                              height=40)
        T4 = tk.Button(self,
                       text="employees",
                       fg="black",
                       bg="#6e44ff",
                       font=("times new roman", 15),
                       command=Employee).place(x=950,
                                               y=300,
                                               width=100,
                                               height=40)
        T5 = tk.Button(self,
                       text="statistics",
                       fg="black",
                       bg="#6e44ff",
                       font=("times new roman", 15),
                       command=Statistic).place(x=950,
                                                y=350,
                                                width=100,
                                                height=40)
        L = tk.Label(self,
                     text="""
Our Clock-in clock-out system allows employe to log their shift, track work hours, and report            
overtime.It’s an efficient way of tracking time, managing attendance, and it helps to calculate          
exact wages.Time clock is popular in many companies and used in various forms. It’s a great             
timekeeping system that helps to save time and money.If you want to set up an effective clock-in     
and out system in your company,our provide a data secure data base to store employee information 
that include :                                                                                                                                                
+add employee.                                                                                                                         
+update employee.                                                                                                                    
+delete employee.                                                                                                                     
+affichage employee information.                                                                                            
and an interface to change admin configiration beside that our systeme use the technology of NFC     
and arduino to registre time of clock-in and clock-out automatically without human intervention.         """,
                     font=("Goudy old style", 11, "bold"),
                     bg="#a3cef1").place(x=50, y=50, width=840, height=350)


class SettingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg="#a3cef1")
        tk.Label(self,
                 text="{ setting page }",
                 font=("Goudy old style", 20, "bold"),
                 fg="black",
                 bg="#a3cef1").place(x=400, y=0)

        lbl = tk.Label(self,
                       text="To change admin username and password !",
                       font=("Goudy old style", 10, "bold"),
                       fg='black',
                       bg="#a3cef1").place(x=360, y=100)
        T1 = tk.Label(self,
                      text="the new username: *",
                      font=("Goudy old style", 10, "bold"),
                      fg="red",
                      bg="#a3cef1").place(x=390, y=140)
        L1 = tk.Entry(self, font=("times new roman", 15), bg="lightgray")
        L1.place(x=390, y=170, width=250, height=35)
        T2 = tk.Label(self,
                      text="the new Password: *",
                      font=("Goudy old style", 10, "bold"),
                      fg="red",
                      bg="#a3cef1").place(x=390, y=220)
        L2 = tk.Entry(self,
                      font=("times new roman", 15),
                      bg="lightgray",
                      show="*")
        L2.place(x=390, y=250, width=250, height=35)
        L3 = tk.Label(self,
                      text="Confirme the new Password: *",
                      font=("Goudy old style", 10, "bold"),
                      fg="red",
                      bg="#a3cef1").place(x=390, y=300)
        L3 = tk.Entry(self,
                      font=("times new roman", 15),
                      bg="lightgray",
                      show="*")
        L3.place(x=390, y=330, width=250, height=35)

        def Home():
            controller.show_frame(HomePage)

        def Exit():
            controller.show_frame(LoginPage)

        def Setting():
            controller.show_frame(SettingPage)

        def Employee():
            controller.show_frame(EmployeePage)

        def Statistic():
            controller.show_frame(StatisticsPage)

        T1 = tk.Button(self,
                       text="home",
                       fg="black",
                       bg="#6e44ff",
                       font=("times new roman", 15),
                       command=Home).place(x=950, y=150, width=100, height=40)
        T2 = tk.Button(self,
                       text="exit",
                       fg="black",
                       bg="#6e44ff",
                       font=("times new roman", 15),
                       command=Exit).place(x=950, y=200, width=100, height=40)
        T3 = tk.Button(self,
                       text="settings",
                       fg="black",
                       bg="#6e44ff",
                       font=("times new roman", 15),
                       command=Setting).place(x=950,
                                              y=250,
                                              width=100,
                                              height=40)
        T4 = tk.Button(self,
                       text="employees",
                       fg="black",
                       bg="#6e44ff",
                       font=("times new roman", 15),
                       command=Employee).place(x=950,
                                               y=300,
                                               width=100,
                                               height=40)
        T5 = tk.Button(self,
                       text="statistics",
                       fg="black",
                       bg="#6e44ff",
                       font=("times new roman", 15),
                       command=Statistic).place(x=950,
                                                y=350,
                                                width=100,
                                                height=40)

        def ChangePassword():
            db = sqlite3.connect("database.db")
            try:
                if str(L2.get()) != str(L3.get()):
                    messagebox.showinfo(
                        "Error",
                        "the new password and configuration password don't mutch"
                    )
                    L2.delete(0, "end")
                    L3.delete(0, "end")

                else:
                    db.execute(
                        "create table if not exists admin(username text,password text)"
                    )
                    db.row_factory = sqlite3.Row
                    cursor = db.execute("select * from admin")

                    for row in cursor:
                        db.execute(
                            f"update admin set password='{str(L2.get())}' where username='{row['username']}'"
                        )
                        db.execute(
                            f"update admin set username='{str(L1.get())}' where username='{row['username']}'"
                        )
                        db.commit()
                    L1.delete(0, "end")
                    L2.delete(0, "end")
                    L3.delete(0, "end")
                    messagebox.showinfo(
                        "Information",
                        "the change of password is sussesfully!!")
            except:
                messagebox.showinfo("Error","you provide unvalide username or password")
                L2.delete(0, "end")
                L3.delete(0, "end")
            db.close()

        B = tk.Button(self, text="Change",
                      command=ChangePassword).place(x=450,
                                                    y=400,
                                                    width=125,
                                                    height=40)

x0=50
class EmployeePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg="#a3cef1")
        tk.Label(self,
                 text="{ employee page }",
                 font=("Goudy old style", 20, "bold"),
                 fg="black",
                 bg="#a3cef1").place(x=400, y=0)

        def Home():
            controller.show_frame(HomePage)

        def Exit():
            controller.show_frame(LoginPage)

        def Setting():
            controller.show_frame(SettingPage)

        def Employee():
            controller.show_frame(EmployeePage)

        def Statistic():
            controller.show_frame(StatisticsPage)

        T1 = tk.Button(self,
                       text="home",
                       fg="black",
                       bg="#6e44ff",
                       font=("times new roman", 15),
                       command=Home).place(x=950, y=150, width=100, height=40)
        T2 = tk.Button(self,
                       text="exit",
                       fg="black",
                       bg="#6e44ff",
                       font=("times new roman", 15),
                       command=Exit).place(x=950, y=200, width=100, height=40)
        T3 = tk.Button(self,
                       text="settings",
                       fg="black",
                       bg="#6e44ff",
                       font=("times new roman", 15),
                       command=Setting).place(x=950,
                                              y=250,
                                              width=100,
                                              height=40)
        T4 = tk.Button(self,
                       text="employees",
                       fg="black",
                       bg="#6e44ff",
                       font=("times new roman", 15),
                       command=Employee).place(x=950,
                                               y=300,
                                               width=100,
                                               height=40)
        T5 = tk.Button(self,
                       text="statistics",
                       fg="black",
                       bg="#6e44ff",
                       font=("times new roman", 15),
                       command=Statistic).place(x=950,
                                                y=350,
                                                width=100,
                                                height=40)
        deco = tk.Label(self,
                        text="<<",
                        font=("Goudy old style", 20, "bold"),
                        fg="black",
                        bg="#a3cef1").place(x=900, y=300)
        mainframe = tk.Frame(self,bg="#dd99bb")
        mainframe.place(x=30, y=50, height=480, width=780)
        mm = tk.Label(self,
                        text="<<",
                        font=("Goudy old style", 12, "bold"),
                        fg="black",
                        bg="#a3cef1").place(x=810, y=310)
        def frameadd():
            fram2 = tk.Frame(self,bg="#dd99bb")
            fram2.place(x=30, y=50, height=480, width=780)
            al1 = tk.Label(fram2,
                           text="Full name                   :",
                           font=("Goudy old style", 15, "bold"),
                           bg="#dd99bb").place(x=140, y=50)
            al2 = tk.Label(fram2,
                           text="Email                          :",
                           font=("Goudy old style", 15, "bold"),
                           bg="#dd99bb").place(x=140, y=90)
            al3 = tk.Label(fram2,
                           text="Id employee               :",
                           font=("Goudy old style", 15, "bold"),
                           bg="#dd99bb").place(x=140, y=130)
            al4 = tk.Label(fram2,
                           text="National ID number   :",
                           font=("Goudy old style", 15, "bold"),
                           bg="#dd99bb").place(x=140, y=170)
            al5 = tk.Label(fram2,
                           text="Region                        :",
                           font=("Goudy old style", 15, "bold"),
                           bg="#dd99bb").place(x=140, y=210)
            al6 = tk.Label(fram2,
                           text="Speciality                   :",
                           font=("Goudy old style", 15, "bold"),
                           bg="#dd99bb").place(x=140, y=250)
            al7 = tk.Label(fram2,
                           text="Mobile phone number:",
                           font=("Goudy old style", 15, "bold"),
                           bg="#dd99bb").place(x=140, y=290)
            ae1 = tk.Entry(fram2, bg="lightgray")
            ae1.place(x=400, y=50,width=230)
            ae2 = tk.Entry(fram2, bg="lightgray")
            ae2.place(x=400, y=90, width=230)
            ae3 = tk.Entry(fram2, bg="lightgray")
            ae3.place(x=400, y=130, width=230)
            ae4 = tk.Entry(fram2, bg="lightgray")
            ae4.place(x=400, y=170, width=230)
            ae5 = tk.Entry(fram2, bg="lightgray")
            ae5.place(x=400, y=210, width=230)
            ae6 = tk.Entry(fram2, bg="lightgray")
            ae6.place(x=400, y=250, width=230)
            ae7 = tk.Entry(fram2, bg="lightgray")
            ae7.place(x=400, y=290, width=230)

            def AddEmployee():
                db = sqlite3.connect("database.db")
                db.execute(
                    "create table if not exists employee(full_name text,email text,id text,national_id text,region text,speciality text,telephone_number text)"
                )
                db.row_factory = sqlite3.Row
                cursor = db.execute("select * from employee")
                s = False
                try:
                    for row in cursor:
                        if row["id"] == str(ae3.get()):
                            s = True
                            a = row
                    if str(ae3.get())=='':
                        messagebox.showinfo(
                            "Error", "you have entered invalid information")
                    else:
                        if s:
                            messagebox.showinfo(
                                "Error",
                                f'this id is already associated to the employee {a["full_name"]} ,please try an other id'
                            )
                            ae3.delete(0, "end")
                        else:
                            db.execute(
                                "insert into employee(full_name,email,id,national_id,region,speciality,telephone_number) values(?,?,?,?,?,?,?)",
                                (ae1.get(), ae2.get(), ae3.get(), ae4.get(),ae5.get(), ae6.get(), ae7.get()))
                            db.commit()
                            messagebox.showinfo(
                                "Information",
                                f'you have add the employee {ae1.get()} successfully'
                            )
                            ae1.delete(0, "end")
                            ae2.delete(0, "end")
                            ae3.delete(0, "end")
                            ae4.delete(0, "end")
                            ae5.delete(0, "end")
                            ae6.delete(0, "end")
                            ae7.delete(0, "end")

                except:
                    messagebox.showinfo("Error",
                                        "you have entered invalid information")
                    ae1.delete(0, "end")
                    ae2.delete(0, "end")
                    ae3.delete(0, "end")
                    ae4.delete(0, "end")
                    ae5.delete(0, "end")
                    ae6.delete(0, "end")
                    ae7.delete(0, "end")

            abutton = tk.Button(fram2, text="Add", bg='green',command=AddEmployee).place(x=400, y=350)
        def framedelet():
            fram1 = tk.Frame(self,bg="#dd99bb")
            fram1.place(x=30, y=50, height=480, width=780)
            dl1 = tk.Label(fram1, text="full name                 :",
                           bg="#dd99bb").place(x=100, y=100)
            dl2 = tk.Label(fram1, text="national ID number :",
                           bg="#dd99bb").place(x=100, y=140)
            dl3 = tk.Label(fram1, text="       Id                      :",
                           bg="#dd99bb").place(x=100, y=180)
            de1 = tk.Entry(fram1, bg="lightgray")
            de1.place(x=400, y=100)
            de2 = tk.Entry(fram1, bg="lightgray")
            de2.place(x=400, y=140)
            de3 = tk.Entry(fram1, bg="lightgray")
            de3.place(x=400, y=180)

            def DeleteEmployee():
                db = sqlite3.connect("database.db")
                db.row_factory = sqlite3.Row
                cursor = db.execute("select * from employee")
                s = False
                for row in cursor:
                    if row["id"] == str(de3.get()):
                        s = True
                        a = row
                if s:

                    messagebox.showinfo(
                        "Information",
                        f'you deleted the employee {a["full_name"]} successfully'
                    )
                    db.execute(f'delete from employee where id="{de3.get()}"')
                    db.commit()
                    de1.delete(0, "end")
                    de2.delete(0, "end")
                    de3.delete(0, "end")
                else:
                    de1.delete(0, "end")
                    de2.delete(0, "end")
                    de3.delete(0, "end")
                    messagebox.showinfo("Eroor",
                                        "there is no employee with such an id !!")

            dbutton = tk.Button(fram1,
                            text="delete",
                            bg='red',
                            command=DeleteEmployee).place(x=300, y=320)
        def frameupdat():
            fram3 = tk.Frame(self, bg="#dd99bb")
            fram3.place(x=30, y=50, height=480, width=780)
            ul1 = tk.Label(fram3,
                           text="Full name                   :",
                           font=("Goudy old style", 15, "bold"),
                           bg="#dd99bb").place(x=140, y=50)
            ul2 = tk.Label(fram3,
                           text="Email                          :",
                           font=("Goudy old style", 15, "bold"),
                           bg="#dd99bb").place(x=140, y=90)
            ul3 = tk.Label(fram3,
                           text="Id employee               :",
                           font=("Goudy old style", 15, "bold"),
                           bg="#dd99bb").place(x=140, y=130)
            ul4 = tk.Label(fram3,
                           text="National ID number   :",
                           font=("Goudy old style", 15, "bold"),
                           bg="#dd99bb").place(x=140, y=170)
            ul5 = tk.Label(fram3,
                           text="Region                        :",
                           font=("Goudy old style", 15, "bold"),
                           bg="#dd99bb").place(x=140, y=210)
            ul6 = tk.Label(fram3,
                           text="Speciality                   :",
                           font=("Goudy old style", 15, "bold"),
                           bg="#dd99bb").place(x=140, y=250)
            ul7 = tk.Label(fram3,
                           text="Mobile phone number:",
                           font=("Goudy old style", 15, "bold"),
                           bg="#dd99bb").place(x=140, y=290)
            ue1 = tk.Entry(fram3, bg="lightgray")
            ue1.place(x=400, y=50,width=230)
            ue2 = tk.Entry(fram3, bg="lightgray")
            ue2.place(x=400, y=90, width=230)
            ue3 = tk.Entry(fram3, bg="lightgray")
            ue3.place(x=400, y=130, width=230)
            ue4 = tk.Entry(fram3, bg="lightgray")
            ue4.place(x=400, y=170, width=230)
            ue5 = tk.Entry(fram3, bg="lightgray")
            ue5.place(x=400, y=210, width=230)
            ue6 = tk.Entry(fram3, bg="lightgray")
            ue6.place(x=400, y=250, width=230)
            ue7 = tk.Entry(fram3, bg="lightgray")
            ue7.place(x=400, y=290, width=230)

            def UpdateEmployee():
                db = sqlite3.connect("database.db")
                db.row_factory = sqlite3.Row
                cursor = db.execute("select * from employee")
                s = False
                try:
                    for row in cursor:
                        if row["id"] == str(ue3.get()):
                            s = True
                    if s:
                        db.execute(
                            f"update employee set full_name='{ue1.get()}' where id='{ue3.get()}'"
                        )
                        db.execute(
                            f"update employee set email='{ue2.get()}' where id='{ue3.get()}'"
                        )
                        db.execute(
                            f"update employee set national_id='{ue4.get()}' where id='{ue3.get()}'"
                        )
                        db.execute(
                            f"update employee set region='{ue5.get()}' where id='{ue3.get()}'"
                        )
                        db.execute(
                            f"update employee set speciality='{ue6.get()}' where id='{ue3.get()}'"
                        )
                        db.execute(
                            f"update employee set telephone_number='{ue7.get()}' where id='{ue3.get()}'"
                        )
                        db.commit()
                        messagebox.showinfo(
                            "Information",
                            f'''you had update the employee id  {ue4.get()} to :
    +full name : {ue1.get()} 
    +email : {ue2.get()} 
    +natinal ID number : {ue4.get()}  
    +region :{ue5.get()}   
    +speciality :{ue6.get()}  
    +telephone number :{ue7.get()}  ''')
                        ue1.delete(0, "end")
                        ue2.delete(0, "end")
                        ue3.delete(0, "end")
                        ue4.delete(0, "end")
                        ue5.delete(0, "end")
                        ue6.delete(0, "end")
                        ue7.delete(0, "end")
                    else:
                        ue1.delete(0, "end")
                        ue2.delete(0, "end")
                        ue3.delete(0, "end")
                        ue4.delete(0, "end")
                        ue5.delete(0, "end")
                        ue6.delete(0, "end")
                        ue7.delete(0, "end")
                        messagebox.showinfo(
                            "Error",
                            f'there is no such an employee with id : {ue3.get()}')
                except:
                    messagebox.showinfo("Error",
                                        "you have entered invalid information")
                    ue1.delete(0, "end")
                    ue2.delete(0, "end")
                    ue3.delete(0, "end")
                    ue4.delete(0, "end")
                    ue5.delete(0, "end")
                    ue6.delete(0, "end")
                    ue7.delete(0, "end")
            ubutton = tk.Button(fram3,
                            text="Update",
                            bg='blue',
                            command=UpdateEmployee).place(x=400, y=350)
        def framaffiche():
            fram4 = tk.Frame(self, bg="#dd99bb")
            fram4.place(x=30, y=50, height=480, width=780)
            fl1 = tk.Label(fram4,
                           text="Full name                   :",
                           font=("Goudy old style", 15, "bold"),
                           bg="#dd99bb").place(x=140, y=50)
            fl2 = tk.Label(fram4,
                           text="Email                          :",
                           font=("Goudy old style", 15, "bold"),
                           bg="#dd99bb").place(x=140, y=90)
            fl3 = tk.Label(fram4,
                           text="Id employee               :",
                           font=("Goudy old style", 15, "bold"),
                           bg="#dd99bb").place(x=140, y=130)
            fl4 = tk.Label(fram4,
                           text="National ID number   :",
                           font=("Goudy old style", 15, "bold"),
                           bg="#dd99bb").place(x=140, y=170)
            fl5 = tk.Label(fram4,
                           text="Region                        :",
                           font=("Goudy old style", 15, "bold"),
                           bg="#dd99bb").place(x=140, y=210)
            fl6 = tk.Label(fram4,
                           text="Speciality                   :",
                           font=("Goudy old style", 15, "bold"),
                           bg="#dd99bb").place(x=140, y=250)
            fl7 = tk.Label(fram4,
                           text="Mobile phone number:",
                           font=("Goudy old style", 15, "bold"),
                           bg="#dd99bb").place(x=140, y=290)

            fe3=tk.Entry(fram4,bg="lightgray")
            fe3.place(x=400,y=130)
            def Affiche():
                db = sqlite3.connect("database.db")
                db.row_factory = sqlite3.Row
                cursor = db.execute("select * from employee")
                s = False
                try:
                    for row in cursor:
                        if row["id"] == str(fe3.get()):
                            s = True
                            a=row
                    if s:
                        fe1 = tk.Label(fram4,
                                        text=str(a["full_name"]),
                                        font=("Goudy old style", 15, "bold"),
                                        bg="#dd99bb").place(x=420, y=50)
                        fe2 = tk.Label(fram4,
                                       text=str(a["email"]),
                                       font=("Goudy old style", 15, "bold"),
                                       bg="#dd99bb").place(x=420, y=90)
                        fe4 = tk.Label(fram4,
                                       text=str(a["national_id"]),
                                       font=("Goudy old style", 15, "bold"),
                                       bg="#dd99bb").place(x=420, y=170)
                        fe5 = tk.Label(fram4,
                                       text=str(a["region"]),
                                       font=("Goudy old style", 15, "bold"),
                                       bg="#dd99bb").place(x=420, y=210)
                        fe6 = tk.Label(fram4,
                                       text=str(a["speciality"]),
                                       font=("Goudy old style", 15, "bold"),
                                       bg="#dd99bb").place(x=420, y=250)
                        fe7 = tk.Label(fram4,
                                       text=str(a["telephone_number"]),
                                       font=("Goudy old style", 15, "bold"),
                                       bg="#dd99bb").place(x=420, y=290)
                    else:
                        messagebox.showinfo(
                            "Error", "you have entered invalid Id Employee")
                        ue1.delete(0, "end")
                except:
                    messagebox.showinfo(
                        "Error", "you have entered invalid Id Employee")
                    ue1.delete(0, "end")
            fbutton = tk.Button(fram4,
                                    text="affichage",
                                    bg='blue',
                                    command=Affiche).place(x=400, y=350)





        fb1 = tk.Button(self,
                        text='add',
                        fg="black",
                        font=("times new roman", 10),
                        bg="#02c39a",
                        command=frameadd).place(x=850, y=260, width=44)
        fb2 = tk.Button(self,
                        text='update',
                        fg="black",
                        font=("times new roman", 10),
                        bg="#02c39a",
                        command=frameupdat).place(x=850, y=290, width=44)
        fb3 = tk.Button(self,
                        text='delete',
                        fg="black",
                        font=("times new roman", 10),
                        bg="#02c39a",
                        command=framedelet).place(x=850, y=320, width=44)
        fb4 = tk.Button(self,
                        text='affiche',
                        fg="black",
                        font=("times new roman", 10),
                        bg="#02c39a",command=framaffiche).place(x=850, y=350, width=44)



class StatisticsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg="#a3cef1")
        tk.Label(self,
                 text="{ statistics page }",
                 font=("Goudy old style", 20, "bold"),
                 fg="black",
                 bg="#a3cef1").place(x=400, y=0)


        def Home():
            controller.show_frame(HomePage)

        def Exit():
            controller.show_frame(LoginPage)

        def Setting():
            controller.show_frame(SettingPage)

        def Employee():
            controller.show_frame(EmployeePage)

        def Statistic():
            controller.show_frame(StatisticsPage)

        T1 = tk.Button(self,
                       text="home",
                       fg="black",
                       bg="#6e44ff",
                       font=("times new roman", 15),
                       command=Home).place(x=950, y=150, width=100, height=40)
        T2 = tk.Button(self,
                       text="exit",
                       fg="black",
                       bg="#6e44ff",
                       font=("times new roman", 15),
                       command=Exit).place(x=950, y=200, width=100, height=40)
        T3 = tk.Button(self,
                       text="settings",
                       fg="black",
                       bg="#6e44ff",
                       font=("times new roman", 15),
                       command=Setting).place(x=950,
                                              y=250,
                                              width=100,
                                              height=40)
        T4 = tk.Button(self,
                       text="employees",
                       fg="black",
                       bg="#6e44ff",
                       font=("times new roman", 15),
                       command=Employee).place(x=950,
                                               y=300,
                                               width=100,
                                               height=40)
        T5 = tk.Button(self,
                       text="statistics",
                       fg="black",
                       bg="#6e44ff",
                       font=("times new roman", 15),
                       command=Statistic).place(x=950,
                                                y=350,
                                                width=100,
                                                height=40)
        mainframe = tk.Frame(self, bg="#dd99bb")
        mainframe.place(x=50, y=200, height=100, width=800)
        name=tk.Label(mainframe,text="Empolyee name").place(x=20,y=10)
        id = tk.Label(mainframe, text="Empolyee id").place(x=220, y=10)
        clock_in = tk.Label(mainframe, text="clockin hour").place(x=420, y=10)
        clock_out = tk.Label(mainframe, text="clockin out").place(x=620, y=10)

        def NextEployee():
            global Next
            db=connect("database.db")
            db.row_factory = sqlite3.Row
            cursor = db.execute("select * from hours")
            i=0
            for row in cursor:
                a=row
                if i==Next:
                    break
                i+=1
            Next+=1
            L1=tk.Label(mainframe,text=str(a["name"])).place(x=20,y=60,width=100)
            L2 = tk.Label(mainframe, text=str(a["id"])).place(x=220, y=60)
            L3 = tk.Label(mainframe, text=str(a['clock_in'])).place(x=440, y=60)
            L4 = tk.Label(mainframe, text=str(a['clock_out'])).place(x=640, y=60)
        def PreviosEmployee():
            global Next
            db = connect("database.db")
            db.row_factory = sqlite3.Row
            cursor = db.execute("select * from hours")
            i = 0
            Next -= 1
            for row in cursor:
                a = row
                if i == Next:
                    break
                i+=1
            L1 = tk.Label(mainframe, text=str(a["name"])).place(x=20, y=60,width=100)
            L2 = tk.Label(mainframe, text=str(a["id"])).place(x=220, y=60)
            L3 = tk.Label(mainframe, text=str(a['clock_in'])).place(x=440,
                                                                    y=60)
            L4 = tk.Label(mainframe, text=str(a['clock_out'])).place(x=640,
                                                                     y=60)

        next_employee=tk.Button(self,text="next emloyee >>",command=NextEployee).place(x=600,y=320)
        previos_employee=tk.Button(self,text="<< previos emloyee ",command=PreviosEmployee).place(x=100,y=320,width=150)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # creating a window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=566)
        window.grid_columnconfigure(0, minsize=1080)

        self.frames = {}
        for F in (HomePage, LoginPage, SettingPage, EmployeePage,
                  StatisticsPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("<clock in/out systeme>")


app = Application()
app.geometry("1080x566")
app.resizable(False, False)
app.mainloop()