import email
from tkinter import *
from tkinter import messagebox
import pickle
import sys
from turtle import back
from tkcalendar import Calendar
global root
root = Tk()
class prodect:
    def __init__(self):
        self.pname = StringVar()
        self.des = StringVar()
        self.sou =StringVar()
        self.pid = IntVar()
        self.uid = IntVar()
        self.cur=StringVar()
    #==========================
    def add(self):
        if(pe1.get()=="" or pe2.get()=="" or pe3.get()=="" or pe4.get()==""):
            messagebox.showerror("Invalid", "Enter all feilds its mandetry!")
            pad.destroy()
        else:
            self.pname=pe1.get()
            self.pid=pe2.get()
            self.des=pe3.get()
            self.sou=pe4.get()
            self.uid=x.UID
            self.cur=pe4.get()
            book = open('cmsproduct.pickel', 'ab')
            pickle.dump(tm,book)
            book.close()
            messagebox.showinfo("Added_CMS","Your Product is added successfully and now been tracked!")
            pad.destroy() 
    #--------------------------
    def track(self):
        if(te1.get()=="" or te2.get()==""):
            messagebox.showerror("Invalid", "Enter all feilds its mandetry!")
            tar.destroy()
        else:
            global t
            t = prodect()
            book = open('cmsproduct.pickel', 'rb')
            while True:
                try:
                    t = pickle.load(book)
                    if (t.uid ==te2.get()  and t.pid == te1.get()):
                        messagebox.showinfo("Found","Product Tracked! \n"+t.pname+"\n"+t.pid
                        +"\n"+"From: "+t.sou+"\n"+"To: "+t.des+"\n"+"Reached: "+t.cur)
                        tar.destroy()
                        break
                except EOFError:
                    messagebox.showerror("Invalid", "Product not found!")
                    break
            book.close()
#-----------------------------------------.

class member:
    def __init__(self):
        self.Name = StringVar()
        self.UID = IntVar
        self.Mobile = IntVar
        self.email = None
        self.pin = IntVar
        self.gender = None
    #======================
    def login(self):
        user = le1.get()
        pas = le2.get()
        if (user == "" or pas == ""):
            messagebox.showerror("Invalid", "Enter UID and PIN Properly!")
            log.destroy()
        else:
            global x
            x = member()
            book = open('cmsdata.dat', 'rb')
            while True:
                try:
                    x = pickle.load(book)
                    if (x.UID == user and x.pin == pas):
                        lm = x
                        log.destroy()
                        home()
                        break
                except EOFError:
                    messagebox.showerror("Invalid", "Ooo! Invalid UID OR PIN!")
                    break
            book.close()
    #=========================
    def register(self):
        name = re1.get()
        uid = re2.get()
        mobile = re3.get()
        email = re4.get()
        type = var.get()
        if (name == "" or uid == "" or mobile == "" or email == "" or type==""):
            messagebox.showerror("Invalid", "*Please Enter all the Details")
            reg.destroy()
        else:
            protectf()
    #==========================
    def pro(self):
        pin = pe1.get()
        cpin = pe2.get()
        if(pin =="" or cpin==""):
            messagebox.showerror("Invalid", "*Please Enter PIN and Confirm Pin Both")
            protect.destroy()
            protectf()
        else:
            if(pin!=cpin):
                messagebox.showerror("Not Match", "Pin and Confirm Pin Don't Matched Try again")
                protect.destroy()
                protectf()
            if(pin==cpin):
                if(messagebox.showinfo("Validation","Your PIN saved succefully plesae do not forget it, will required for furture access to your account")):
                    self.Name = re1.get()
                    self.UID = re2.get()
                    self.Mobile = re3.get()
                    self.email = re4.get()
                    self.gender = var.get()
                    self.pin = pe1.get()

                    book = open('cmsdata.dat', 'ab')
                    pickle.dump(rm,book)
                    book.close()
                    messagebox.showinfo("Registered_CMS","Congratulations !! You are Registered Succefully")
                    reg.destroy()             
