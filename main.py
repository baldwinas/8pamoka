# Homework 7.1
mood = input("What is your mood today?")
if mood == "happy":
    print("It is a pleasure to see you happy!")
elif mood == "anxious":
    print("take a rest")
elif mood == "sad":
    print("Go watch a funny movie")
elif mood == "excited":
    print("Go party!")
elif mood == "tired":
    print("Go to sleep")
else:
    print("There is no such mood")

# Homework 7.2
secret = 21
guess = int(input("Iveskite stebuklinga skaiciu: "))
if guess == secret:
    print("Sveikiname! Jus atspejote stebuklinga skaiciu!")
else:
    print("Bandykite dar karta.")

# Homework 7.3
x = int(input("Iveskite pirma skaiciu: "))
y = int(input("Iveskite antra skaiciu: "))
operation = input("Pasirinkite matematine operacija (+, -, *, /): ")

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
else:
    print("Neivedete teisingos operacijos")
