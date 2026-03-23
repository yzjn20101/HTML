import random
random_number = random.randint(1, 10)

for goes in range(3):
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == random_number:
        print("Congratulations! You guessed it right.")
    elif random_number > guess:
        print("Too low")
    else:
        print("Too high")
