# GenLock: Your Pythonic Password Generator

#### Video Demo: 

## Description
GenLock is a Python-based password generator that creates strong, random passwords for you in seconds. Specify length, choose whether to include special characters or digits, and even obscure your password’s middle characters to prevent prying eyes. Store all your passwords in a convenient file for quick reference.

## Features
- **Customizable Password Generation**: Control length, special characters, and digits.  
- **Password Strength Check**: Identifies if a generated password is Weak, Moderate, or Strong.  
- **Obscuring Function**: `obscure_password` masks the middle portion of a password.  
- **Secure Storage**: Save passwords in a local file for later retrieval.  
- **Automated Tests**: A `test_project.py` file ensures everything works as intended.

## File Overview
1. **project.py**  
   - **`main()`**: The entry point, prompting for user inputs (length, special chars, digits) and optionally storing passwords.  
   - **`generate_password(length, use_special_chars, use_digits)`**: Creates a random password given user criteria.  
   - **`is_password_strong(password)`**: Rates the generated password’s overall strength.  
   - **`store_password(password, filename="passwords.txt")`**: Appends the password to a local file.  
   - **`obscure_password(password)`**: Masks the middle characters of a password, preserving only the first and last two characters.

2. **test_project.py**  
   - Houses unit tests (using `pytest`) for each of the above functions.  
   - Ensures the password generation, strength checking, storing, and obscuring features all behave as expected.

3. **requirements.txt**  
   - Lists required third-party libraries (only `pytest`, if that’s all you need).  
   - Install with:
     ```bash
     pip install -r requirements.txt
     ```

4. **README.md**  
   - This documentation file, explaining how to set up and use GenLock.  
   - Includes your project’s overview, instructions, and video demo link.

## How to Install & Run GenLock
1. **Clone This Repository**  
   ```bash
   git clone https://github.com/zlpzgy/GenLock
   cd GenLock