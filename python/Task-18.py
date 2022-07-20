import tkinter
import datetime
import pymysql

mycon= pymysql.connect(host="localhost", user="root", password="", database="my_db")
mycursor = mycon.cursor()


screen = tkinter.Tk()
screen.title("VACCINATION REPORT")
screen.geometry("500x500")
screen.configure(bg="navajo white")

firstname= tkinter.StringVar()
lastname = tkinter.StringVar()
email = tkinter.StringVar()
contact = tkinter.StringVar()
doze = tkinter.StringVar()
messagevar=tkinter.StringVar()

def vacc():
    query= "insert into student (firstname, lastname, email, contact, doze) values ('%s', '%s', '%s', '%s', '%s')"

    values= (firstname.get(), lastname.get(),email.get(),contact.get(),doze.get() )

    res=mycursor.execute(query%values)

    if res:
        messagevar.set("data inserted successfully !!")
        firstname.set("")
        lastname.set("")
        email.set("")
        contact.set("")
        doze.set("")

    else:
        messagevar.set("oops.. something went wrong !!")


    mycon.commit()