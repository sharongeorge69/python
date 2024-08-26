import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
choice_letter = int(input("How many letters do you want in ur password : "))
choice_number = int(input("How many numbers do you want : "))
choice_symbol = int(input("How many symbols do you want : "))
password = [] #for adding the random letter/num/symbol to list
for i in range(0,choice_letter):
    password.append(random.choice(letters))
for j in range(0,choice_number):
    password.append(random.choice(numbers))
for k in range(0,choice_symbol):
    password.append(random.choice(symbols))
random.shuffle(password) #to shuffle the password randomly

passwords =""
for l in password:
    passwords+=l
print(f"Your password is {passwords}")


