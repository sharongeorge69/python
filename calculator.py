print("Welcome to the tip calculator")
bill = float(input("Enter the amount in the bill :"))
tip = float(input("How much tip ?10,12 or 15 : "))
spilt = int(input("How much person do you want to split it with : "))
percentage = (tip / 100) * bill
result =(bill+percentage)/spilt
total_bill=round(result, 2)
print(f"Each should pay : {total_bill}")






