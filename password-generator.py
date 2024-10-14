import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    # Define the character sets based on user preferences
    character_pool = ""
    
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation
    
    # Ensure that at least one character set is selected
    if not character_pool:
        raise ValueError("At least one character type should be selected.")
    
    # Generate the password
    password = ''.join(random.choice(character_pool) for i in range(length))
    
    return password

def main():
    try:
        # Get user input for password preferences
        length = int(input("Enter the password length (at least 6): "))
        if length < 6:
            raise ValueError("Password length should be at least 6 characters.")
        
        use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
        
        # Generate and display the password
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print("Generated Password: ", password)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()


