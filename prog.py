from tkinter import*
from tkinter import messagebox as mb
import os,random,smtplib
from tkmacosx import Button
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
#change the location of the file here.
path="/Users/tharun/Downloads/Food_Ordering_System/"

def wdw(t):
    wd.title(t)
                                                           
def bck(q):
    q.pack_forget()
        
def login():
    f=open(path+"receipt.txt","w")
    f.write('')
    f.close()
    global o,s5
    s5=Frame(wd,width=1500,height=750,bg='light yellow')
    s5.pack(fill=BOTH)
    us=open(path+"users.txt",'r')
    l=us.readlines()
    user_names,user_pass,user_mail=[],[],[]
    for i in l:
        temp=i.split(',')
        user_names.append(temp[0])
        user_pass.append(temp[1])
        user_mail.append(temp[2])
    def click(m,n):
        if (m in user_names) and (n in user_pass):
            ele=user_names.index(m)
            global to_mailid,u_name
            u_name=user_names[ele]
            to_mailid=user_mail[ele]
            bck(s5)
            location()
            return True
        else:
            msg=mb.askquestion("INVALID CREDENTIALS","DO YOU WANT TO SIGN UP")
            if msg=="yes":
                bck(s5)
                signup()
            else:

                e.delete(0,END)
                f.delete(0,END)
                return False
    def clr():
            m=str(e.get())
            n=str(f.get())
            click(m,n)
    wdw("LOGIN")
    Label(s5,text="WELCOME",font=16,bg="orange",fg="black",height=3,width=160).place(x=0,y=0)        
    Label(s5,text="ENTER YOUR USERNAME:",font=16,bg="orange",fg="black",width=30,height=2).place(x=200,y=250)
    e=Entry(s5,font=("default",30),width=16,bg="light goldenrod",fg="black")
    e.place(x=700,y=250)
    e.focus()
    Label(s5,text="ENTER PASSWORD:",font=16,bg="orange",fg="black",width=30,height=2).place(x=200,y=350)
    f=Entry(s5,font=("arial",30),width=18,bg="light goldenrod",fg="black",show="*")
    f.place(x=700,y=350)
    b=Button(s5,text='SIGNUP',command=lambda:[bck(s5),signup()],width=250,font=16,bg="orange",fg="black",height=50,borderless=1)
    b.place(x=200,y=550)
    b1=Button(s5,text='LOGIN',command=clr,width=250,font=16,bg="orange",fg="black",height=50,borderless=1)
    b1.place(x=700,y=550)

def signup():
    global s,btn1
    s=Frame(wd,width=1500,height=750,bg='light yellow')
    s.pack(fill=BOTH)
    wdw("SIGN UP")
    def click(m,n,n1,o,p):
        if m.isalpha():
            if 8<=len(n)<=12:
                if n1==n:
                    if "a" and ".com" or ".edu" in o:
                        if p.isdigit() and len(p)==10:
                            r=""
                            r+=m+','+n+','+o+','+p+'\n'
                            u=open(path+"users.txt","a")
                            u.write(r)
                            u.close()
                            otps(o,1,m)
                            otp_verification(0)
                            return True
                        else:
                            mb.showinfo("WRONG ENTRY","ENTER A VALID PHONE NUMBER")
                            h.delete(0,END)
                            return False
                    else:
                        mb.showinfo("WRONG ENTRY","ENTER A VALID EMAIL")
                        g.delete(0,END)
                        return False
                else:
                    mb.showinfo("WRONG ENTRY","PASSWORDS DONT MATCH")
                    f1.delete(0,END)
                    return False
            else:
                mb.showinfo("WRONG ENTRY","ENTER A STRONGER PASSWORD(8-12 CHARACTERS)")
                f.delete(0,END)
                return False
        else:
            mb.showinfo("WRONG ENTRY","ENTER A VALID NAME")
            e.delete(0,END)
            return False
    def clr():
            m=str(e.get())
            n=str(f.get())
            n1=str(f1.get())
            o=str(g.get())
            p=str(h.get())
            click(m,n,n1,o,p)
    Button(s,text="<",command=lambda:[bck(s),login()],bg='orange',fg='black',width=80,font=16,height=40,borderless=1).place(anchor="nw")
    Label(s,text="ENTER YOUR DETAILS",width=160,font=16,bg="orange",fg="black",height=3).place(x=0,y=50)
    Label(s,text="ENTER YOUR NAME:",font=16,width=30,bg="orange",fg="black",height=2).place(x=100,y=150)
    e=Entry(s,width=25,bg="light goldenrod",fg="black",font=("default",30))
    e.place(x=700,y=150)
    e.focus()
    Label(s,text="ENTER YOUR PASSWORD:",width=30,font=16,bg="orange",fg="black",height=2).place(x=100,y=250)
    f=Entry(s,width=25,bg="light goldenrod",fg="black",show="*",font=("default",30))
    f.place(x=700,y=250)
    Label(s,text="RE ENTER YOUR PASSWORD:",width=30,font=16,bg="orange",fg="black",height=2).place(x=100,y=350)
    f1=Entry(s,width=25,bg="light goldenrod",fg="black",show="*",font=("default",30))
    f1.place(x=700,y=350)
    Label(s,text="ENTER YOUR EMAIL:",width=30,font=16,bg="orange",fg="black",height=2).place(x=100,y=450)
    g=Entry(s,width=25,bg="light goldenrod",fg="black",font=("default",30))
    g.place(x=700,y=450)
    Label(s,text="ENTER YOUR PHONE NO.:",width=30,font=16,bg="orange",fg="black",height=2).place(x=100,y=550)
    h=Entry(s,width=25,bg="light goldenrod",fg="black",font=("default",30))
    h.place(x=700,y=550)
    btn1=Button(s,text='SIGN UP',command=clr,width=250,font=16,bg="orange",fg="black",height=50,borderless=1)
    btn1.place(x=900,y=650)

