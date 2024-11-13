#!/usr/bin/env python3

import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if characters == "":
        raise ValueError("At least one character set must be selected")

    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the desired password length: "))

    use_upper = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    use_lower = input("Include lowercase letters? (yes/no): ").lower() == "yes"
    use_digits = input("Include digits? (yes/no): ").lower() == "yes"
    use_special = input("Include special characters? (yes/no): ").lower() == "yes"

    try:
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print(f"Generated password: {password}")
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()
