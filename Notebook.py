from tkinter import *
import mysql.connector as mysql
from tkinter import messagebox
from tkinter import ttk
def register():
    global f1,book,e1,e2
    def save():
        query="insert into register(first_name,last_name,username,password) values('{}','{}','{}','{}')". format(e1.get(),e2.get(),e3.get(),e4.get())
        cur.execute(query)
        cur.execute("commit")
        register()
    def show():
        e4.configure(show='')
    def hide():
        e4.configure(show='*')
    f1=Frame(root,bg="#EBD4B2",width=878,height=677).place(x=0,y=0)
    t=Label(f1,text="Register",fg="red",width=25,bg="#EBD4B2",font=('Britannic Bold',20,'bold')).place(x=150,y=10)
    book=PhotoImage(file="nobg.png")
    book_label=Label(f1,image=book)
    book_label.place(x=450,y=50)
    l1=Label(f1,text="First Name\t:",bg="#EBD4B2").place(x=50,y=75)
    l2=Label(f1,text="Last Name\t:",bg="#EBD4B2").place(x=50,y=175)
    l3=Label(f1,text="Username\t:",bg="#EBD4B2").place(x=50,y=275)
    l4=Label(f1,text="Password\t:",bg="#EBD4B2").place(x=50,y=375)
    e1=Entry(f1);    e2=Entry(f1)
    e3=Entry(f1)
    e4=Entry(f1,show='*')
    e1.place(x=250,y=75) ;e2.place(x=250,y=175); e3.place(x=250,y=275)
    e4.place(x=250,y=375)
    b1=Button(f1,text="Save",bg="#EBD4B2",fg="#142B4D",height=2,width=15,activebackground="#EBD4B2",activeforeground="#EBD4B2",command=save,font=('Britannic Bold',20,'bold')).place(x=100,y=500)
    b2=Button(f1,text="Login",bg="#EBD4B2",fg="#142B4D",height=2,width=15,activebackground="#EBD4B2",activeforeground="#EBD4B2",command=login,font=('Britannic Bold',20,'bold')).place(x=500,y=500)
    check1=Button(f1,text="Show",command=show,bg="#EBD4B2",fg="#142B4D",width=10,height=1,activebackground="#EBD4B2",activeforeground="#EBD4B2",font=('danfo',10,'bold')).place(x=450,y=375)
    check2=Button(f1,text="Hide",command=hide,bg="#EBD4B2",fg="#142B4D",width=10,activebackground="#EBD4B2",activeforeground="#EBD4B2",font=('danfo',10,'bold')).place(x=600,y=375)

def login():
    global e5,e6,login1
    def show():
        e6.configure(show='')
    def hide():
        e6.configure(show='*')
    def verify():
        if e5.get()=="":
          messagebox.showinfo("ERROR","Please fill the entry!!!")
          login()
        elif e6.get()=="":
            messagebox.showinfo("ERROR","Please fill the entry!!!")
            login()
        if e5.get()!="" and e6.get()!="":
            query="select * from register where username='{}'and password='{}'". format(e5.get(),e6.get())
            cur.execute(query)
            record=cur.fetchone()
            if record==None:
                messagebox.showinfo("ERROR","Invalid username or password!!!")
                login()
            else:
                messagebox.showinfo("Message","Loged in successfully!!!")
                messagebox.showinfo("ID",record[0])
                main_window()
    f2=Frame(root,bg="#EBD4B2",width=878,height=677).place(x=0,y=0)
    login1=PhotoImage(file="login_bg.png")
    img_label=Label(f2,image=login1)
    img_label.place(x=350,y=100)
    t=Label(f2,text="Login",fg="red",width=25,bg="#EBD4B2",font=('Britannic Bold',20,'bold')).place(x=150,y=0)
    l1=Label(f2,text="Username\t:",bg="#EBD4B2").place(x=10,y=100)
    l2=Label(f2,text="Password\t:",bg="#EBD4B2").place(x=10,y=200)
    e5=Entry(f2);e6=Entry(f2,show='*')
    e5.place(x=300,y=100) ;e6.place(x=300,y=200)
    check1=Button(f2,text="Show",command=show,bg="#EBD4B2",fg="#142B4D",width=10,height=1,activebackground="#EBD4B2",activeforeground="#EBD4B2",font=('danfo',10,'bold')).place(x=50,y=275)
    check2=Button(f2,text="Hide",command=hide,bg="#EBD4B2",fg="#142B4D",width=10,activebackground="#EBD4B2",activeforeground="#EBD4B2",font=('danfo',10,'bold')).place(x=150,y=275)
    b1=Button(f2,text='Login',bg="#EBD4B2",fg="#142B4D",height=2,width=15,activebackground="#EBD4B2",activeforeground="#EBD4B2",font=('Britannic Bold',20,'bold'),command=verify).place(x=200,y=450)
    b2=Button(f2,text='BACK',bg="#EBD4B2",fg="#142B4D",height=2,width=15,activebackground="#EBD4B2",activeforeground="#EBD4B2",font=('Britannic Bold',20,'bold'),command=register).place(x=500,y=450)

