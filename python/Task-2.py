import random

randomlist = random.sample(range(1,100),12)

print("list",randomlist)

print()
player1 = randomlist[:6]
random.shuffle(player1)
print("player1 :",player1)

player2 = randomlist[6:]
random.shuffle(player2)
print("player2 :",player2)

status=True
while status:
    input()
    random_gen = random.choice(randomlist)

    print("LUCKY NUMBER :",random_gen)
    if random_gen in player1:
        print("player1 is lucky!!!!!\n")
        randomlist.remove(random_gen)
        player1.remove(random_gen)
        print("player1 :",player1)
        print("player2 :",player2)

    else:
        print("player2 is lucky\n") 
        randomlist.remove(random_gen)
        player2.remove(random_gen)  
        print("player1 :",player1)
        print("player2 :",player2) 
   
      
    if (len(player1))==0:
        status=False
        print("player1 win the match")
    elif (len(player2))==0:
        status=False
        print("player2 win the match")
        
        

  
                             




    

        