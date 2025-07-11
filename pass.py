import random
import string

print("Hi there! Ready to create a strong password?")
length = int(input("How many characters should your password have? "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

all_chars = lower + upper + digits + symbols
password = "".join(random.choices(all_chars, k=length))

print("\nHere’s your unique and secure password:")
print(password)
print("\nStay safe out there 🔐")
