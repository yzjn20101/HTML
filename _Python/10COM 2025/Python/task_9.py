age = int(input("Enter your age:"))
if age <= 10:
    print("You can watch G-rated movies.")
elif age <= 12:
    print("You can watch PG movies.")
elif age <= 17:
    print("You can watch PG-13 movies.")
elif age >= 18:
    print("You can watch R-rated movies.")