status = True
while status:
    import datetime
    d = datetime.datetime.now()
    str_current_datetime = str(d)
    f=d.date()

    file_name = str(f)+".txt"
    file = open(file_name,'a')
    
    print(d)
    name = input("Enter your Name :")
    age = input("Enter your Age :")
    gender = input("Enter your Gender Male or Female :")
    vaccine = input("Eter your completed dose 1 or 2 :")
    file.write("\n ===================")
    

    file.write("\n Name ="+name)
    file.write("\n Age ="+age)
    file.write("\n Gender ="+gender)
    file.write("\n Vaccine ="+vaccine) 
    file.write("\n ===================")
    choice = input("Do you like to add another person details : y or n ::")
    if choice == 'y' or choice == 'Y':
        pass
    else:
        status = False
file.close()

print("""thank you {} for register !!!!""".format(name))
