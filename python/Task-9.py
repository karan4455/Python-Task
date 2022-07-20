def order():
    class Pizzer():
        def inputData(self,pizza,pizzas,Pizza):
            self.pizza = pizza
            self.pizzas = pizzas
            self.Pizza = Pizza
        
        def price(self):
            print("large pizza = ",self.pizza)
            print("large pizzas = ",self.pizzas)
            print("Large Pizza = ",self.Pizza)

        def display(self):
            print("***Buy 4 or more pizza and get 1.5lt of soft drink free***\n")

    class Pasta():
        def inputData(self,pasta,pastas,Pasta):
            self.pasta = pasta
            self.pastas = pastas
            self.Pasta = Pasta

        def price(self):
            print("large pasta = ",self.pasta)
            print("large pastas = ",self.pastas)
            print("Large Pasta = ",self.Pasta)

        def display(self):
            print("***Buy 4 or more pastas and get 2 bruschetta free.***")
            print("***Buy 4 or more pizzas and pastas and get 2 chocco brownies ice cream free.")
            print("--------------------------------------------------------------")
    piz=Pizzer()
    piz.inputData("10.99 AUD", "19.99 AUD", "29.99 AUD")
    piz.price()
    piz.display()
    pas=Pasta()
    pas.inputData("9.5 AUD","17.00 AUD" ,"27.50 AUD")
    pas.price()
    pas.display()

    pizza_count = 0
    pasta_count = 0
    total_sum_count = 0
    number_pizza_quantity = 0
    number_pasta_quantity = 0
    
    while True:
        name=input("\nEnter your name: ")
        print("Welcome {}".format(name))
        pizza_quantity = int(input("Enter number or pizza order you want(if no then press 0): "))
        if pizza_quantity >= 4:
            print("*** Congratulations !! 1.5lt softdrink free ***\n")

        pizza_calculate = pizza_quantity*10.99
        pizza_count += pizza_calculate
        number_pasta_quantity += pizza_quantity

        print("your pizza order amount is : ",pizza_calculate)

        pasta_quantity = int(input("Enter number or pasta order you want(if no then press 0): "))
        if pasta_quantity >= 4:
            print("*** Congratulations !! get 2 bruschetta free ***")
            print("*** Congratulations !! get 2 chocco brownies ice cream free ***\n")
        
        pasta_calculate = pasta_quantity*9.5
        pasta_count += pasta_calculate
        number_pasta_quantity += pasta_quantity

        print("your pizza order amount is : ",pasta_quantity*9.5)
        
        total_sum = pizza_calculate + pasta_calculate
        total_sum_count += total_sum
        total_number_quantity = number_pasta_quantity + number_pizza_quantity

        print(" your total order is : ",total_sum)
        print("-----> your Net order amount of the day is : ",total_sum)
        ch = input(" want to enter order from another customer (Y/N) : ")
        if ch=="n" or ch=="N" or ch=="no" or ch=="NO":
            break
    
    print("\n----------- Pizza and pasta Bill --------------\n")
    print(" payment received from pizza : ",pizza_count)
    print(" payment received from pasta : ",pasta_count)
    print(" payment received today : ",total_sum_count)
    print(" Number of pizza and pasta sold in one shift : ",total_number_quantity)

    print("BYE BYE !!!")
    
def mainmenu():
    print()
    print("--------------------------------------------------------------------------------\n               Welcome to Amazing Pizza and Pasta Pizzeria \n--------------------------------------------------------------------------------")
    print()
    print("press : 1 order menu")
    print("press : 2 exit")

while True:
    mainmenu()
    ch=int(input("enter your choice: "))
    if ch==1:
        order()
    elif ch==2:
        break

