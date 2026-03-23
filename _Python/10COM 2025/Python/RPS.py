import random
computer_number = random.randint(1,3)

if computer_number == 1:
    com_choice = "Rock"
if computer_number == 2:
    comp_choice = "Paper"
if computer_number == 3:
    comp_choice = "scissors"
print("rock is 1, paper is 2, scissors is 3")
user_number = int(input("Enter 1, 2, or 3: "))

if user_number == 1:
    user_choice = "Rock"
elif user_number == 2:
    user_choice = "Paper"
else:
    user_choice = "Scissors"

print(f"You chose: {user_choice}")
print(f"Computer chose: {comp_choice}")

if user_choice == comp_choice:
    print("It's a tie!")
elif (user_choice == "Rock" and comp_choice == "Scissors") or \
     (user_choice == "Paper" and comp_choice == "Rock") or \
     (user_choice == "Scissors" and comp_choice == "Paper"):
    print("You win!")
else:
    print("Computer wins!")
