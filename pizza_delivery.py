sizee = input("What size pizza do you want S,M or L : ")
pepperoni = input("Do u want pepperoni Yes or No: ")
want_cheese =input("Extra cheese? : ")
bill =0
if sizee =="s":
    bill+=15
elif sizee=="m":
    bill+=20
elif sizee == "l":
    bill += 25
else:
    print("You have entered wrong input!")

if pepperoni=="y":
    if sizee =="s":
        bill+=2
    else:
        bill+=3
if want_cheese =="y":
    bill+=1

print(f"UR final bill is ${bill}")