def main_window():
    f3=Frame(root,bg="#EBD4B2",width=878,height=677).place(x=0,y=0)
    b1=Button(f3,text='CREATE',bg="#EBD4B2",fg="#142B4D",height=2,width=15,activebackground="#EBD4B2",activeforeground="#EBD4B2",font=('Britannic Bold',20,'bold'),command=create).place(x=200,y=250)
    b2=Button(f3,text='SEARCH',bg="#EBD4B2",fg="#142B4D",height=2,width=15,activebackground="#EBD4B2",activeforeground="#EBD4B2",command=search,font=('Britannic Bold',20,'bold')).place(x=200,y=350)
    b2=Button(f3,text='DELETE',bg="#EBD4B2",fg="#142B4D",height=2,width=15,activebackground="#EBD4B2",activeforeground="#EBD4B2",command=delete,font=('Britannic Bold',20,'bold')).place(x=200,y=450)

def create():
    global bg,bg1,e7,e8,e9,combobox1,combobox
    def insert():
        query="insert into books values({},'{}',{},'{}')". format(e10.get(),e7.get(),combobox1.get(),combobox.get())
        cur.execute(query)
        cur.execute("commit")
        messagebox.showinfo("Submited","Your entries have been submitted!!!")
        create()
    f4=Frame(root,width=878,height=677).place(x=0,y=0)
    bg=PhotoImage(file="create_bg.png")
    bg1=PhotoImage(file="images1.png")
    bg_label=Label(f4,image=bg)
    bg1_label=Label(f4,image=bg1)
    bg_label.place(x=0,y=0);bg1_label.place(x=400,y=80)
    options=["Select Mode Type","Classroom","Coaching","Tution","Online"]
    options2=["Select Class",'6','7','8','9','10','11','12']
    e7=Entry(f4);e8=Entry(f4);e10=Entry(f4)
    combobox = ttk.Combobox(f4,values=options,state='readonly')
    combobox1 = ttk.Combobox(f4,values=options2,state='readonly')
    combobox1.set("Select Class");combobox.set("Select Mode Type")
    e7.place(x=250,y=215);e10.place(x=250,y=110);combobox.place(x=250,y=425);combobox1.place(x=250,y=320)
    b1=Button(f4,text="Create",bg="#EBD4B2",fg="#142B4D",height=2,width=15,command=insert,font=('Britannic Bold',20,'bold')).place(x=200,y=500)
    b2=Button(f4,text="Home",bg="#EBD4B2",fg="#142B4D",height=2,width=15,command=main_window,font=('Britannic Bold',20,'bold')).place(x=500,y=500)

def search():
    f5=Frame(root,bg="#EBD4B2",width=878,height=677).place(x=0,y=0)
    l1=Label(f5,text="Search By\t:",bg="#EBD4B2",font=('Britannic Bold',30,'bold')).place(x=100,y=75)
    b1=Button(f5,text="ID",bg="#EBD4B2",fg="#142B4D",height=2,width=15,activebackground="#EBD4B2",activeforeground="#EBD4B2",font=('Britannic Bold',20,'bold'),command=id).place(x=100,y=175)
    b2=Button(f5,text="SUBJECT",bg="#EBD4B2",fg="#142B4D",height=2,width=15,activebackground="#EBD4B2",activeforeground="#EBD4B2",font=('Britannic Bold',20,'bold'),command=subject).place(x=100,y=275)
    b3=Button(f5,text="CLASS",bg="#EBD4B2",fg="#142B4D",height=2,width=15,activebackground="#EBD4B2",activeforeground="#EBD4B2",font=('Britannic Bold',20,'bold'),command=Class).place(x=100,y=375)
    b4=Button(f5,text="Home",bg="#EBD4B2",fg="#142B4D",height=2,width=15,command=main_window,font=('Britannic Bold',20,'bold')).place(x=100,y=475)
