
import tkinter

screen = tkinter.Tk()
screen.title("My App")
screen.geometry("550x450")
screen.config(background="black")


#---------------------Start Logic--------------------

var_result = tkinter.StringVar()
var_box1 = tkinter.StringVar()
var_box2 = tkinter.StringVar()
var_box3 = tkinter.StringVar()
var_box4 = tkinter.StringVar()
var_box5 = tkinter.StringVar()

def submit():
    content = var_box1.get()
    var_result.set(content)
    var_box1.set(" ")

#-----------------------End Logic------------------------
my_hadder = tkinter.Label(screen,text="Registration Form",bg="black",fg="white",font=("arial",16,"bold"))

fisr_name = tkinter.Label(screen,text="First Name",bg="black",fg="white",font=("arial",10,"bold"))
last_name = tkinter.Label(screen,text="Last Name",bg="black",fg="white",font=("arial",10,"bold"))
email_add = tkinter.Label(screen,text="Email",bg="black",fg="white",font=("arial",10,"bold"))
phone_num = tkinter.Label(screen,text="Mobile",bg="black",fg="white",font=("arial",10,"bold"))
vc_status = tkinter.Label(screen,text="Vaccine",bg="black",fg="white",font=("arial",10,"bold"))

mybox1 = tkinter.Entry(screen,textvariable=var_box1,)
mybox1.insert(0," ")
mybox2 = tkinter.Entry(screen,textvariable=var_box2)
mybox2.insert(0," ")
mybox3 = tkinter.Entry(screen,textvariable=var_box3)
mybox3.insert(0," ")
mybox4 = tkinter.Entry(screen,textvariable=var_box4)
mybox4.insert(0," ")
mybox5 = tkinter.Entry(screen,textvariable=var_box5)
mybox5.insert(0," ")

btn1 = tkinter.Button(screen,text="Submit",bg="white",fg="black",height=1,width=6,font=("arial",16,"bold"),activebackground="green",activeforeground="white",bd=3,command=submit)
btn2 = tkinter.Button(screen,text="Update",bg="white",fg="black",height=1,width=6,font=("arial",16,"bold"),activebackground="green",activeforeground="white",bd=3,command=submit)
btn3 = tkinter.Button(screen,text="Search",bg="white",fg="black",height=1,width=6,font=("arial",16,"bold"),activebackground="green",activeforeground="white",bd=3,command=submit)
btn4 = tkinter.Button(screen,text="Delete",bg="white",fg="black",height=1,width=6,font=("arial",16,"bold"),activebackground="green",activeforeground="white",bd=3,command=submit)

my_hadder.place(x=180,y=0)

fisr_name.place(x=150,y=40)
last_name.place(x=150,y=80)
email_add.place(x=150,y=120)
phone_num.place(x=150,y=160)
vc_status.place(x=150,y=200)

mybox1.place(x=250,y=40)
mybox2.place(x=250,y=80)
mybox3.place(x=250,y=120)
mybox4.place(x=250,y=160)
mybox5.place(x=250,y=200)

btn1.place(x=100,y=280)
btn2.place(x=200,y=280)
btn3.place(x=300,y=280)
btn4.place(x=400,y=280)

screen.mainloop()
