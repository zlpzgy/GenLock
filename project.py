import random
import string
import os

def main():
    """
    Main function to prompt the user for password generation settings 
    and display or store the resulting password.
    """
    print("Welcome to GenLock: Your Pythonic Password Generator!")

    # Ask user for desired password length
    try:
        length = int(input("Enter desired password length (default is 12): ") or "12")
    except ValueError:
        length = 12  # fallback if input is invalid

    # Ask user whether they want special characters
    special_chars_choice = input("Include special characters? (y/n, default=y): ").lower() or "y"
    use_special_chars = True if special_chars_choice.startswith('y') else False

    # Ask user whether they want digits
    digits_choice = input("Include digits? (y/n, default=y): ").lower() or "y"
    use_digits = True if digits_choice.startswith('y') else False

    # Generate the password
    password = generate_password(length, use_special_chars, use_digits)
    print(f"\nGenerated Password: {password}")

    # Check strength
    strength = is_password_strong(password)
    print(f"Password Strength: {strength}")

    # Optionally store the password
    store_choice = input("Would you like to store this password in a file? (y/n, default=n): ").lower() or "n"
    if store_choice.startswith('y'):
        store_password(password)
        print("Password stored in passwords.txt")

def generate_password(length=12, use_special_chars=True, use_digits=True):
    """
    Generate a random password of a given length.
    
    Args:
        length (int): The length of the password.
        use_special_chars (bool): Whether to include special characters.
        use_digits (bool): Whether to include digits.
    
    Returns:
        str: The generated password.
    """
    # Basic character set: letters
    chars = list(string.ascii_letters)

    # Optionally include digits
    if use_digits:
        chars.extend(string.digits)

    # Optionally include punctuation
    if use_special_chars:
        # Exclude whitespace-like or ambiguous chars as desired
        special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?"
        chars.extend(special_chars)

    # Generate the password
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def is_password_strong(password):
    """
    Check the 'strength' of a password based on arbitrary rules (length, chars).
    
    Args:
        password (str): The password to check.

    Returns:
        str: "Weak", "Moderate", or "Strong" depending on the password's length 
             and complexity.
    """
    # Simple checks for illustrative purposes
    length_score = len(password)
    digit_score = sum(c.isdigit() for c in password)
    special_score = sum(not c.isalnum() for c in password)

    # Example scoring logic
    score = 0
    score += length_score
    score += digit_score * 2
    score += special_score * 3

    if score < 15:
        return "Weak"
    elif score < 25:
        return "Moderate"
    else:
        return "Strong"

def store_password(password, filename="passwords.txt"):
    """
    Append the password to a file (default: passwords.txt).
    
    Args:
        password (str): The password to store.
        filename (str): The file in which to store the password.
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(password + os.linesep)

if __name__ == "__main__":
    main()