def id():
    global e11
    def search_id():
        query="select * from books where id={};". format(e11.get())
        r=Tk()
        r.title("Notebook details")
        r.geometry("600x300")
        cur.execute(query)
        tree=ttk.Treeview(r)
        tree["column"]=("ID","Subject","Class","Mode")
        tree["show"]='headings'
        s=ttk.Style(r)
        s.theme_use("winnative")
        s.configure("Treeview.Heading",font=('Britannic Bold',12,'bold'))
        hsb=ttk.Scrollbar(r,orient="vertical")
        hsb.configure(command=tree.xview)
        tree.configure(xscrollcommand=hsb.set)
        hsb.pack(fill=Y,side=RIGHT)
        tree.column("ID",width=50,minwidth=50,anchor=CENTER)
        tree.column("Subject",width=100,minwidth=50,anchor=CENTER)
        tree.column("Class",width=100,minwidth=50,anchor=CENTER)
        tree.column("Mode",width=150,minwidth=150,anchor=CENTER)
        tree.heading("ID",text="ID",anchor=CENTER)
        tree.heading("Subject",text="SUBJECT",anchor=CENTER)
        tree.heading("Class",text="CLASS",anchor=CENTER)
        tree.heading("Mode",text="MODE",anchor=CENTER)
        i=0
        for j in cur:
            tree.insert('',i,text="",values=(j[0],j[1],j[2],j[3]))
            i+=1
        tree.pack()
        r.mainloop()

    f6=Frame(root,bg="#EBD4B2",width=300,height=300).place(x=450,y=275)
    l1=Label(f6,bg="#EBD4B2",text="ID :",font=('Britannic Bold',20,'bold')).place(x=470,y=295)
    b1=Button(f6,text="SEARCH",bg="#EBD4B2",fg="#142B4D",height=1,width=15,activebackground="#EBD4B2",activeforeground="#EBD4B2",font=('Britannic Bold',15,'bold'),command=search_id).place(x=495,y=375)
    e11=Entry(f6)
    e11.place(x=500,y=335)

def subject():
    global e12
    def search_sub():
        query="select * from books where subject='{}';". format(e12.get())
        r=Tk()
        r.title("Notebook details")
        r.geometry("600x300")
        cur.execute(query)
        tree=ttk.Treeview(r)
        tree["column"]=("ID","Subject","Class","Mode")
        tree["show"]='headings'
        s=ttk.Style(r)
        s.theme_use("winnative")
        s.configure("Treeview.Heading",font=('Britannic Bold',12,'bold'))
        hsb=ttk.Scrollbar(r,orient="vertical")
        hsb.configure(command=tree.xview)
        tree.configure(xscrollcommand=hsb.set)
        hsb.pack(fill=Y,side=RIGHT)
        tree.column("ID",width=50,minwidth=50,anchor=CENTER)
        tree.column("Subject",width=100,minwidth=50,anchor=CENTER)
        tree.column("Class",width=100,minwidth=50,anchor=CENTER)
        tree.column("Mode",width=150,minwidth=150,anchor=CENTER)
        tree.heading("ID",text="ID",anchor=CENTER)
        tree.heading("Subject",text="SUBJECT",anchor=CENTER)
        tree.heading("Class",text="CLASS",anchor=CENTER)
        tree.heading("Mode",text="MODE",anchor=CENTER)
        i=0
        for j in cur:
            tree.insert('',i,text="",values=(j[0],j[1],j[2],j[3]))
            i+=1
        tree.pack()
        r.mainloop()
    f7=Frame(root,bg="#EBD4B2",width=300,height=300).place(x=450,y=275)
    l1=Label(f7,bg="#EBD4B2",text="SUBJECT :",font=('Britannic Bold',20,'bold')).place(x=470,y=295)
    b1=Button(f7,text="SEARCH",bg="#EBD4B2",fg="#142B4D",height=1,width=15,activebackground="#EBD4B2",activeforeground="#EBD4B2",font=('Britannic Bold',15,'bold'),command=search_sub).place(x=495,y=375)
    e12=Entry(f7,width=25)
    e12.place(x=500,y=335)