def lc(mn,n):
    if mn==1:
        global a
        a=str(n)
    elif mn==2:
        global b
        b=str(n)

def location():
    global s1,a
    s1=Frame(wd,width=1500,height=750,bg='light yellow')
    s1.pack(fill=BOTH)
    wdw("LOCATION")
    f=open("location.txt","r")
    l=f.readlines()
    x=int(len(l))
    Button(s1,text="<",command=lambda:[bck(s1),login()],bg='orange',fg='black',height=40,width=80,borderless=1).pack(anchor="nw")
    for i in range(x):
        q=Button(s1,text=l[i].upper(),command=lambda n=i+1:[lc(1,n),bck(s1),hotel()],bg='orange',fg='black',font=16,height=50,borderless=1)
        q.pack(pady=10,fill=X)
        q.focus()

def hotel():
    global s2
    s2=Frame(wd,width=1500,height=750,bg='light yellow')
    s2.pack(fill=BOTH)
    wdw("HOTELS")
    f=open(path+a+"/0.txt","r")
    l=f.readlines()
    x=int(len(l))
    Button(s2,text="<",command=lambda:[bck(s2),location()],bg='orange',fg='black',height=40,width=80,borderless=1).pack(anchor="nw")
    for i in range(x):
        q=Button(s2,text=l[i].upper(),command=lambda n=i+1:[lc(2,n),bck(s2),menu()],bg='orange',fg='black',font=16,height=50,borderless=1)
        q.pack(pady=10,fill=X)
        q.focus()

def menu():
    global l,d,s3
    d=[]
    f=open(path+a+"/"+b+".txt","r")
    l=f.readlines()
    s3=Frame(wd,width=1500,height=750,bg='light yellow')
    s3.pack(fill=BOTH)
    wdw("MENU")
    Button(s3,text="<",command=lambda:[bck(s3),hotel()],bg='orange',fg='black',height=40,width=80,borderless=1).grid(sticky='nw')
    Label(s3,text="PRICE IN Rs.",bg="orange",fg="black",width=15,font=16,height=2).place(x=400,y=0)
    for i in range(len(l)):
        lbl=Label(s3,text=l[i].split(':')[0].upper(),bg='orange',fg='black',width=50,font=16,height=3,anchor='w')
        lbl.grid(row=i+1,column=0,sticky="w")
        lbl=Label(s3,text=l[i].split(':')[1],bg='orange',fg='black',width=150,font=16,height=3,anchor='w')
        lbl.grid(row=i+1,column=1,sticky="w",pady=10)
        spb=Spinbox(s3,from_=0,to=50,font=16,bg='white',fg='navy blue',state="readonly",width=5)
        spb.grid(row=i+1,column=1)
        spb.focus()
        d.append(spb)
    Button(s3,text="ADD TO CART",command=lambda:[add(),bck(s3),cart()],bg='orange',fg='black',width=250,height=50,font=16,borderless=1).grid(row=len(l)+3,pady=100,column=1)

