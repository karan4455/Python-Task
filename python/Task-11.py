import tkinter, pymysql


my_con = pymysql.connect(host="localhost",user="root",password="",database="student")
mydb = my_con.cursor()


var_search = tkinter.StringVar()
searchname_var = tkinter.StringVar()
    

def searchData():
    global var_search,searchname_var
    query = "select * from vaccine where (id=%s)"
    print("---> data ",var_search.get())
    args = (var_search.get())
    mydb.execute(query%args)
    result = mydb.fetchone()
    searchname_var.set(result[2])
    print(result[1])

def SearchScreen():
    global var_search,searchname_var
    display = tkinter.Tk()
    display.title("SEARCH")
    display.geometry("500x500")
    display.configure(bg="powder blue")

    
    label_2 = tkinter.Label(display,text="ENTER ID" ,bg="#CCCCCC",fg="black", font=("arial",10,"bold"),bd=2)
    label_2.place(x=60,y=70)
    
    label_2 = tkinter.Label(display,textvariable=searchname_var,bg="#CCCCCC",fg="black", font=("arial",10,"bold"),bd=2)
    label_2.place(x=60,y=150)

    entry_2 = tkinter.Entry(display, textvariable=var_search,width=40, insertwidth=2)
    entry_2.place(x=200,y=70)

    btn_search = tkinter.Button(display, text="SEARCH", bg="#4a7abc", fg="white", height=2, width= 25,  font=("arial",12,"bold"),activebackground="#4a7abc",activeforeground="white",command=searchData)
    btn_search.place(x=100,y=250)


def deleteData():
    display = tkinter.Tk()
    display.title("DELETE")
    display.geometry("500x500")
    display.configure(bg="powder blue")

    var_delete = tkinter.StringVar()

    label_2 = tkinter.Label(display,text="ENTER ID" ,bg="#CCCCCC",fg="black", font=("arial",10,"bold"),bd=2)
    label_2.place(x=60,y=70)

    entry_2 = tkinter.Entry(display, textvariable=var_delete,width=40, insertwidth=2)
    entry_2.place(x=200,y=70)

    btn_delete = tkinter.Button(display, text="DELETE", bg="#4a7abc", fg="white", height=2, width= 25,  font=("arial",12,"bold"),activebackground="#4a7abc",activeforeground="white",)
    btn_delete.place(x=100,y=250)




def updateData():
    display = tkinter.Tk()
    display.title("UPDATE")
    display.geometry("500x500")
    display.configure(bg="powder blue")

    var_update = tkinter.StringVar()

    label_2 = tkinter.Label(display,text="ENTER ID" ,bg="#CCCCCC",fg="black", font=("arial",10,"bold"),bd=2)
    label_2.place(x=60,y=70)

    entry_2 = tkinter.Entry(display, textvariable=var_update,width=40, insertwidth=2)
    entry_2.place(x=200,y=70)

    btn_update = tkinter.Button(display, text="UPDATE", bg="#4a7abc", fg="white", height=2, width= 25,  font=("arial",12,"bold"),activebackground="#4a7abc",activeforeground="white", )
    btn_update.place(x=100,y=250)