def Class():
    global e13
    def search_class():
        query="select * from books where class={};". format(e13.get())
        r=Tk()
        r.title("Notebook details")
        r.geometry("600x300")
        cur.execute(query)
        tree=ttk.Treeview(r)
        tree["column"]=("ID","Subject","Class","Mode")
        tree["show"]='headings'
        s=ttk.Style(r)
        s.theme_use("winnative")
        s.configure("Treeview.Heading",font=('Britannic Bold',12,'bold'))
        hsb=ttk.Scrollbar(r,orient="vertical")
        hsb.configure(command=tree.xview)
        tree.configure(xscrollcommand=hsb.set)
        hsb.pack(fill=Y,side=RIGHT)
        tree.column("ID",width=50,minwidth=50,anchor=CENTER)
        tree.column("Subject",width=100,minwidth=50,anchor=CENTER)
        tree.column("Class",width=100,minwidth=50,anchor=CENTER)
        tree.column("Mode",width=150,minwidth=150,anchor=CENTER)
        tree.heading("ID",text="ID",anchor=CENTER)
        tree.heading("Subject",text="SUBJECT",anchor=CENTER)
        tree.heading("Class",text="CLASS",anchor=CENTER)
        tree.heading("Mode",text="MODE",anchor=CENTER)
        i=0
        for j in cur:
            tree.insert('',i,text="",values=(j[0],j[1],j[2],j[3]))
            i+=1
        tree.pack()
        r.mainloop()
    f8=Frame(root,bg="#EBD4B2",width=300,height=300).place(x=450,y=275)
    l1=Label(f8,bg="#EBD4B2",text="CLASS :",font=('Britannic Bold',20,'bold')).place(x=470,y=295)
    b1=Button(f8,text="SEARCH",bg="#EBD4B2",fg="#142B4D",height=1,width=15,activebackground="#EBD4B2",activeforeground="#EBD4B2",font=('Britannic Bold',15,'bold'),command=search_class).place(x=495,y=375)
    e13=Entry(f8)
    e13.place(x=500,y=335)

def delete():
    global e14,combobox2
    def d():
        query="delete from books where id={} and subject='{}' and class={} and mode='{}';". format(e14.get(),e15.get(),combobox3.get(),combobox2.get())
        print(query)
##        cur.execute(query)
##        cur.execute("commit")
##        r=cur.fetchall()
##        print(r)
    f9=Frame(root,bg='#EBD4B2',width=878,height=677).place(x=0,y=0)
    l1=Label(f9,bg="#EBD4B2",text="ID\t:",font=('Britannic Bold',20,'bold')).place(x=50,y=100)
    l2=Label(f9,bg="#EBD4B2",text="SUBJECT\t:",font=('Britannic Bold',20,'bold')).place(x=50,y=200)
    l3=Label(f9,bg="#EBD4B2",text="CALSS\t:",font=('Britannic Bold',20,'bold')).place(x=50,y=300)
    l4=Label(f9,bg="#EBD4B2",text="MODE\t:",font=('Britannic Bold',20,'bold')).place(x=50,y=400)
    b1=Button(f9,text="DELETE",bg="#EBD4B2",fg="#142B4D",height=1,width=15,activebackground="#EBD4B2",activeforeground="#EBD4B2",font=('Britannic Bold',15,'bold'),command=d).place(x=495,y=375)
    e15=Entry(f9);e16=Entry(f9)
    options=["Select Mode Type","Classroom","Coaching","Tution","Online"]
    options2=["Select Class",'6','7','8','9','10','11','12']
    default_value = "Permanent Text"
    entry_var =StringVar(value=default_value)

    # Create the entry widget and set it to be disabled
    e14 = Entry(f9, textvariable=entry_var, state='readonly')
    combobox2= ttk.Combobox(f9,values=options,state='readonly')
    combobox3= ttk.Combobox(f9,values=options2,state='readonly')
    e14.place(x=225,y=110);e15.place(x=225,y=210);combobox3.place(x=225,y=310);combobox2.place(x=225,y=410)

##Main Programme
root=Tk()
bg = PhotoImage(file = "bg.png") 
root.title("Notebook")
root.geometry("878x677")
label1 = Label(root,image=bg) 
label1.place(x=0,y=0)
con=mysql.connect(host='localhost',
                  user='root',
                  password='tiger',
                  database='Notebook')
cur=con.cursor()
Label(root,text="Welcome To Notebook",bg="#E0CAAA").place(x=75,y=20)
b1=Button(root,text="REGISTER",bg="#EBD4B2",fg="#142B4D",height=2,width=15,command=register,font=('Britannic Bold',20,'bold'))
b2=Button(root,text="LOGIN",bg="#EBD4B2",fg="#142B4D",height=2,width=15,command=login,font=('Britannic Bold',20,'bold'))
b3=Button(root,text="Test",bg="#EBD4B2",fg="#142B4D",height=2,width=15,command=main_window,font=('Britannic Bold',20,'bold'))
b1.place(x=100,y=250);b2.place(x=525,y=250);b3.place(x=439,y=338)
