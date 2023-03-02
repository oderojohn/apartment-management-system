from tkinter import*
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import os
from datetime import datetime
now = datetime.now()
date = now.strftime('%y')
root=Tk()  #create a tkinter window
root.geometry("1500x1000")   #set dimension of window
root.title('apartment Management System')
regf=Frame(root,background="white")
add=Frame(root,background="skyblue")
loginf=Frame(root,background="palegreen")
home=Frame(root,background="magenta")
div=Frame(root,background="light blue")
intro=Frame(root,background="skyblue")
visitor=Frame(root,background="skyblue")
gateman=Frame(root,background="magenta")
manager=Frame(root,background="skyblue")
history=Frame(root,background="skyblue")
pas_reset=Frame(root)
login=Frame(root)
login2=Frame(root)
login3=Frame(root)


add.place(x=0,y=0,width=15000,height=1000)
regf.place(x=0,y=0,width=1500,height=1000)
loginf.place(x=0,y=0,width=1500,height=1000)

home.place(x=0,y=0,width=15000,height=1000)
div.place(x=0,y=0,width=1500,height=1000)
intro.place(x=0,y=0,width=1500,height=1000)
visitor.place(x=0,y=0,width=1500,height=1000)
gateman.place(x=0,y=0,width=1500,height=1000)
manager.place(x=0,y=0,width=1500,height=1000)
login.place(x=450,y=80,width=600,height=400)
login2.place(x=450,y=80,width=600,height=400)
login3.place(x=450,y=80,width=600,height=600)
pas_reset.place(x=450,y=80,width=600,height=600)
history.place(x=0,y=0,width=1500,height=1000)

root.wm_iconbitmap()

def show(frame):
    frame.tkraise()
for frame in (regf,loginf,home,add,div,intro,manager,gateman):
    frame.place(x=0,y=0)
style = ttk.Style()

Estyle = ttk.Style()
Estyle.configure('TEntry', foreground = 'green')

#-----------------------------------------------------------------------
db = sqlite3.connect('projectSMS.db')
my=db.cursor()
#-----------------------------------------------------------------------

#

      
#-----------------------registration-----------------------------------------
Label(regf,text="",bg="white").pack()
adr=Label(regf,text="APARTMENT MANAGEMENT SYSTEM",bg="white",font=('Kristen ITC', 30, 'bold','italic','underline'),fg='blue')
adr.pack()
Label(regf,text="",bg="white").pack()
Label(regf,text="",bg="white").pack()
Label(regf,text="",bg="white").pack()
Label(regf,text="",bg="white").pack()
Label(regf,text="login",bg="white",fg="blue").pack()
#---------------------------------------,fg=----------------------------------------------




#-----------------------login---------------------------------------------------------

#-------------------------------------------------------------------------------------

    
def exit():
    root.destroy()
Label(regf,text="",bg="white").pack()
F6=LabelFrame(regf,text="user login",font=("times new roman",10,),fg="white",bg="grey")
F6.place(x=500,y=100,width=500,height=500)

st=Button(regf,text="MANAGER",font=("times new roman",15,"bold"),width=25,height=2,bg="black",fg="white",command=lambda:show(login) )
st.pack()
Label(regf,text="",bg="grey").pack()
Label(regf,text="",bg="grey").pack()
st=Button(regf,text="CARETAKER",font=("times new roman",15,"bold"),width=25,height=2,bg="black",fg="white",command=lambda:show(login2),)
st.pack()
Label(regf,text="",bg="grey").pack()
Label(regf,text="",bg="grey").pack()
st=Button(regf,text="GATEMAN",font=("times new roman",15,"bold"),width=25,height=2,bg="black",fg="white",command=lambda:show(gateman) ,)
st.pack()
Label(regf,text="",bg="grey").pack()
Label(regf,text="",bg="grey").pack()
st=Button(regf,text="exit",width=10,bg="grey",fg="white",command=exit,)
st.pack()


#####_____function_______________###################################################
def backi():
    global style
    div_nma.delete(0,END)
    div_poia.delete(0,END)
    div_pera.delete(0,END)
    div_doba.delete(0,END)
    div_gena.delete(0,END)
    combo_pay.delete(0,END)
    combo1_pay.delete(0,END)
    show(home)
#################___Home____###############################################################
####____tree view______####
def log_out():
    show(loginf)
table_frame = Frame(home,bg='light blue')
table_frame.place(x=150,y=70,width=1200,height=390)

scroll_x = Scrollbar(table_frame,orient="horizontal")
scroll_y = Scrollbar(table_frame,orient="vertical")



tree=ttk.Treeview(table_frame,columns=('sno','name','id no.','room no','reg date','jan','feb','march','2','2','2','2','2','2','2',),
                  xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=tree.xview)
