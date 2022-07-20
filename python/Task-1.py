print("----------------------------------------\n       Welcome to JAY BHAVANI      \n-----------------------------------------")
print()

name = input("What is your name? --> ")
name = name.title()
print("""Hello {}, welcome to JAY BHAVANI SNACKS""".format(name))
print()

main_menu = {
"vadapav" : {
'qty' : 8,
'price' :30,
},
"bhel" : {
'qty' : 7,
'price' :70,
},
"dabeli" : {
'qty' : 9,
'price' :35,
},
}
for item in main_menu.keys():
    qty = (main_menu[item]["qty"])
    price = (main_menu[item]["price"])
    print(item, ":", qty, ":", price)

status = True
total_price = 0
inner_dic = {}

while status:
    customer_item = input("Enter your product : ")
    customer_qty = int(input("Enter qty : "))

    qtychk = main_menu[customer_item]['qty']

    if customer_qty > qtychk:
        print("Soryy!! we haven't enough stock..we have only ",qtychk, "qty if you want to i will gives you")
        choice = input("Do you want to ? Y/N : ")
        if choice == "No" or choice == "N" or choice == "n" or choice=="no":
            print("Thank you have nice day")
        else:
            fqty = main_menu[customer_item]['qty']
            inner_dic[customer_item] = fqty
            cprice = main_menu[customer_item]['price']
            qty_price = fqty * cprice
            total_price += qty_price

            choice = input("Do you want to add more items?")
            if choice == "No" or choice == "N" or choice == "n" or choice=="no":
                status = False
    else:
        inner_dic[customer_item] = customer_qty
        cprice = main_menu[customer_item]['price']
        qty_price = customer_qty * cprice
        total_price += qty_price

        choice = input("Do you want to add more items?")
        if choice == "No" or choice == "N" or choice == "n":
            status = False

print(inner_dic)
print("Total Bill = ",total_price)
