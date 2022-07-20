print("--------------------------------------------------\n             WELCOME TO IPL 2022             \n--------------------------------------------------")
input()
ipl_teams=["CSK","MI","RCB","GT","KKR","DC","SRH","LSG","PBKS","RR"]
t1=input("select your team:").upper()
ipl_teams.remove(t1)
import random
t2=random.choice(ipl_teams)
print("random team name is:",t2)
toss=["H","T"]
tchoice=input("enter your choice for toss:")
rchoice=random.choice(toss)
print("final toss:",rchoice)
if tchoice==rchoice:
    print(t1,"won the toss and chosse batting first")
else:
    print(t2,"won the toss and choose batting first")
run_list=[0,1,2,3,4,6,"out"]
if tchoice==rchoice:
    print(t1,"your score is here")
    box=0
    BALL=0
    for i in range(1,7):
        input()
        run=random.choice(run_list)
        BALL=BALL+1
        print("BALL",BALL,":",run)
        if run=="out":
            break
        else:
            box=box+run
    print("your final score is:=",box)
    print(t2,"needs",box+1,"run to win the match")

    print(t2,"your score is here")
    box1=0
    BALL=0
    for i in range(1,7):
        input()
        run=random.choice(run_list)
        BALL=BALL+1
        print("BALL",BALL,":",run)
        if run=="out":
            break
        else:
            box1=box1+run
    print("your final score is:=",box1)


else:

    print(t2,"your score is here")
    box1=0
    BALL=0
    for i in range(1,7):
        input()
        run=random.choice(run_list)
        BALL=BALL+1
        print("BALL",BALL,":",run)
        if run=="out":
            break
        else:
            box1=box1+run
    print("your final score is:=",box1)
    print(t1,"needs",box1+1,"run to win the match")


    print(t1,"your score is here")
    box=0
    BALL=0
    for i in range(1,7):
        input()
        run=random.choice(run_list)
        BALL=BALL+1
        print("BALL",BALL,":",run)
        if run=="out":
            break
        else:
            box=box+run
    print("your final score is:=",box)

if box>box1:
    print(t1,"WON THE MATCH!!!")
else:
    print(t2,"WON THE MATCH!!!")