def add():
    global amt
    f=open(path+"receipt.txt","a")
    n=0
    for i in d:
        r=""
        q=int(i.get())
        if q>0:
            itm=l[n].split(":")[0][2::].strip()
            cost =int(l[n].split(":")[1])
            price=cost*q
            amt+=price
            if itm in list:
                mb.showinfo("ITEM NOT ORDERED",itm.upper()+" ALREADY PRESENT IN CART.")
            elif itm not in list:
                r+=itm+"\t\t\t:"+str(cost)+"\t\t\t:"+str(q)+"\t\t\t:"+str(price)+"\n"
                list.append(itm)
                f.write(r)
        n+=1
    f.close()
  
def cart():
    global s7,e,ch,amt
    s7=Frame(wd,width=1500,height=950,bg='light yellow')
    s7.pack(fill=BOTH)
    f=open("receipt.txt","r")
    ch=f.readlines()
    can = Canvas(s7,bg="light yellow",width=1350,height=950)
    can.pack(fill=BOTH,side=LEFT)
    sb=Scrollbar(s7,orient='vertical',command=can.yview,bg='orange',width=20)
    sb.pack(fill=Y,side=LEFT,expand=1,)
    can.configure(yscrollcommand=sb.set)
    can.bind('<Configure>',lambda e:can.configure(scrollregion=can.bbox("all")))
    s6=Frame(can,width=1350,height=950,bg='light yellow')
    s6.pack(fill=BOTH)
    can.create_window((0,0),window=s6,anchor="nw")
    wdw("CART")
    Button(s6,text="<",command=lambda:[bck(s7),menu()],bg='orange',fg='black',height=40,width=80,borderless=1).grid(sticky='nw')
    Label(s6,text="COST",bg="orange",fg="black",width=15,font=16,height=2).place(x=400,y=0)
    e=[];qty=[]
    for i in range(len(ch)):
        qty.append(IntVar(s6))
        arr=ch[i].split("\t\t\t:")
        itm=arr[0]
        q =arr[2]
        qty[i].set(q)
        pr=arr[3]
        qt=Label(s6,text=itm.upper(),bg='orange',fg='black',width=50,font=16,height=3,anchor='w')
        qt.grid(row=i+1,column=0,sticky="w")
        lbl1=Label(s6,text=pr,bg='orange',fg='black',width=150,font=16,height=3,anchor='w')
        lbl1.grid(row=i+1,column=1,sticky="w",pady=10)
        spb=Spinbox(s6,from_=0,to=50,width=5,bg='white',fg='navy blue',textvariable=qty[i],state="readonly",font=16)
        spb.grid(row=i+1,column=1)
        e.append(spb)
    Label(s6,text="AMOUNT\t\t:",bg='orange',fg='black',font=16,width=50,height=3,anchor='e').grid(row=len(ch)+1,column=0,sticky='ew')
    Label(s6,text=str(amt),bg='orange',fg='black',font=16,width=85,height=3,anchor='w').grid(row=len(ch)+1,column=1,sticky='ew')
    bt=Button(s6,text="GENERATE BILL",command=lambda:[CartChange(),bck(s7),bill()],bg='orange',fg='black',width=250,height=50,borderless=1,font=16)
    bt.grid(pady=100,row=len(ch)+2,column=1)
    bt.focus()

def CartChange():
    global amt
    f=open(path+"receipt.txt","w")
    n=0
    amt=0
    r=""
    ar=[]
    for i in e:
        q=int(i.get())
        if q>0:
            ar=ch[n].split("\t\t\t:")
            itm=ar[0].strip()
            cost =int(ar[1])
            price=cost*q
            amt+=price
            r+=(itm+"\t\t\t:"+str(q)+"\t\t\t:"+str(price)+"\n").upper()
        n+=1
    bg=" \t\t\t: \t\t\t: \n"
    f.write(bg+r)
    f.close()

