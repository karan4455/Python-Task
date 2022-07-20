from vaccform_logic_db import*
from second_form_db import * 

label_1 = tkinter.Label(screen,text="VACCINATION FORM" ,bg="#CCCCCC",fg="black", font=("arial",10,"bold"),bd=2)
label_1.place(x=200,y=5)

label_1 = tkinter.Label(screen,text="FIRST NAME" ,bg="#CCCCCC",fg="black", font=("arial",10,"bold"),bd=2)
label_1.place(x=10,y=30)

label_2 = tkinter.Label(screen,text="LAST NAME" ,bg="#CCCCCC",fg="black", font=("arial",10,"bold"),bd=2)
label_2.place(x=10,y=70)

label_3 = tkinter.Label(screen,text="EMAIL" ,bg="#CCCCCC",fg="black", font=("arial",10,"bold"),bd=2)
label_3.place(x=10,y=110)

label_4 = tkinter.Label(screen,text="CONTACT NUMBER" ,bg="#CCCCCC",fg="black", font=("arial",10,"bold"),bd=2)
label_4.place(x=10,y=150)

label_5 = tkinter.Label(screen,text="VACCINATION DOZE" ,bg="#CCCCCC",fg="black", font=("arial",10,"bold"),bd=2)
label_5.place(x=10,y=190)

entry_1 = tkinter.Entry(screen, textvariable=var_first,width=40, insertwidth=2)
entry_1.place(x=200,y=30)

entry_2 = tkinter.Entry(screen, textvariable=var_last,width=40, insertwidth=2)
entry_2.place(x=200,y=70)

entry_3 = tkinter.Entry(screen, textvariable=var_email, width=40, insertwidth=2)
entry_3.place(x=200,y=110)

entry_4 = tkinter.Entry(screen, textvariable=var_contact, width=40, insertwidth=2, justify="left")
entry_4.place(x=200,y=150)

entry_5 = tkinter.Entry(screen, textvariable=var_doze, width=40, insertwidth=2)
entry_5.place(x=200,y=190)

btn = tkinter.Button(screen, text="SUBMIT DATA", bg="#4a7abc", fg="white", height=2, width= 25,  font=("arial",12,"bold"),activebackground="#4a7abc",activeforeground="white",command=insert_data)
btn.place(x=100,y=250)

btn_1 = tkinter.Button(screen, text="SEARCH", bg="#4a7abc", fg="white", height=2, width= 10,  font=("arial",12,"bold"),activebackground="#4a7abc",activeforeground="white", command=SearchScreen)
btn_1.place(x=60,y=330)

btn_2 = tkinter.Button(screen, text="UPDATE", bg="#4a7abc", fg="white", height=2, width= 10,  font=("arial",12,"bold"),activebackground="#4a7abc",activeforeground="white", command=updateData)
btn_2.place(x=180,y=330)

btn_3 = tkinter.Button(screen, text="DELETE", bg="#4a7abc", fg="white", height=2, width= 10,  font=("arial",12,"bold"),activebackground="#4a7abc",activeforeground="white", command=deleteData)
btn_3.place(x=300,y=330)

mess_label = tkinter.Label(screen,textvariable=var_submit, bg="powder blue", fg="black", font=("arial",10,"bold"),bd=2, height=2, width= 25 )
mess_label.place(x=100,y=400)

screen.mainloop()