temperature = int(input("Enter the temperature in Celsius:"))
if temperature >= 30:
    print("It's hot! Wear shorts and drink water!")
elif temperature >= 20:
    print("Nice weather! Maybe a t-shirt?")
elif temperature >= 10:
    print("Getting chilly! Wear a jacket!")
elif temperature < 10:
    print("Brrr! Time for a coat and scarf!")