def bill(m=0):
    global s4,ch
    s4=Frame(wd,width=1500,height=750,bg='light yellow')
    s4.pack(fill=BOTH)
    wdw("       BILL GENERATED")
    if m==0:
        payment()
        if amt==0:
            mb.showinfo("EMPTY ORDER","BILL IS NOT GENERATED AS NOTHING HAS BEEN ORDERED")
            exit()
    f=open("receipt.txt","r")
    l=f.readlines()
    txt="*"*30+"BILL GENERATED"+"*"*31
    Label(s4,text=txt,bg='orange',fg='black',font=16,height=2,width=60).grid(row=0,column=1)
    Label(s4,text="PRODUCT NAME",bg='navy blue',fg='red',font=16,height=2,width=50).grid(row=1,column=0)
    Label(s4,text="QUANTITY",bg='navy blue',fg='red',font=16,height=2,width=60).grid(row=1,column=1)
    Label(s4,text="PRICE",bg='navy blue',fg='red',font=16,height=2,width=60).grid(row=1,column=2)
    for i in range(1,len(l)-3):
        Label(s4,text=l[i].split(':')[0].strip(),bg='navy blue',fg='light yellow',font=16,height=2,width=50).grid(row=i+2,column=0)
        Label(s4,text=l[i].split(':')[1].strip(),bg='navy blue',fg='light yellow',font=16,height=2,width=60).grid(row=i+2,column=1)
        Label(s4,text=l[i].split(':')[2].strip(),bg='navy blue',fg='light yellow',font=16,height=2,width=60).grid(row=i+2,column=2)
    for i in range(3):
        Label(s4,text="*"*100,bg='navy blue',fg='light yellow',font=16,height=2,width=50).grid(row=len(l)+3,column=i,sticky='ew')
    Label(s4,bg='navy blue',fg='light yellow',font=16,height=2,width=50).grid(row=len(l)+4,column=0,sticky='ew')
    Label(s4,text=l[len(l)-1].split("\t\t")[0]+":",bg='navy blue',fg='light yellow',font=16,height=2,width=60,anchor='e').grid(row=len(l)+4,column=1,sticky='ew')
    Label(s4,text=l[len(l)-1].split("\t\t\t\t\t\t")[1],bg='navy blue',fg='light yellow',font=16,height=2,width=60).grid(row=len(l)+4,column=2,sticky='ew')
    bt=Button(s4,text="CHOOSE YOUR PAYMENT MODE",command=lambda:[bck(s4),mode()],bg='orange',fg='black',font=16,height=50,borderless=1,width=500)
    bt.grid(pady=100,row=len(l)+5,column=1)
    bt.focus()

def mode(): 
    global s5,b1,b2,b3,bu
    def dbl(x,y):
        x["state"]=DISABLED
        y["state"]=DISABLED
        bu.configure(command=lambda:[bck(s5),mode()])
    def but1():
        def click(m,n):
            if n.isdigit() and len(n)==16:
                if m.isdigit() and m==n[-3::]: 
                    mb.showinfo("ORDERED","YOUR FOOD WILL BE DELIVERED IN 30 MINUTES")
                    bck(s5)
                    wd.destroy()
                    otps(to_mailid,3)
                    return True
                else:
                    mb.showinfo("WRONG ENTRY","WRONG CVV")
                    f.delete(0,END)
                    return False
            else:
                mb.showinfo("WRONG ENTRY","ENTER A VALID NUMBER")
                e.delete(0,END)
                f.delete(0,END)
                return False
        def clr():
                m=str(f.get())
                n=str(e.get())
                click(m,n)            
        Label(s5,text="ENTER YOUR CARD NUMBER:",font=16,bg="orange",fg="black",height=2,width=30).place(x=200,y=350)
        e=Entry(s5,width=25,bg="light goldenrod",fg="black",font=("default",30))
        e.place(x=700,y=350)
        e.focus()
        Label(s5,text="ENTER YOUR CVV:",font=16,bg="orange",fg="black",height=2,width=30).place(x=200,y=450)
        f=Entry(s5,width=25,bg="light goldenrod",fg="black",show="*",font=("default",30))
        f.place(x=700,y=450)
        b=Button(s5,text='OK',command=clr,width=250,font=16,bg="orange",fg="black",height=40,borderless=1)
        b.place(x=700,y=550)
    def but2():
        def click(n):
            if n.isdigit() and len(n)==10:
                otps(to_mailid,2)
                otp_verification(1)
                otps(to_mailid,3)
                return True
            else:
                mb.showinfo("WRONG ENTRY","ENTER A VALID PHONE NUMBER")
                e.delete(0,END)
                return False
        def clr():
            n=str(e.get())
            click(n)
        Label(s5,text="ENTER YOUR PHONE NUMBER:",font=16,bg="orange",fg="black",height=2,width=30).place(x=200,y=350)
        e=Entry(s5,width=25,bg="light goldenrod",fg="black",font=("default",30))
        e.place(x=600,y=350)
        e.focus()
        btn2=Button(s5,text='OK',command=clr,width=250,font=16,bg="orange",fg="black",height=40,borderless=1)
        btn2.place(x=600,y=550)
    def but3():
        mb.showinfo("ORDERED","YOUR FOOD WILL BE DELIVERED IN 30 MINUTES")
        wd.destroy()
        otps(to_mailid,3)
    s5=Frame(wd,width=1500,height=750,bg='light yellow')
    s5.pack(fill=BOTH)
    wdw('PAYMENT MODE')
    bu=Button(s5,text="<",command=lambda:[bck(s5),bill(1)],bg='orange',fg='black',width=80,font=16,height=40,borderless=1)
    bu.place(anchor="nw")
    bu.focus()
    b1=Button(s5,text="CARD",bg='orange',fg='black',font=16,height=50,borderless=1,width=1350)
    b1.place(x=20,y=100)
    b2=Button(s5,text="UPI",bg='orange',fg='black',font=16,height=50,borderless=1,width=1350)
    b2.place(x=20,y=150)
    b3=Button(s5,text="CASH ON DELIVERY",bg='orange',fg='black',font=16,height=50,borderless=1,width=1350)
    b3.place(x=20,y=200)
    b1.configure(command=lambda:[dbl(b2,b3),but1()])
    b2.configure(command=lambda:[dbl(b1,b3),but2()])
    b3.configure(command=lambda:[dbl(b1,b2),but3()])
             
