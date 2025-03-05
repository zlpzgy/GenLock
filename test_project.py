"""
project.py

GenLock: A simple password generator with obscuring functionality.

Citations:
- Used ChatGPT (on 3/3/2025) to brainstorm function outlines and docstrings.
"""

import random
import string
import os

def main():
    """
    Main function that orchestrates the primary workflow of the program.
    """
    print("Welcome to GenLock: Your Pythonic Password Generator!")

    try:
        length = int(input("Enter desired password length (default=12): ") or "12")
    except ValueError:
        length = 12

    use_special_chars = (input("Include special chars? (y/n, default=y): ") or "y").lower().startswith('y')
    use_digits = (input("Include digits? (y/n, default=y): ") or "y").lower().startswith('y')

    pwd = generate_password(length, use_special_chars, use_digits)
    print(f"\nGenerated Password: {pwd}")

    strength = is_password_strong(pwd)
    print(f"Password Strength: {strength}")

    # Example usage of obscure_password
    obscured_pwd = obscure_password(pwd)
    print(f"Obscured Password: {obscured_pwd}")

    if input("Save password to file? (y/n, default=n): ").lower().startswith('y'):
        store_password(pwd)
        print("Password saved to passwords.txt")

def generate_password(length=12, use_special_chars=True, use_digits=True):
    """
    Generate a random password of a given length.
    """
    chars = list(string.ascii_letters)
    if use_digits:
        chars.extend(string.digits)
    if use_special_chars:
        # Exclude ambiguous characters if desired
        special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?"
        chars.extend(special_chars)

    return ''.join(random.choice(chars) for _ in range(length))

def is_password_strong(password):
    """
    Check the strength of a password based on length and character diversity.
    Returns "Weak", "Moderate", or "Strong".
    """
    length_score = len(password)
    digit_score = sum(c.isdigit() for c in password)
    special_score = sum(not c.isalnum() for c in password)

    # Basic scoring logic
    score = length_score + (digit_score * 2) + (special_score * 3)

    if score < 15:
        return "Weak"
    elif score < 25:
        return "Moderate"
    else:
        return "Strong"

def store_password(password, filename="passwords.txt"):
    """
    Appends the password to the specified file (default: passwords.txt).
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(password + os.linesep)

def obscure_password(password):
    """
    Replaces some middle characters with '*' to partially obscure the password,
    preserving the first and last two characters as-is.
    """
    length = len(password)
    if length < 4:
        return '*' * length  # If shorter than 4, mask everything

    start = password[:2]
    end = password[-2:]
    middle = '*' * (length - 4)

    return start + middle + end

if __name__ == "__main__":
    main()