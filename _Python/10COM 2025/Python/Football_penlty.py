import random

penalty_taker = int(input("Your choice? (0-left 1-center 2-right)"))

goalkeeper = random.randint(0,2)

if penalty_taker == goalkeeper:
    print("Penalty saved! ")
else:
    print("GOAL!!!!!!")