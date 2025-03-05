"""
project.py

GenLock: A simple password generator.
THREE ADDITIONAL CUSTOM FUNCTIONS:
1) parse_requirements_from_string()
2) bulk_generate_passwords()
3) obscure_password()
"""

import random
import string
import os

def main():
    """
    Main function that orchestrates the primary workflow of the program.
    """
    print("Welcome to GenLock: Your Pythonic Password Generator!")

    # Simple demonstration of the new custom functions:
    req_string = "length=12,special=True,digits=False"
    length, use_special, use_digits = parse_requirements_from_string(req_string)
    password = generate_password(length, use_special, use_digits)
    print(f"[parse_requirements_from_string Demo] -> {password}")

    # Demonstrate bulk password generation
    bulk = bulk_generate_passwords(count=3, length=8, use_special_chars=True, use_digits=True)
    print("[bulk_generate_passwords Demo] ->", bulk)

    # Show obscure_password usage
    obscured = obscure_password(password)
    print(f"[obscure_password Demo] Original: {password}, Obscured: {obscured}")

    # Prompt user for an interactive password generation (original logic)
    try:
        length = int(input("Enter desired password length (default 12): ") or "12")
    except ValueError:
        length = 12

    use_special_chars = (input("Include special characters? (y/n, default=y): ") or "y").lower().startswith('y')
    use_digits = (input("Include digits? (y/n, default=y): ") or "y").lower().startswith('y')

    final_pwd = generate_password(length, use_special_chars, use_digits)
    print(f"Final Password: {final_pwd}")

    strength = is_password_strong(final_pwd)
    print(f"Password Strength: {strength}")

    if input("Save password to file? (y/n, default=n): ").lower().startswith('y'):
        store_password(final_pwd)
        print("Password saved to passwords.txt")


# ---------------------------------------------------------------------------
# Original three custom functions
# ---------------------------------------------------------------------------

def generate_password(length=12, use_special_chars=True, use_digits=True):
    """
    Generate a random password of a given length.
    """
    chars = list(string.ascii_letters)
    if use_digits:
        chars.extend(string.digits)
    if use_special_chars:
        special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?"
        chars.extend(special_chars)

    return ''.join(random.choice(chars) for _ in range(length))


def is_password_strong(password):
    """
    Check the 'strength' of a password based on length and character diversity.
    Returns "Weak", "Moderate", or "Strong".
    """
    length_score = len(password)
    digit_score = sum(c.isdigit() for c in password)
    special_score = sum(not c.isalnum() for c in password)

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
    with open(filename, "a", encoding="utf-8") as file:
        file.write(password + os.linesep)


# ---------------------------------------------------------------------------
# Three NEW custom functions
# ---------------------------------------------------------------------------

def parse_requirements_from_string(req_string):
    """
    Parses a simple comma-separated string of requirements such as:
        "length=12,special=True,digits=False"
    
    Returns:
        (length, use_special_chars, use_digits)
    """
    # Default settings
    length = 12
    use_special = True
    use_digits = True

    segments = req_string.split(',')
    for seg in segments:
        key, val = seg.split('=')
        key = key.strip().lower()
        val = val.strip()

        if key == "length":
            # Safely convert to int if possible
            try:
                length = int(val)
            except ValueError:
                pass
        elif key == "special":
            use_special = (val.lower() == "true")
        elif key == "digits":
            use_digits = (val.lower() == "true")

    return length, use_special, use_digits


def bulk_generate_passwords(count=5, length=12, use_special_chars=True, use_digits=True):
    """
    Generates multiple passwords at once.

    Args:
        count (int): How many passwords to generate.
        length (int): The length of each password.
        use_special_chars (bool): Whether to include special characters.
        use_digits (bool): Whether to include digits.

    Returns:
        list of str: A list containing 'count' randomly generated passwords.
    """
    passwords = []
    for _ in range(count):
        pwd = generate_password(length, use_special_chars, use_digits)
        passwords.append(pwd)
    return passwords


def obscure_password(password):
    """
    Replaces some characters with '*' to partially obscure the password,
    making it less readable on screen while still showing length.

    Example:
        "Password123!" -> "Pa******123!"
    """
    # For simplicity, mask the middle half of the characters
    length = len(password)
    if length < 4:
        return '*' * length  # mask fully if too short

    start = password[:2]
    end = password[-2:]
    middle = '*' * (length - 4)

    return start + middle + end


if __name__ == "__main__":
    main()