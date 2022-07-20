import tkinter, pymysql

screen = tkinter.Tk()
screen.title("VACCINATION REPORT")
screen.geometry("500x500")
screen.configure(bg="powder blue")

my_con = pymysql.connect(host="localhost",user="root",password="")
mycursor = my_con.cursor()
mycursor.execute("create database IF NOT EXISTS  student")
my_con.commit()


my_con = pymysql.connect(host="localhost",user="root",password="",database="student")
mycursor = my_con.cursor()
mycursor.execute("create table IF NOT EXISTS vaccine  (id integer primary key auto_increment,firstname varchar(30), lastname varchar(30), email varchar(30), contact varchar(15), vaccination varchar(10) )")
my_con.commit()

var_first= tkinter.StringVar()
var_last = tkinter.StringVar()
var_email = tkinter.StringVar()
var_contact = tkinter.StringVar()
var_doze = tkinter.StringVar()
var_submit = tkinter.StringVar()

def insert_data():
    fname= var_first.get()
    lname = var_last.get()
    email = var_email.get()
    contact = var_contact.get()
    doze = var_doze.get()

    query = "insert into vaccine(firstname,lastname,email,contact,vaccination) values ('%s', '%s' ,'%s' ,' %s', '%s')"
    values = (fname,lname,email,contact,doze)
    res = mycursor.execute(query%values)
    if res:
        var_submit.set("sucessfully submitted")
        var_first.set("")
        var_last.set("")
        var_email.set("")
        var_contact.set("")
        var_doze.set("")
        
    my_con.commit()



    