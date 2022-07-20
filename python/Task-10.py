import pymysql

my_con = pymysql.Connect(host= "local host", username="root", password= "",)
mycursor = my_con.cursor()

mycursor.execute("create database topsdb")
my_con.commit()

my_con = pymysql.Connect(host="local host", username="root", password="", database="topsdb")
mycursor = my_con.cursor()

mycursor.execute("create table student(id integer primary key auto_increment, fname varchar(20), subject varchar(20), city varchar(20)) ")
my_con.commit()

def getallData():
    query =" select * from student " 
    mycursor.execute(query)
    row  = mycursor.fetchall()

    print("length :", len(row))
    print("row :",row)

def getData():
    id = int(input("enter the id :"))
    query =" select * from student where id = (%s) " 
    values = (id)
    mycursor.execute(query%values)
    row  = mycursor.fetchone()

    print("firstname :", row[1])
    print(" subject :",row[2])