#=========================================

def protectf():
    global protect
    protect = Toplevel(reg)
    protect.title("Protect_C.M.S.")
    protect.geometry("300x300")
    protect.resizable(False, False)
    protect.config(background="light green")
    head1 = Label(protect, bg="black", fg="white",
                  text="C.M.S. Protect", font=("Calibri", 25), width="300")
    head1.pack()
    ph1 = Label(protect, pady=20, text="Create Your 4 Digit Strong Pin\nyou security matters a lot!",
                bg="light green", fg="black", font=("Impact", 12))
    ph1.pack()
    global pe1
    global pe2
    ph2 = Label(protect, text="New PIN : ", bg="light green",
                fg="black", font=("Latin", 12, "bold"))
    ph2.place(x=30, y=150)
    pe1 = Entry(protect, width="10", font=("Latin", 12, "bold"))
    pe1.place(x=150, y=150)

    ph3 = Label(protect, text="Confirm PIN : ", bg="light green",
                fg="black", font=("Latin", 12, "bold"))
    ph3.place(x=30, y=200)
    pe2 = Entry(protect, width="10", font=("Latin", 12, "bold"))
    pe2.place(x=150, y=200)
    
    submit = Button(protect, command=rm.pro, text="Submit", bg="black",
                    fg="white", font=("Calibri"), width="10").pack(side=BOTTOM)

#------------------------------------------

def register():
    global reg
    reg = Toplevel(root)
    reg.title("C.M.S_Register")
    reg.geometry("800x500")
    reg.resizable(False, False)
    reg.config(background="light green")
    head1 = Label(reg, bg="black", fg="white",
                  text="C.M.S. Registration", font=("Calibri", 35), width="400")
    head1.pack()
    lspace = Label(reg, bg="light green")
    lspace.pack()
    rh1 = Label(reg, text="We welcome you to become a part of LPU's CMS\nBack bone of Courier Services",
                bg="light green", fg="black", font=("Elephant", 12))
    rh1.pack()
    rh2 = Label(reg, text="-----Please Enter Following Details-----",
                bg="light green", fg="black", font=("Calibri", 11), pady=20)
    rh2.pack()

    rh3 = Label(reg, text="Name : ", bg="light green",
                fg="black", font=("Latin", 12, "bold"))
    rh3.place(x=50, y=200)
    global re1
    re1 = Entry(reg, font=("Latin", 12, "bold"))
    re1.place(x=120, y=200)

    global re2
    rh4 = Label(reg, text="U.I.D. : ", bg="light green",
                fg="black", font=("Latin", 12, "bold"))
    rh4.place(x=50, y=300)
    re2 = Entry(reg, font=("Latin", 12, "bold"))
    re2.place(x=120, y=300)

    global re3
    rh3 = Label(reg, text="Mobile No. : ", bg="light green",
                fg="black", font=("Latin", 12, "bold"))
    rh3.place(x=400, y=200)
    re3 = Entry(reg, font=("Latin", 12, "bold"))
    re3.place(x=520, y=200)

    global re4
    rh3 = Label(reg, text="Email ID : ", bg="light green",
                fg="black", font=("Latin", 12, "bold"))
    rh3.place(x=400, y=300)
    re4 = Entry(reg, font=("Latin", 12, "bold"))
    re4.place(x=520, y=300)

    rh4 = Label(reg, text="Gender : ", bg="light green",
                fg="black", font=("Latin", 12, "bold"))
    rh4.place(x=230, y=350)
    global var
    var = IntVar()
    r1 = Radiobutton(reg, text='Male', variable=var, value=1, background="light green", font=(
        "Latin", 12, "bold")).place(x=330, y=350)
    r1 = Radiobutton(reg, text='Female', variable=var, value=2,
                     background="light green", font=("Latin", 12, "bold")).place(x=430, y=350)
    global rm
    rm = member()
    submit = Button(reg, command=rm.register, text="Submit", bg="black",
                    fg="white", font=("Calibri"), width="10").pack(side=BOTTOM)

