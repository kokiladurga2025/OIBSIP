import random

small_letters = "abcdefghijklmnopqrstuvwxyz"
capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special_symbols = "!@#$%^&*?"

all_characters = ""

password_length = int(input("Enter the password length: "))

include_letters = input("Do you want letters? (yes/no): ")
if include_letters == "yes":
    all_characters += small_letters + capital_letters

include_numbers = input("Do you want numbers? (yes/no): ")
if include_numbers == "yes":
    all_characters += digits

include_symbols = input("Do you want symbols? (yes/no): ")
if include_symbols == "yes":
    all_characters += special_symbols

if all_characters == "":
    print("You must choose at least one character type.")
else:
    generated_password = ""

    for i in range(password_length):
        generated_password += random.choice(all_characters)

    print("Your generated password is:", generated_password)