scroll_y.config(command=tree.yview)
tree.column('#0',width=150)
tree.column('#1',width=220)
tree.column('#2',width=130)
tree.column('#3',width=100)
tree.column('#4',width=160)
tree.column('#5',width=140)
tree.column('#6',width=150)
tree.column('#7',width=150)
tree.column('#8',width=150)
tree.column('#9',width=150)
tree.column('#10',width=150)
tree.column('#11',width=150)

tree.heading('#0',text='remaining rooms',)
tree.heading('#1',text='NAME')
tree.heading('#2',text='ID NUMBER.')
tree.heading('#3',text='ROOM NO')
tree.heading('#4',text='REG DATE')
tree.heading('#5',text='JANUARY')
tree.heading('#6',text='FEBRUARY')
tree.heading('#7',text='MARCH')
tree.heading('#8',text='pending')
tree.heading('#9',text='pending')
tree.heading('#10',text='pending')
tree.heading('#11',text='pending')


sno=50
tree.pack(fill=BOTH,expand=1)

frame = Frame(manager,bg='light blue')
frame.place(x=350,y=45,width=1000,height=415)

scroll_x = Scrollbar(frame,orient="horizontal")
scroll_y = Scrollbar(frame,orient="vertical")



tre=ttk.Treeview(frame,columns=('sno','name','id no.','room no','reg date','jan','feb','march','2','2','2','2','2','2','2',),
                  xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=tre.xview)
scroll_y.config(command=tre.yview)
tre.column('#0',width=150)
tre.column('#1',width=220)
tre.column('#2',width=130)
tre.column('#3',width=100)
tre.column('#4',width=160)
tre.column('#5',width=140)
tre.column('#6',width=150)
tre.column('#7',width=150)
tre.column('#8',width=150)
tre.column('#9',width=150)
tre.column('#10',width=150)
tre.column('#11',width=150)

tre.heading('#0',text='remaining rooms',)
tre.heading('#1',text='NAME')
tre.heading('#2',text='ID NUMBER.')
tre.heading('#3',text='ROOM NO')
tre.heading('#4',text='REG DATE')
tre.heading('#5',text='JANUARY')
tre.heading('#6',text='FEBRUARY')
tre.heading('#7',text='MARCH')
tre.heading('#8',text='pending')
tre.heading('#9',text='pending')
tre.heading('#10',text='pending')
tre.heading('#11',text='pending')


sno=50
tre.pack(fill=BOTH,expand=1)


def veiw():
    global sno
#    sn=my.execute("select* from student")

    my.execute("select* from apartment")
