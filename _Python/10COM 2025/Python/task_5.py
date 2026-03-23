print("You account balance is 500")
withdraw = int(input("How much do you want to withdraw?"))
balance = 500
if withdraw > balance:
    print("Insufficient funds!")
elif withdraw <= balance:
    print("Withdrawal successful. Your new balance is X.")
