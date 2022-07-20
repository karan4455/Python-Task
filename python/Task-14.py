from vaccine import*
label_1 = tkinter.Label(screen,text="FIRST NAME" ,bg="navajo white",fg="midnight blue", font=("arial",10,"bold"),bd=2)
label_1.place(x=10,y=20)

label_2 = tkinter.Label(screen,text="LAST NAME" ,bg="navajo white",fg="midnight blue", font=("arial",10,"bold"),bd=2)
label_2.place(x=10,y=60)

label_3 = tkinter.Label(screen,text="EMAIL" ,bg="navajo white",fg="midnight blue", font=("arial",10,"bold"),bd=2)
label_3.place(x=10,y=100)

label_4 = tkinter.Label(screen,text="CONTACT NUMBER" ,bg="navajo white",fg="midnight blue", font=("arial",10,"bold"),bd=2)
label_4.place(x=10,y=140)

label_5 = tkinter.Label(screen,text="VACCINATION DOZE" ,bg="navajo white",fg="midnight blue", font=("arial",10,"bold"),bd=2)
label_5.place(x=10,y=180)

entry_1 = tkinter.Entry(screen, textvariable=firstname,width=40, insertwidth=2)
entry_1.place(x=200,y=20)

entry_2 = tkinter.Entry(screen, textvariable=lastname,width=40, insertwidth=2)
entry_2.place(x=200,y=60)

entry_3 = tkinter.Entry(screen, textvariable=email, width=40, insertwidth=2)
entry_3.place(x=200,y=100)

entry_4 = tkinter.Entry(screen, textvariable=contact, width=40, insertwidth=2,justify="left")
entry_4.place(x=200,y=140)

entry_5 = tkinter.Entry(screen, textvariable=doze, width=40, insertwidth=2)
entry_5.place(x=200,y=180)

btn = tkinter.Button(screen, text="SUBMIT DATA", bg="midnight blue", fg="navajo white", height=2, width= 25,  font=("arial",12,"bold"),activebackground="royal blue",activeforeground="white",command=vacc)
btn.place(x=100,y=250)

msg= tkinter.Button(screen, textvariable=messagevar, bg="midnight blue", fg="navajo white", height=2, width= 25,  font=("arial",12,"bold"),activebackground="royal blue",activeforeground="white",)
msg.place(x=100,y=300)

screen.mainloop()