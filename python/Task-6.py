print("=============== KALYAN JWELLERS ===============")
firstname=input("\nfirst name:")
lastname=input("last name:")
age=int(input("age:"))
Gender=input("gender:")
vaccine=input("vaccination status:")
PA=int(input("\nenter purchase amount:"))


discountA = 0
if PA>=100000 and PA<=200000:
    MakingC=0.08*PA
    Making=PA+(0.08*PA)
    print("making charges:",MakingC)
    print("total amount with making charges:",Making)
elif PA>200000 and PA<300000:
    MakingC=0.12*PA
    Making=PA+(0.12*PA)
    print("making charges:",MakingC)
    print("total amount with making charges:",Making)
elif PA>=300000:
    MakingC=0.16*PA
    Making=PA+(0.16*PA)
    print("making charges:",MakingC)
    print("total amount with making charges:",Making)
else:
    pass
    

if age>=65:
    if Gender == "male":
        if PA>=100000 and PA<200000:
            discountA=0.15*PA
            Discount=PA-(0.15*PA)
            print("discount amount",discountA)
        elif PA>=200000 and PA<300000:
            discountA=0.25*PA
            Discount=PA-(0.25*PA)
            print("discount amount",discountA)
        elif PA>=300000:
            discountA=0.35*PA
            Discount=PA-(0.35*PA)
            print("discount amount",discountA)
    else:
        if PA>=100000 and PA<200000:
            discountA=0.20*PA
            Discount=PA-(0.20*PA)
            print("discount amount",discountA)
        elif PA>=200000 and PA<300000:
            discountA=0.30*PA
            Discount=PA-(0.30*PA)
            print("discount amount",discountA)
        elif PA>=200000 and PA<300000:
            discountA=0.40*PA
            Discount=PA-(0.40*PA)
            print("discount amount",discountA)
        else:
            pass
else:
    pass

if age<=65:
    if Gender == "male":
        if PA>=100000 and PA<200000:
            discountA=0.10*PA
            Discount=PA-(0.10*PA)
            print("discount amount",discountA)
        elif PA>=200000 and PA<300000:
            discountA=0.20*PA
            Discount=PA-(0.20*PA)
            print("discount amount",discountA)
        elif PA>=300000:
            discountA=0.30*PA
            Discount=PA-(0.35*PA)
            print("discount amount",discountA)
    else:
        if PA>=100000 and PA<200000:
            discountA=0.15*PA
            Discount=PA-(0.15*PA)
            print("discount amount",discountA)
        elif PA>=200000 and PA<300000:
            discountA=0.25*PA
            Discount=PA-(0.25*PA)
            print("discount amount",discountA)
        elif PA>=200000 and PA<300000:
            discountA=0.35*PA
            Discount=PA-(0.35*PA)
            print("discount amount",discountA)
        else:
            pass
else:
    pass

netamount=PA+MakingC-discountA
print("\n::::::::::::::: INVOICE :::::::::::::::")
print(firstname, lastname)
print(Gender)
print(age)
print("purchase amount:",PA)
print("making charges:",MakingC)
print("total amount with making charge:", Making)
print("discount amount:",discountA)
print("total amount with discount:",Discount)
print("total net amount:",netamount)



