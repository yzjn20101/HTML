package = int(input("Enter the package weight in kg:"))
if package <= 2:
    print("Shipping is $5")
if package <= 5:
    print("Shipping is $10")
if package <= 10:
    print("Shipping is $20")
if package > 10:
    print("Package too heavy to ship!")