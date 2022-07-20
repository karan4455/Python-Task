print("--------------------------------------------------\n               JAY BHAVANI SNACKS          \n--------------------------------------------------")

menu = {
    "vadapav" : 30,
    "dabeli" : 30,
    "bhel" : 70,
    "panipuri" : 20,
    "sandwich" : 70,
    "frechfries" : 50,
    "pulav" :  80,
}

for k,v  in menu.items():
    print(f"{k}={v}")
    print()

status = True
total_item = 0
total_qnt = 0
while status :
    item = input("Enter your product : ").lower()
    qty = int(input("Enter quantity : "))
    price = menu[item.lower()]
    print(item.title(), ' : ',price)
    print("Number Of Quatity : ",qty)
    print("Total cost : ",price * qty)
    choice = input("Do you want to add more item? Y/N : ")
    if choice == "n" or choice == "N" or choice == "no" or choice == "No":
        status = False

