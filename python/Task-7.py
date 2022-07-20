print("--------------------------------------------------------------------------------\n                              WELCOME TO KBC             \n--------------------------------------------------------------------------------")
print()


name = input("What is your name? --> ")
name = name.title()
print("""Hello {}, welcome to KBC! 
You will be presented with 10 questions.
Enter the appropriate option to answer the question
Good luck!""".format(name))


quiz={
        1:{
            "que":"1. jerin's father has three sons- jerin 1, jerin 2. can you guess the name of the third son?",
            "opt":"A.jerin 3    B.jerin     C.jerin 5       D.none",
            "ans":"B"
        },
        2:{
            "que":"2. you are 3rd place right now in race. what place are you in when you pass the person in 2nd place?",
            "opt":"A.3      B.1       C.2      D.no idea",
            "ans":"B"
        },
        3:{
            "que":"3. the answer is really big.",
            "opt":"A.THE ANSWER     B.really big       C.an elephant       D.the data given is insufficient",
            "ans":"A"
        },
         4:{
            "que":"4. there is a room with no doors, and no windows.a man is found hung from the ceiling. a puddle of water is on the floor. how did he die?",
            "opt":"A.he is mental       B.he was standing on a block of ice     C.he has a fever        D.not idea",
            "ans":"B"
        },
         5:{
            "que":"5. a man walks into a restaurant, the waiter says good day Admiral, why did the waiter call the man an admiral?",
            "opt":"A.none       B.bymistakely     C.it's his duty     D.wearing uniform",
            "ans":"D"
        },
         6:{
            "que":"6. what can be seen once in a minute, twice in a moment, and never in a thousand years?",
            "opt":"A. gems      B.M      C.Eucalyptus deglupta      D. none of above",
            "ans":"B"
        },
         7:{
            "que":"7. i am not alive, but i have five fingers, what i am?",
            "opt":"A.gauntlet       B.snake     C.aye-aye       D.sloth",
            "ans":"A"
        },
         8:{
            "que":"8. A truck drove to the village and met 4 cars, how many vehicles were going to the village?",
            "opt":"A.1     B.2     C.3       D.4",
            "ans":"A"
        },
         9:{
            "que":"9. we kill and we give life, we are either poison or fruit, you choose what are we?",
            "opt":"A.gloves    B.joseph     C.words     D.sloth",
            "ans":"C"
        },
         10:{
            "que":"10. Which Shopkeeper takes your stuff and charges money for the same.",
            "opt":"A.coiffeuse     B.joseph        C.jerin       D.none of above",
            "ans":"A"
        }
    }
fifty_fifty={
        1:{
            "que":"1. jerin's father has three sons- jerin 1, jerin 2. can you guess the name of the third son?",
            "opt":"A.jerin 3    B.jerin",
            "ans":"B"
        },
        2:{
            "que":"2. you are 3rd place right now in race. what place are you in when you pass the person in 2nd place?",
            "opt":"B.1       C.2",
            "ans":"B"
        },
        3:{
            "que":"3. the answer is really big.",
            "opt":"A.THE ANSWER     B.really big",
            "ans":"A"
        },
         4:{
            "que":"4. there is a room with no doors, and no windows.a man is found hung from the ceiling. a puddle of water is on the floor. how did he die?",
            "opt":"A.he is mental       B.he was standing on a block of ice",
            "ans":"B"
        },
         5:{
            "que":"5. a man walks into a restaurant, the waiter says good day Admiral, why did the waiter call the man an admiral?",
            "opt":"C.it's his duty     D.wearing uniform",
            "ans":"D"
        },
         6:{
            "que":"6. what can be seen once in a minute, twice in a moment, and never in a thousand years?",
            "opt":"B.M      C.Eucalyptus deglupta",
            "ans":"B"
        },
         7:{
            "que":"7. i am not alive, but i have five fingers, what i am?",
            "opt":"A.gauntlet       C.aye-aye",
            "ans":"A"
        },
         8:{
            "que":"8. A truck drove to the village and met 4 cars, how many vehicles were going to the village?",
            "opt":"A.1     C.3",
            "ans":"A"
        },
         9:{
            "que":"9. we kill and we give life, we are either poison or fruit, you choose what are we?",
            "opt":"C.words     D.sloth",
            "ans":"C"
        },
         10:{
            "que":"10. Which Shopkeeper takes your stuff and charges money for the same.",
            "opt":"A.coiffeuse     B.joseph",
            "ans":"A"
        }
    }
audiance_poll={
        1:{
            "que":"1. jerin's father has three sons- jerin 1, jerin 2. can you guess the name of the third son?",
            "ans":"most voted option: B",
        },
        2:{
            "que":"2. you are 3rd place right now in race. what place are you in when you pass the person in 2nd place?",
            "ans":"most voted option: B",
        },
        3:{
            "que":"3. the answer is really big.",
            "ans":"most voted option: A",
        },
         4:{
            "que":"4. there is a room with no doors, and no windows.a man is found hung from the ceiling. a puddle of water is on the floor. how did he die?",
            "ans":"most voted option: B",
        },
         5:{
            "que":"5. a man walks into a restaurant, the waiter says good day Admiral, why did the waiter call the man an admiral?",
            "ans":"most voted option: D",
        },
         6:{
            "que":"6. what can be seen once in a minute, twice in a moment, and never in a thousand years?",
            "ans":"most voted option: B",
        },
         7:{
            "que":"7. i am not alive, but i have five fingers, what i am?",
            "ans":"most voted option: A",
        },
         8:{
            "que":"8. A truck drove to the village and met 4 cars, how many vehicles were going to the village?",
            "ans":"most voted option: A",
        },
         9:{
            "que":"9. we kill and we give life, we are either poison or fruit, you choose what are we?",
            "ans":"most voted option: C",
        },
         10:{
            "que":"10. Which Shopkeeper takes your stuff and charges money for the same.",
            "ans":"most voted option: A"
        }
    }
points=0 
choice=0
fifty=1
audiance=1
for i in quiz:
        print("------------------------------------------------------------\n")
        print(quiz[i]["que"])
        print(quiz[i]["opt"])
        print()

        if fifty==1:
            choice=int(input("do you want to take fifty_fifty lifeline? if yes then press 1 otherwise press 0:"))
            if choice==1:
                fifty=0
                print(fifty_fifty[i]["que"])
                print(fifty_fifty[i]["opt"])
            else:
                fifty=1
                if audiance==1:
                    choice=int(input("\ndo you want to take audiance lifeline? if yes then press 2 ohterwise press 0:"))
                    if choice==2:
                        audiance=0
                        print(audiance_poll[i]["que"])
                        print(audiance_poll[i]["ans"])
                    else:
                        audiance=1
                    
        elif audiance==1:
            choice=int(input("do you want to take audiance lifeline? if yes then press 2 otherwise press 0:"))
            if choice==2:
                        audiance=0
                        print(audiance_poll[i]["que"])
                        print(audiance_poll[i]["ans"])
            else:
                        audiance=1
        else:
            pass

        

        ans = input("\nEnter your ans :--> ")
        print()
        if ans == quiz[i]["ans"]:
            points=points+5
            print("RIGHT ANSWER!!!")
            print("your total points is:",points)
        else:
            points=points-2
            print("ohh! WRONG ANSWER..the right answer is below")
            print(quiz[i]["ans"])
            print("your total points is:",points)


print("""THANK YOU {} FOR PLAYING!
      !!!!!!  GOODBYE   !!!!!""".format(name))
        