#--------------------------------

def login():
    global log
    log = Toplevel(root)
    log.title("C.M.S_Login")
    log.geometry("400x400")
    log.resizable(False, False)
    log.config(background="pink")
    head1 = Label(log, bg="black", fg="white", text="C.M.S. Login",
                  font=("Calibri", 35), width="400").pack()
    lspace = Label(log, bg="pink")
    lspace.pack()
    lh1 = Label(log, text="-----Enter the Folowing Details-----",
                bg="pink", fg="black", pady=20, font=("Calibri", 20)).pack()
    lspace.pack()
    lh2 = Label(log, text="UID", bg="pink", fg="black",
                pady=10, font=("Calibri", 20)).pack()
    global le1
    global le2
    le1 = Entry(log, font=('calibre', 15))
    le1.pack()
    lspace.pack()
    lh3 = Label(log, text="PIN ", bg="pink", fg="black",
                pady=10, font=("Calibri", 20)).pack()
    le2 = Entry(log, show='*', font=('calibre', 15))
    le2.pack()
    lspace.pack()
    global lm
    lm = member()
    submit = Button(log, command=lm.login, text="Submit", bg="black",
                    fg="white", font=("Calibri"), width="10").pack(side=BOTTOM)
#---------------------------
def add():
    global pad
    pad = Toplevel(hom)
    pad.title("C.M.S_Add Parcel")
    pad.geometry("800x500")
    pad.resizable(False, False)
    pad.config(background="light green")
    head1 = Label(pad, bg="black", fg="white",
                  text="Add Parcel", font=("Calibri", 35), width="400")
    head1.pack()
    lspace = Label(pad, bg="light green")
    lspace.pack()
    rh2 = Label(pad, text="Please Enter Following Details of your Product",
                bg="light green", fg="black", font=("Calibri", 20), pady=20)
    rh2.pack()

    rh3 = Label(pad, text="Product Name : ", bg="light green",
                fg="black", font=("Latin", 12, "bold"))
    rh3.place(x=15, y=200)
    global pe1
    pe1 = Entry(pad, font=("Latin", 12, "bold"))
    pe1.place(x=160, y=200)

    global pe2
    rh4 = Label(pad, text="Product ID : ", bg="light green",
                fg="black", font=("Latin", 12, "bold"))
    rh4.place(x=15, y=250)
    pe2 = Entry(pad, font=("Latin", 12, "bold"))
    pe2.place(x=160, y=250)

    global pe3
    rh3 = Label(pad, text="Destination Add. : ", bg="light green",
                fg="black", font=("Latin", 12, "bold"))
    rh3.place(x=15, y=300)
    pe3 = Entry(pad, font=("Latin", 12, "bold"))
    pe3.place(x=160, y=300)

    global pe4
    rh3 = Label(pad, text="Source Add. : ", bg="light green",
                fg="black", font=("Latin", 12, "bold"))
    rh3.place(x=15, y=350)
    pe4 = Entry(pad, font=("Latin", 12, "bold"))
    pe4.place(x=160, y=350)
     
    global dat
    dat = Label(pad, text="Select Date", bg="light green",
                fg="black", font=("Latin", 12, "bold"))
    dat.place(x=575, y=180)
    
    global cal
    cal = Calendar(pad, selectmode = 'day',
               year = 2020, month = 11,
               day = 4)
    cal.place(x=500,y=200)
    global tm
    tm = prodect()
    submit = Button(pad, text="Submit",command=tm.add, bg="black",
                    fg="white", font=("Calibri"), width="10").pack(side=BOTTOM)
