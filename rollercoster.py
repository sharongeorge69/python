height = int(input("Enter ur height : "))
bill=0
if height > 120:
    print("Can ride")
    age = int(input("Enter the age : "))
    if age < 12:
        bill= 5
        print("Cost is $5")
    elif age < 18:
        print("Cost is $7")
        bill = 7
    else:
        bill=12
        print("Cost is $12")

    want_ride=input("Do you want a Photo? : ")
    if want_ride== "y":
        bill+=3

    print(f"Total bill is :{bill} ")
else:
    print("Cant ride")

