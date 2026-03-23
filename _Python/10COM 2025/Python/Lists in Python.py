cheeses = ["Cheddar", "Brie", "Camembert", "Edam"]

print(cheeses[1])

print()
print("First loop example")
for cheese in cheeses:
    print(cheese)

cheeses.append("Mozzarella")

print()
print("Second loop example")
for i in range(len(cheeses)):
    print(cheeses[i])