def payment():
    f=open("/Users/tharun/Downloads/project/receipt.txt","a")
    a="\n"+"*"*76+"\n\tBILL AMOUNT"+"\t\t\t\t\t\t"+str(amt)+"\n"
    f.write(a)
    f.close()

def exit():
    tk=Tk()
    tk.geometry("1x1+700+450")
    mb.showinfo('EXIT','THANK YOU')
    os._exit(0) 

def otp_verification(x):
    s_otp=Tk()
    s_otp.geometry('300x200+550+300')
    s_otp.title("VERIFICATION")
    s_otp.config(bg="light yellow")
    Label(s_otp,text="ENTER THE OTP SENT TO YOUR E-MAIL",bg="orange",fg="black",height=2).pack(fill=X)
    Label(s_otp,bg='light yellow').pack()
    u_otp=Entry(s_otp,font=16,width=25,bg="light goldenrod",fg="black")
    u_otp.focus()
    u_otp.pack()
    def check():
        while True:
            if u_otp.get() == otp:
                s_otp.destroy()
                if x==1:
                     mb.showinfo("ORDERED","YOUR FOOD WILL BE DELIVERED IN 30 MINUTES")
                     wd.destroy()
                elif x==0:
                     mb.showinfo("","USER REGISTERED SUCCESSFULLY")
                     bck(s)
                     login()
                break
            else:
                mb.showinfo('INCORRECT OTP')
                s_otp.destroy()
    Label(s_otp,bg='light yellow').pack()
    Button(s_otp, text='Submit', command=check,bg="orange",font=16,fg="black",height=40).pack(anchor='s')
    s_otp.mainloop()

def otps(m,x,un=None):
    global otp
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    frm="scrumptiousservices.official@gmail.com"
    s.login(frm,'sqma eedm lwzi ufwc')
    msg=MIMEMultipart()
    msg['from']=frm
    msg['to']=m
    otp=str(random.randint(1000,9999))
    if x==1:
        msg['subject']='OTP FOR EMAIL VERIFICATION'
        bdy="HI "+un+"\nVERIFY YOUR EMAIL BY ENTERING THE FOLLOWING OTP.\n"+otp
    elif x==2:
        msg['subject']='OTP TO COMPLETE PAYMENT'
        bdy="HI "+u_name+"\nENTER THE FOLLOWING OTP TO COMPLETE THE PAYMENT.\n"+otp
    elif x==3:
        msg['subject']='BILL FOR YOUR ORDER'
        bdy="HI "+u_name+"\nTHANK YOU FOR YOUR ORDER.\nYOUR BILL IS ATTACHED BELOW."
        f_name='receipt.txt'
        with open('receipt.txt','r') as file:
            data=file.read().split("\n")
            data=data[0:len(data)-4]
        data=[i.split('\t\t\t:') for i in data]
        df=pd.DataFrame(data,columns=["PRODUCT NAME","          QUANTITY","             PRICE IN RS."])
        df=df.to_string(index = False)
        file=open("receipt.txt",'w')
        file.write(df)
        file.close()
        payment()
        attachment=open(r'receipt.txt','rb')
        p=MIMEBase('application','octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', 'attachment; filename= {}'.format(f_name))
        msg.attach(p)
    msg.attach(MIMEText(bdy,'plain'))
    msg=msg.as_string()
    s.sendmail(frm,m,msg)
    s.quit()
#=================================================================================================================
amt=0;list=[]
wd=Tk()
wd.geometry("1400x750+10+10")
wd.config(bg='light yellow')   
login()
wd.mainloop()
exit()