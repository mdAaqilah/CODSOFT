print("Hey there! Let's do some quick math 🧮")

num1 = float(input("Enter your first number: "))
num2 = float(input("Now enter your second number: "))

print("\nChoose what you'd like to do:")
print(" + for Addition")
print(" - for Subtraction")
print(" * for Multiplication")
print(" / for Division")

choice = input("So, what's your pick? ")

if choice == '+':
    result = num1 + num2
    message = "Adding them gives"
elif choice == '-':
    result = num1 - num2
    message = "Subtracting them gives"
elif choice == '*':
    result = num1 * num2
    message = "Multiplying them gives"
elif choice == '/':
    if num2 == 0:
        print("Oops! Can't divide by zero.")
        exit()
    result = num1 / num2
    message = "Dividing them gives"
else:
    print("Hmm... that doesn't look like a valid operation.")
    exit()

print(f"{message}: {result}")
print("Thanks for calculating with me!")
