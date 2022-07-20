print("--------------------------------------------------------------------------------\n                              WELCOME TO KBC             \n--------------------------------------------------------------------------------")
print()


name = input("What is your name? --> ")
name = name.title()
print("""Hello {}, welcome to KBC! 
You will be presented with 10 questions.
Enter the appropriate option to answer the question
Good luck!""".format(name))



questions ={
"1. jerin's father has three sons- jerin 1, jerin 2. can you guess the name of the third son?:" : "C",

"2. you are 3rd place right now in race. what place are you in when you pass the person in 2nd place?:" : "C",

"3. the answer is really big." : "A",

"4. there is a room with no doors, and no windows.a man is found hung from the ceiling. a puddle of water is on the floor. how did he die?:" : "B",

"5. a man walks into a restaurant, the waiter says good day Admiral, why did the waiter call the man an admiral?" : "D",

"6. what can be seen once in a minute, twice in a moment, and never in a thousand years?" : "B",

"7. i am not alive, but i have five fingers, what i am?" : "A",

"8. A truck drove to the village and met 4 cars, how many vehicles were going to the village?" : "A",

"9. we kill and we give life, we are either poison or fruit, you choose what are we?" : "C",

"10. Which Shopkeeper takes your stuff and charges money for the same." : "A"
}

options = [["A.jerin 3", "B.jerin 5", "C.jerin", "D.none"],
          ["A.2nd" , "B.3rd", "C.1st", "D.none"],
          ["A.THE ANSWER", "B.really big", "C.an elephant", "D.the data given is insufficient"],
          ["A.he is mental", "B.he was standing on a block of ice", "C.he has a fever", "D.not idea"],
          ["A.none", "B.bymistakely", "C.it's his duty", "D.wearing uniform"],
          ["A. gems", "B.M", "C.Eucalyptus deglupta", "D. none of above"],
          ["A.gauntlet", "B.snake", "C.aye-aye", "D.sloth"],
          ["A.1", "B.2", "C.3", "D.4"],
          ["A.gloves", "B.joseph", "C.words", "D.sloth"],
          ["A.coiffeuse", "B.joseph", "C.jerin", "D.none of above"]]


def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("enter (A,B,C,D):-->  ")
        guess = guess.upper()
        guesses.append(guess)

        

        correct_guesses+=check_answer(questions.get(key),guess)
        question_num +=1

    display_score(correct_guesses,guesses)

# ------------------------------
def check_answer(answer, guess):

    if answer==guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0

# ------------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------------")
    print("RESULTS")
    print("-------------------------------")
   
    print("answers:", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("guesses:", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score =int ((correct_guesses/len(questions))*100)
    print("your score is:"+str(score)+"%")

# ------------------------------
def play_again():
    
    response= input("do you want to play again? (yes or no): ")
    response = response.upper()

    if response=="yes":
        return True
    else:
        return False
# ------------------------------


new_game()

while play_again():
    new_game()

print("Thank you for playing, goodbye!💜")