#    sn=list(range(1,len(sn)+1))
    for i in my:
        sno=sno-1
        tree.insert('',str(sno),'item '+str(sno),text=sno
                    ,values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        tre.insert('',str(sno),'item '+str(sno),text=sno
                    ,values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        
    sno=0

#tre.place(x=20,y=50)
veiw()
item='False'

def show_div():
    global item
    if 'item' in item: # item = 'item {any number}'
        show(div)
    else:
        messagebox.showerror("reminder","select a row to vey details")       #print('not called')
        
def delete():
    global m4
    named="'"+str(div_nm1.get())+"'"
    item=tree.focus()  #return item name whene clicked
    dictc=tree.item(item)
    if dictc['text']=='':  #cheak if name deleted
        messagebox.showerror("Error","no data to be deleted")
    else:
        tree.delete('item '+str(dictc['text']))
        my.execute("delete from apartment where name={}".format(named))
        db.commit()
        div_nma.delete(0,END)
        div_poia.delete(0,END)
        div_pera.delete(0,END)
        div_doba.delete(0,END)
        div_gena.delete(0,END)
        combo_pay.delete(0,END)
        combo1_pay.delete(0,END)
        m=Label(root, text="successfully removed from database",bg="red",font=('Kristen ITC', 15, 'bold'),fg='green')
        root.after(5, lambda:m.pack())
        root.after(4500, lambda:m.pack_forget())
        #messagebox.showerror("succes","data deleated succesifully!")
        
def search_data():
        #==================================for sqlite3==================
        conn=sqlite3.connect("projectSMS.db")
        cur=conn.cursor()
        cur.execute("select * from apartment where "+str(search_by.get())+" LIKE '%"+str(search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!=0:
            tree.delete(*tree.get_children())
            for row in rows:
                tree.insert("",END,values=row)
            conn.commit()
        else:
            messagebox.showerror("Error","Record doesn't find")
        conn.close()
def fetch_data():
        conn=sqlite3.connect("projectSMS.db")
        cur=conn.cursor()
        cur.execute("select * from apartment")
        rows = cur.fetchall()
        if len(rows)!=0:
            tree.delete(*tree.get_children())
            for row in rows:
                tree.insert("",END,values=row)
            conn.commit()
        conn.close()


T1=LabelFrame(home,bg="skyblue").place(x=5,y=45,width=130,height=415)

T3=LabelFrame(home,bg="skyblue")
T3.place(x=5,y=5,width=1350,height=30)
T4=LabelFrame(home,bg="skyblue")
T4.place(x=5,y=670,width=1350,height=15)
T5=LabelFrame(home,bg="skyblue")
T5.place(x=5,y=470,width=1350,height=190)
name=Label(T3,text="APARTMENT MANAGEMENT SOFTWARE",fg="white",bg="skyblue",font=('Kristen ITC', 15, 'bold'))
footer=Label(T4,text="Designed By Odero John Owino.",font=('Kristen ITC', 6, 'italic',"bold"),bg='skyblue')
footer.pack()
name.pack()
sth=ttk.Button(home,text="veiw data",style='C.TButton',command=show_div)
sth.place(x=20,y=70)
about=ttk.Button(home,text="log out",width=10,command=lambda:show(regf) ,style='C.TButton')  #show frame 'div' whene clicked
about.place(x=20,y=120)
logout=ttk.Button(home,text="paswords",style='C.TButton',command=lambda:show(login3))
logout.place(x=20,y=220)
hist=ttk.Button(home,text="history",style='C.TButton',command=lambda:show(history))
hist.place(x=20,y=270)
ddel=ttk.Button(home,text="delete",command=delete,width=10,style='C.TButton')
ddel.place(x=20,y=170)
searchbtn =ttk.Button(home,text="Search",width=7,style='C.TButton',command=search_data)
searchbtn.place(x=1190,y=37.5)
showbtn =ttk.Button(home,text="show all",width=7,style='C.TButton',command=fetch_data)
showbtn.place(x=1265,y=37.5)
lbl_search = Label(home,text="Search By",bg="light blue",fg="black",font=("times new roman",12,'bold'))
lbl_search.place(x=850,y=40)
search_by = StringVar()
search_txt = StringVar()
combo_search = ttk.Combobox(home,width=10,textvariable=search_by,font=("times new roman",10,'bold'),state='readonly')
combo_search['values']=("ID","NAME","ROOM")
combo_search.place(x=930,y=40)

txt_search = Entry(home,width=20,textvariable=search_txt,font=('times new roman',10,),fg="black",bd=2,bg="white",relief=GROOVE)
txt_search.place(x=1025,y=40)




###############__add__################################################################
def insert():
  global style,sno
  no=0
  gnl1=0
  gnl2=0
  gnl3=0
  name="'"+str(nm1.get())+"'"
  idno="'"+str(p1.get())+"'"
  room="'"+str(per1.get())+"'"
  regdate=date
  jan=gnl1
  feb=gnl2
  march=gnl3
  if name=="''" or idno=="''":
      messagebox.showerror("Error","NAME & ID must be provided befor you register")
  else:
      my.execute("insert into apartment values({},{},{},{},{},{},{})".format(name,idno,room,regdate,jan,feb,march))
      db.commit()
      my.execute('select* from apartment')
      nma.delete(0,END)
      poia.delete(0,END)
      pera.delete(0,END)
      doba.delete(0,END)
      combo_pay.delete(0,END)
      combo1_pay.delete(0,END)
  #    gena.delete(0,END)
      sno=50
      for i in my:
          sno=sno-1
          lst=i
      tree.insert('',str(sno),'item '+str(sno),text=sno,values=(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6]))
      tre.insert('',str(sno),'item '+str(sno),text=sno,values=(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6]))#insert into tree ,last row of table
      m4=Label(root, text="successfully added to database",font=('Kristen ITC', 15, 'bold'),fg='green')
      messagebox.showerror("success","data aded to database")
      root.after(100, lambda:m4.pack())
      root.after(1500, lambda:m4.pack_forget())
      

def insert2():
  userName="'"+str(userName4.get())+"'"
  pword="'"+str(pword4.get())+"'"
  if userName=="''" or pword=="''":
      messagebox.showerror("Error","userNAME & PASSWORD must be provided befor you update")
  else:
      my.execute("insert into user2 values({},{})".format(userName,pword,))
      db.commit()
      my.execute('select* from user2')
      textBox1.delete(0,END)
      textBox2.delete(0,END)
      messagebox.showerror("success","pasword updated succes")
def insert2():
  userName="'"+str(userName4.get())+"'"
  pword="'"+str(pword4.get())+"'"
  if userName=="''" or pword=="''":
      messagebox.showerror("Error","userNAME & PASSWORD must be provided befor you update")
  else:
      my.execute("insert into user2 values({},{})".format(userName,pword,))
      db.commit()
      my.execute('select* from user2')
      textBox1.delete(0,END)
      textBox2.delete(0,END)
      messagebox.showerror("success","pasword updated succes")

def insert3():
  global sno
  Name="'"+str(name_var.get())+"'"
  idn="'"+str(phone_var.get())+"'"
  phone="'"+str(email_var.get())+"'"
  mail="'"+str(id_var.get())+"'"
  if Name=="''" or idn=="''":
      messagebox.showerror("Error","NAME & ID must be provided")
  else:
      my.execute("insert into visitors values({},{},{},{})".format(Name,idn,phone,mail))
      db.commit()
      my.execute('select* from visitors')
      name_var.delete(0,END)
      phone_var.delete(0,END)
      email_var.delete(0,END)
      id_var.delete(0,END)
      
      for i in my:
          sno=sno+1
          lst=i
      t.insert('',str(sno),'item '+str(sno),text=sno,values=(lst[0],lst[1],lst[2],lst[3]))
      messagebox.showerror("success","ADDED")     


#in manager screen
frame1 = Frame(manager,bg='light blue')
frame1.place(x=10,y=5,width=1350,height=25)
def validate(u_input): # callback function
    return u_input.isdigit()
my_valid = manager.register(validate)
t=Label(frame1,text="odero owino john",bg="light blue",font = ('Kristen ITC', 15, 'bold'))
t.pack()

add_name1=Label(manager,text='NAME:',bg='skyblue',fg='#145862',font=('Kristen ITC', 15, 'bold'))
add_name1.place(x=10,y=45)
nm1=StringVar()
nma=ttk.Entry(manager,textvariable=nm1 ,font = ('Kristen ITC', 10, 'bold'))
nma.place(x=90,y=45)
admis1=Label(manager,text='ID NO:',fg='#145862',bg='skyblue',font = ('Kristen ITC', 15, 'bold'))
admis1.place(x=10,y=75)

p1=StringVar()
poia=ttk.Entry(manager,textvariable=p1 ,font = ('Kristen ITC', 10, 'bold'),validate='key',validatecommand=(my_valid,'%S'))
poia.place(x=90,y=75)

percent1=Label(manager,text='ROOM NO:',fg='#145862',bg='skyblue',font = ('Kristen ITC', 15, 'bold'))
percent1.place(x=10,y=105)
per1=StringVar()
pera=ttk.Entry(manager,textvariable=per1 ,font = ('Kristen ITC', 10, 'bold'),validate='key',validatecommand=(my_valid,'%S'))
pera.place(x=140,y=105)

dob_1=Label(manager,text='REG DATE:',fg='#145862',bg='sky blue',font = ('Kristen ITC', 15, 'bold'))
dob_1.place(x=10,y=130)

dob1=date
doba=ttk.Entry(manager,textvariable=dob1 ,font = ('Kristen ITC', 10, 'bold'))
doba.place(x=140,y=130)

'''gender1=Label(manager,text='JANUARY:',fg='#145862',bg='skyblue',font = ('Kristen ITC', 15, 'bold'))
gender1.place(x=10,y=165)
gen1=StringVar()
gena=ttk.Entry(manager,textvariable=gen1 ,font = ('Kristen ITC', 10, 'bold'))
gena.place(x=130,y=165)

'''

sub=ttk.Button(manager,text="add",command=insert,width=10,style='C.TButton')
sub.place(x=50,y=220)

back=ttk.Button(manager,text="back",width=10,style='C.TButton')
back.place(x=200,y=220)
#sth=ttk.Button(manager,text="veiw data",style='C.TButton',command=show_div)
#sth.place(x=80,y=400)
logout=ttk.Button(manager,text="log out",style='C.TButton',command=lambda:show(regf))
logout.place(x=50,y=260)

about=ttk.Button(manager,text="NULL",width=10,command=lambda:show(visitor)
                 ,style='C.TButton')  #show frame 'div' whene clicked
about.place(x=200,y=260)
###############__div__####################################################################
old_paw=''
def set_hifi(event):
    global old_paw,item
    item=tree.focus()  #return item name whene clicked
    dictc=tree.item(item)
    old_paw="'"+str(dictc['values'][1])+"'" #in dictc value[1] is password
    if div_nm1.get().isalnum():
        pass
    else:
        div_nma.insert(1,str(dictc['values'][0]))#value[0] is user name
        div_poia.insert(1,str(dictc['values'][1]))
        div_pera.insert(1,str(dictc['values'][2]))
        div_doba.insert(1,str(dictc['values'][3]))
        div_gena.insert(1,str(dictc['values'][4]))
        combo_pay.insert(1,str(dictc['values'][5]))
        combo1_pay.insert(1,str(dictc['values'][6]))
        
        
def set_hif(event):
    global old_paw,item
    item=tre.focus()  #return item name whene clicked
    dictc=tre.item(item)
    old_paw="'"+str(dictc['values'][1])+"'" #in dictc value[1] is password
    if div_nm1.get().isalnum():
        pass
    else:
        div_nma.insert(1,str(dictc['values'][0]))#value[0] is user name
        div_poia.insert(1,str(dictc['values'][1]))
        div_pera.insert(1,str(dictc['values'][2]))
        div_doba.insert(1,str(dictc['values'][3]))
        div_gena.insert(1,str(dictc['values'][4]))
        combo_pay.insert(1,str(dictc['values'][5]))
        combo1_pay.insert(1,str(dictc['values'][6]))


def hifiv(event):
    global tp,old_paw,style
    my.execute("select* from student ")

tree.bind('<<TreeviewSelect>>',set_hifi)
tre.bind('<<TreeviewSelect>>',set_hif)

 
    
def log():
    username = userName.get()
    Pass = password.get()
        	#Establish Connection
    with sqlite3.connect('projectSMS.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
    find_user = ('SELECT * FROM user WHERE username = ? and  pword = ?')
    c.execute(find_user,[(userName.get()),(password.get())])
    result = c.fetchall()
    if result:
        show(home)
        m4=Label(root, text=" managet successfully loged in",font=('Kristen ITC', 15, 'bold'),fg='red',bg="skyblue")
            
        root.after(100, lambda:m4.grid(row=3,column=5))
        root.after(1500, lambda:m4.grid_forget())
        man.delete(0,END)
        man2.delete(0,END)
            
                     
    else:
        messagebox.showerror('Oops!','Username Not Found.')
        m4=Label(root, text="pleace enter correct  login",font=('Kristen ITC', 15, 'bold'),fg='red',bg="skyblue")
            
        root.after(100, lambda:m4.grid(row=3,column=5))
        root.after(1500, lambda:m4.grid_forget())
def log3():
    username3= userName3.get()
    Pass3 = password3.get()
        	#Establish Connection
    with sqlite3.connect('projectSMS.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
    find_user = ('SELECT * FROM user WHERE username = ? and  pword = ?')
    c.execute(find_user,[(userName3.get()),(password3.get())])
    result = c.fetchall()
    if result:
        show(pas_reset)
        m4=Label(root, text=" VERIFIED",font=('Kristen ITC', 15, 'bold'),fg='red',bg="skyblue")
            
        root.after(100, lambda:m4.grid(row=3,column=5))
        root.after(1500, lambda:m4.grid_forget())
            
                     
    else:
        messagebox.showerror('Oops!','NOT AUTHORISED.')
        m4=Label(root, text="pleace enter correct  login",font=('Kristen ITC', 15, 'bold'),fg='red',bg="skyblue")
            
        root.after(100, lambda:m4.grid(row=3,column=5))
        root.after(1500, lambda:m4.grid_forget())
def log2():
    username = userName1.get()
    Pass = password1.get()
        	#Establish Connection
    with sqlite3.connect('projectSMS.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
    find_user = ('SELECT * FROM user2 WHERE username = ? and pword = ?')
    c.execute(find_user,[(userName.get()),(password.get())])
    result = c.fetchall()
    if result:
        show(manager)
                     
    else:
        messagebox.showerror('Oops!','Username Not Found.')
            

def update():
  global old_paw
  nm=str(div_nm1.get())
  pw=str(div_p1.get())
  pct=str(div_per1.get())
  dobt=str(div_dob1.get())
  gendert=str(div_gen1.get())
  fb=str(combo_pay.get())
  mar=str(combo1_pay.get())
  
  name1="'"+str(div_nm1.get())+"'"
  paw1="'"+str(div_p1.get())+"'"
  pc="'"+str(div_per1.get())+"'"
  dob="'"+str(div_dob1.get())+"'"
  gender="'"+str(div_gen1.get())+"'"
  feb="'"+str(combo_pay.get())+"'"
  march="'"+str(combo1_pay.get())+"'"
  
  my.execute("update apartment set name={},id={},room={},regdate={},january={},february={},march={} where id={}"
             .format(name1,paw1,pc,dob,gender,feb,march,old_paw))
  db.commit()
  m3=Label(root, text="successfully updated",font=('Kristen ITC', 15, 'bold'),bg="skyblue",fg='red')
  
  root.after(100, lambda:m3.pack())
  root.after(1500, lambda:m3.pack_forget())
  item=tree.focus()
  tree.item(item,values=(nm,pw,pct,dobt,gendert,fb,mar)) 
  tre.item(item,values=(nm,pw,pct,dobt,gendert,fb,mar))






######
def validate(u_input): # callback function
    return u_input.isdigit()
my_valid = div.register(validate)
F5= Frame(div,bg='skyblue')
F5.place(x=10,y=10,width=550,height=415)
div_sub=ttk.Button(F5,text="update",command=update,width=10,style='C.TButton')
div_sub.place(x=60,y=340)

div_del=ttk.Button(F5,text="delete",command=delete,width=10,style='C.TButton')
div_del.place(x=160,y=340)

back=ttk.Button(F5,text="back",width=10,command=backi,style='C.TButton')
back.place(x=260,y=340)

up_name=Label(F5,text='NAME:',bg='skyblue',fg='#145862',font=('Kristen ITC', 15, 'bold'))
up_name.place(x=10,y=10)
div_nm1=StringVar()
div_nma=ttk.Entry(F5,textvariable=div_nm1 ,font = ('Kristen ITC', 10, 'bold'))
div_nma.place(x=90,y=10)

admis2=Label(F5,text='ID NO:',fg='#145862',bg='skyblue',font = ('Kristen ITC', 15, 'bold'),)
admis2.place(x=10,y=40)

div_p1=StringVar()
div_poia=ttk.Entry(F5,textvariable=div_p1 ,font = ('Kristen ITC', 10, 'bold'),validate='key',validatecommand=(my_valid,'%S'))
div_poia.place(x=90,y=40)

percent2=Label(F5,text='ROOM NO:',fg='#145862',bg='skyblue',font = ('Kristen ITC', 15, 'bold'))
percent2.place(x=10,y=70)
div_per1=StringVar()
div_pera=ttk.Entry(F5,textvariable=div_per1 ,font = ('Kristen ITC', 10, 'bold'),validate='key',validatecommand=(my_valid,'%S'))
div_pera.place(x=135,y=70)

dob_2=Label(F5,text='REG DATE:',fg='#145862',bg='skyblue',font = ('Kristen ITC', 15, 'bold'))
dob_2.place(x=10,y=100)
div_dob1=StringVar()
div_doba=ttk.Entry(F5,textvariable=div_dob1 ,font = ('Kristen ITC', 10, 'bold'))
div_doba.place(x=135,y=100)

gender2=Label(F5,text='JANUARY:',fg='#145862',bg='skyblue',font = ('Kristen ITC', 15, 'bold'))
gender2.place(x=10,y=130)
div_gen1=StringVar()
div_gena=ttk.Entry(F5,textvariable=div_gen1 ,font = ('Kristen ITC', 10, 'bold'),validate='key',validatecommand=(my_valid,'%S'))
div_gena.place(x=130,y=130)
gender1=Label(F5,text='FEBRUARY:',fg='#145862',bg='skyblue',font = ('Kristen ITC', 15, 'bold'))
gender1.place(x=10,y=160)
feb=StringVar()
combo_pay=ttk.Entry(F5,textvariable=feb ,font = ('Kristen ITC', 10, 'bold'),validate='key',validatecommand=(my_valid,'%S'))
combo_pay.place(x=140,y=160)
gender1=Label(F5,text='MARCH:',fg='#145862',bg='skyblue',font = ('Kristen ITC', 15, 'bold'))
gender1.place(x=10,y=180)
march=StringVar()
combo1_pay=ttk.Entry(F5,textvariable=march ,font = ('Kristen ITC', 10, 'bold'),validate='key',validatecommand=(my_valid,'%S'))
combo1_pay.place(x=140,y=180)
######################################################################################################
#########_intro___________________________############################################################
bg_color='white'

team=Label(intro,text='VISITORS ',font = ('Kristen ITC', 25, 'bold','underline'),bg='skyblue',fg='#ff0303')
team.pack()



ttk.Button(intro,text="back",width=30,command=lambda:show(home),style='C.TButton').place(x=20,y=340)


t=Label(visitor,text='VISITORS ',font = ('Kristen ITC', 25, 'bold','underline'),bg='skyblue',fg='#ff0303')
team.pack()



ttk.Button(visitor,text="back",width=30,command=lambda:show(manager),style='C.TButton').place(x=20,y=340)




#gate man4
bcolor="black"
Ccolor="white"
bg_color="magenta"
name_var=StringVar()
phone_var=StringVar()
email_var=StringVar()
id_var=StringVar()
F1=Label(gateman,text="VISITORS DETAILS",font=("times new roman",30,"bold","underline"),fg="white",bg=bg_color,)
F1.place(x=10,y=0,width=1330,height=45) 
    
        #Label(F1,text="search for registered student").grid(row=0,column=0)
Button(F1,text="LOGOUT",bg="grey",command=lambda:show(regf)).grid(column=2,row=0)
        #adm=Entry(F1,width="20",).grid(column=1,row=0) 
F2=LabelFrame(gateman,text="visitors details ",font=("times new roman",15,"bold","underline"),fg="white",bg=bg_color,)
F2.place(x=10,y=50,width=500,height=500)
F3=LabelFrame(gateman,text="visitors",font=("times new roman",15,"bold"),fg="black",bg=Ccolor,)
F3.place(x=520,y=50,width=830,height=400)
Label(F2,text="NAME:",bg=bg_color,fg="white",font=("times new roman",12,"bold")).place(x=10,y=20)
Label(F2,text="ID NO:",bg=bg_color,fg="white",font=("times new roman",12,"bold")).place(x=10,y=60)
Label(F2,text="PHONE NO:",bg=bg_color,fg="white",font=("times new roman",12,"bold")).place(x=10,y=100)
Label(F2,text="DATE:",bg=bg_color,fg="white",font=("times new roman",12,"bold")).place(x=10,y=140)
name_var= Entry(F2,bg="white",fg="black",textvariable=name_var)
name_var.place(x=80,y=20,width=140)
def validate(u_input): # callback function
    return u_input.isdigit()
my_valid = gateman.register(validate) 
phone_var= Entry(F2,bg="white",fg="black",textvariable=phone_var,validate='key',validatecommand=(my_valid,'%S'))
phone_var.place(x=80,y=60,width=140)
email_var= Entry(F2,bg="white",fg="black",textvariable=email_var,validate='key',validatecommand=(my_valid,'%S'))
email_var.place(x=120,y=100,width=140)

id_var= Entry(F2,bg="white",fg="black")
id_var.place(x=140,y=140,width=140)
    #buttons
F5=LabelFrame(F2,font=("times new roman",15,"bold","underline"),fg="magenta",bg=bg_color,)
F5.place(x=5,y=300,width=485,height=75)
Button(F5,text="SAVE",bg="cadetblue",fg="white",pady=15,font="aerial",command=insert3).grid(row=0,column=0,padx=5,pady=5)
Button(F5,text="EXIT",bg="cadetblue",fg="white",pady=15,font="aerial",command=lambda:show(regf)).grid(row=0,column=3,padx=5,pady=5)
 
Gframe = Frame(gateman,bg='light blue')
Gframe.place(x=520,y=50,width=850,height=415)

scroll_x = Scrollbar(Gframe,orient="horizontal")
scroll_y = Scrollbar(Gframe,orient="vertical")



t=ttk.Treeview(Gframe,columns=('sno','name','id no.','PHONE no','email'),
                  xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=tre.xview)
scroll_y.config(command=tre.yview)
t.column('#0',width=50)
t.column('#1',width=220)
t.column('#2',width=130)
t.column('#3',width=150)
t.column('#4',width=150)

t.heading('#0',text='no',)
t.heading('#1',text='NAME')
t.heading('#2',text='ID NUMBER.')
t.heading('#3',text='PHONE NO')
t.heading('#4',text='DATE')



sno=0
t.pack(fill=BOTH,expand=1)
   
def veiw2():
    global sno
#    sn=my.execute("select* from student")

    my.execute("select* from visitors")
#    sn=list(range(1,len(sn)+1))
    for i in my:
        sno=sno+1
        t.insert('',str(sno),'item '+str(sno),text=sno
                    ,values=(i[0],i[1],i[2],i[3]))
       
        
    sno=0

#tre.place(x=20,y=50)
veiw2()
item='False'
    

############$$$$$$$$$$$$$$$$$$#login########################################
label1 = Label(login, text = "")
label1.pack()
label1 = Label(login, text = "")
label1.pack()
label1 = Label(login, text = "Manager  Login ", fg = "black", font = ("new times roman", 40, "bold"))
label1.pack()

label2 = Label(login, text = "User Name :", font = ("arial", 16, "bold"))
label2.place(x = 90, y = 130)

userName = StringVar()
man = Entry(login, textvar = userName, width = 20, font = ("arial", 16, "bold"))
man.place(x = 270, y = 130)

label3 = Label(login, text = "Password :", font = ("arial", 16, "bold"))
label3.place(x = 90, y = 200)

password = StringVar()
man2 = Entry(login, textvar = password,validate='key',font = ("arial", 16, "bold"), width = 20, show="*")
man2.place(x = 270, y = 200)

button1 = Button(login, text = "   Login   ", fg = "white", bg = "black", relief = "raised", font = ("arial", 16, "bold"), command = log)
button1.place(x = 300, y = 250)
button1 = Button(login, text = "   Exit   ", fg = "white", bg = "black", relief = "raised", font = ("arial", 10, "bold"), command=lambda:show(regf))
button1.place(x = 320, y = 300)

label1 = Label(login3, text = "MANAGER AUTHENTIFICATION ", fg = "black", font = ("new times roman", 35, "bold"))
label1.place(x = 100, y = 15)

label2 = Label(login3, text = "User Name :", font = ("arial", 16, "bold"))
label2.place(x = 110, y = 150)

userName3 = StringVar()
textBox1 = Entry(login3, textvar = userName3, width = 30, font = ("arial", 16, "bold"))
textBox1.place(x = 290, y = 150)

label3 = Label(login3, text = "Password :", font = ("arial", 16, "bold"))
label3.place(x = 116, y = 250)

password3 = StringVar()
textBox2 = Entry(login3, textvar = password3,validate='key',font = ("arial", 16, "bold"), width = 30, show="*")
textBox2.place(x = 290, y = 250)

button1 = Button(login3, text = "   Login   ", fg = "white", bg = "black", relief = "raised", font = ("arial", 16, "bold"), command = log3)
button1.place(x = 335, y = 320)
button1 = Button(login3, text = "   Exit   ", fg = "white", bg = "black", relief = "raised", font = ("arial", 10, "bold"), command=lambda:show(home))
button1.place(x = 355, y = 360)



#caretaker login

label1 = Label(login2, text = " Caretaker Login ", fg = "black", font = ("new times roman", 40, "bold"))
label1.pack()

label2 = Label(login2, text = "User Name :", font = ("arial", 16, "bold"))
label2.place(x = 90, y = 150)

userName1 = StringVar()
textBox1 = Entry(login2, textvar = userName, width = 20, font = ("arial", 16, "bold"))
textBox1.place(x = 270, y = 150)

label3 = Label(login2, text = "Password :", font = ("arial", 16, "bold"))
label3.place(x = 90, y = 200)

password1 = StringVar()
textBox2 = Entry(login2, textvar = password,validate='key',font = ("arial", 16, "bold"), width = 20, show="*")
textBox2.place(x = 270, y = 200)

button1 = Button(login2, text = "   Login   ", fg = "white", bg = "black", relief = "raised", font = ("arial", 16, "bold"), command = log2)
button1.place(x = 300, y = 250)
button1 = Button(login2, text = "   Exit   ", fg = "white", bg = "black", relief = "raised", font = ("arial", 10, "bold"), command=lambda:show(regf))
button1.place(x = 320, y = 300)

## pasword reset window

label1 = Label(pas_reset, text = " PASSWORD RESET ", fg = "black", font = ("new times roman", 30, "bold"))
label1.place(x = 150, y = 15)
label1 = Label(pas_reset, text = " caretaker ", fg = "white", font = ("new times roman", 20, "bold"))
label1.place(x = 50, y = 60)
label1 = Label(pas_reset, text = " gateman", fg = "white", font = ("new times roman", 20, "bold"))
label1.place(x = 500, y = 60) 
label2 = Label(pas_reset, text = " Enter New UserName :",fg = "white",font = ("arial", 16, "bold"))
label2.place(x =20, y = 110)

userName4 = StringVar()
textBox1 = Entry(pas_reset, textvar = userName4, width = 20, font = ("arial", 15, "bold"))
textBox1.place(x = 20, y = 150)

label3 = Label(pas_reset, text = " Enter New Password :",fg = "white", font = ("arial", 16, "bold"))
label3.place(x = 20, y = 190)

pword4 = StringVar()
textBox2 = Entry(pas_reset, textvar = pword4, width = 20, font = ("arial", 15, "bold"))
textBox2.place(x = 20, y = 230)


label2 = Label(pas_reset, text = " Enter New UserName :",fg = "white",font = ("arial", 16, "bold"))
label2.place(x =400, y = 110)

userName5 = StringVar()
textBox1 = Entry(pas_reset, textvar = userName5, width = 20, font = ("arial", 15, "bold"))
textBox1.place(x = 400, y = 150)

label3 = Label(pas_reset, text = " Enter New Password :",fg = "white", font = ("arial", 16, "bold"))
label3.place(x = 400, y = 190)

userName5 = StringVar()
textBox1 = Entry(pas_reset, textvar = userName5, width = 20, font = ("arial", 15, "bold"))
textBox1.place(x = 400, y = 230)

button1 = Button(pas_reset, text = "   Reset   ", fg = "white", bg = "black", relief = "raised", font = ("arial", 16, "bold"),command=insert2 )
button1.place(x = 30, y = 280)
button1 = Button(pas_reset, text = "   Reset   ", fg = "white", bg = "black", relief = "raised", font = ("arial", 16, "bold"))
button1.place(x = 430, y = 280)
button1 = Button(pas_reset, text = "   Exit   ", fg = "white", bg = "black", relief = "raised", font = ("arial", 10, "bold"), command=lambda:show(home))
button1.place(x = 355, y = 360)

show(regf)



###end by odero john###





root.mainloop()