#----------------------------
def track():
    global tar
    tar = Toplevel(hom)
    tar.title("C.M.S_Track")
    tar.geometry("400x400")
    tar.resizable(False, False)
    tar.config(background="pink")
    head1 = Label(tar, bg="black", fg="white", text="C.M.S. Track",
                  font=("Calibri", 35), width="400").pack()
    lspace = Label(tar, bg="pink")
    lspace.pack()
    lh1 = Label(tar, text="-----Enter the Folowing Details-----",
                bg="pink", fg="black", pady=20, font=("Calibri", 20)).pack()
    lspace.pack()
    lh2 = Label(tar, text="Product ID", bg="pink", fg="black",
                pady=10, font=("Calibri", 20)).pack()
    global te1
    global te2
    te1 = Entry(tar, font=('calibre', 15))
    te1.pack()
    lspace.pack()
    lh3 = Label(tar, text="UID: ", bg="pink", fg="black",
                pady=10, font=("Calibri", 20)).pack()
    te2 = Entry(tar, font=('calibre', 15))
    te2.pack()
    lspace.pack()
    global tam
    tam = prodect()
    submit = Button(tar, text="Submit", bg="black",command=tam.track,
                    fg="white", font=("Calibri"), width="10").pack(side=BOTTOM)
#----------------------------

def home():
    global hom
    root.destroy()
    hom = Tk()
    hom.title("Home_C.M.S.")
    hom.geometry("800x500")
    hom.resizable(False,False)
    hom.config(background="light blue")
    space = Label(hom, bg="light blue")
    C = Canvas(hom,bg="black",height=2,width=800)
    head = Label(hom, text="Courier Management System",
             bg="black", fg="white", font=("Calibri", 35), width="800").pack()
    C.pack()
    space.pack()
    h1 = Label(hom,text="Welcome Back! "+x.Name, bg="light blue",
           fg="black", pady=20, font=("Calibri", 30)).pack()
    h2 = Label(hom,relief=RAISED,text="U.I.D.: "+x.UID, bg="red",
           fg="black", font=("Calibri", 15)).place(x="5",y="75")
    space.pack()
    rh1 = Label(hom, text="LPU's CMS\nBack bone of Courier Services",
                bg="light green", fg="black", font=("Elephant", 12))
    rh1.pack()
    space.pack()
    h3 = Label(hom, text="Track your Packet\nRight now!", pady=25,
           bg="light blue", fg="red", font=("Impact", 20)).pack()
    space.pack()
    logb = Button(hom,text="Track", command=track,bg="green", fg="white", font=(
            "Calibri", 13), width="10", height="1").place(x="200", y="375")
    """upb = Button(hom,text="Update Loc", command=update,bg="green", fg="white", font=(
            "Calibri", 13), width="10", height="1").place(x="350", y="375")"""
    regb = Button(hom,text="Add Parcel", command=add,bg="blue", fg="white", font=(
            "Calibri", 13), width="10", height="1").place(x="500", y="375")
    out =Button(hom,text="Logout and Exit",command=exit, bg="red", fg="white", font=(
            "Calibri", 13), width="15", height="1").pack(side=BOTTOM)
    hom.mainloop()

#----------------------------
root.title("C.M.S")
root.geometry("800x500")
root.resizable(False, False)
root.config(background="light blue")
head = Label(root, text="Courier Management System",
             bg="black", fg="white", font=("Calibri", 35), width="800")
space = Label(root, bg="light blue")
head.pack()
space.pack()
h1 = Label(root, text="-----WELCOME-----", bg="light blue",
           fg="black", pady=20, font=("Calibri", 30)).pack()
space.pack()
h2 = Label(root, text="Track your Packet\nRight now!", pady=25,
           bg="light blue", fg="yellow", font=("Impact", 25)).pack()
space.pack()
logb = Button(root,command=login,  text="Login", bg="black", fg="white", font=(
    "Calibri", 13), width="10", height="1").place(x="285", y="375")
regb = Button(root, command=register,text="New User", bg="black", fg="white", font=(
    "Calibri", 13), width="10", height="1").place(x="425", y="375")
space.pack()
h3 = Label(root, text="*Press LOGIN if already have an CMS Account\notherwise if you are new to CMS than press NEW USER", bg="light blue").pack()
space.pack()
e = Label(root,text="©pro.krishpatel-hiyajain-yaswanthkumar").pack(side=BOTTOM)
root.mainloop()

