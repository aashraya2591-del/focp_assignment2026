import random

def check_password_length(password):
    """
    Checks if password is at least 9 characters long.
    Returns True if valid, False otherwise.
    """
    if len(password) < 9:
        print("Password too short.")
        return False
    return True

def verify_character(password, position):
    """
    Asks user for a character at a specific position.
    Returns True if correct, False if wrong.
    """
    user_input = input(f"Enter letter at position {position}: ")
    
   
    if user_input == password[position - 1]:
        print("Correct")
        return True
    else:
        print("Security check failed.")
        return False

def main():
    """
    Main function that runs the password verification process.
    """

    password = input("Enter your password: ")
    
  
    if not check_password_length(password):
        return
    
   
    password_length = len(password)
    random_positions = [random.randint(1, password_length) for _ in range(3)]
    
   
    for position in random_positions:
        if not verify_character(password, position):
            return
    
  
    print("Security check passed.")

if __name__ == "__main__":
    main()