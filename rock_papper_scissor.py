import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissor =("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

list =[rock,paper,scissor]



print("What do want to choose? Type 0 for rocks,1 for paper, 2 for scissor : ")
ur_choice = int(input("Your Choice :"))
print(list[ur_choice])
test = random.randint(0, 2)
print(f"Computer Chose : {test}")
print(list[test])
if ur_choice == 0:
    if test==1:
        print("You lost")
    elif test==2:
        print("you won")
    else:
        print("its a draw")
if ur_choice == 1:
    if test==0:
        print("You won")
    elif test==2:
        print("you lost")
    else:
        print("its a draw")

if ur_choice == 2:
    if test==1:
        print("You won")
    elif test==0:
        print("you lost")
    else:
        print("its a draw")












