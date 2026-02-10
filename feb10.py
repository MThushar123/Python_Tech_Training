# Password Validator - Validate a password based on criteria (length, uppercase, lowercase, digits, special characters).

import re  

def password_validator(password):
    # Empty list to store problems 
    problems = []
    
    # Password must be 8 characters or more
    if len(password) < 8:
        problems.append(" Password too short! Need 8+ characters")
    
    # Must have at least 1 capital letter (A,B,C...Z)
    if not re.search(r'[A-Z]', password):
        problems.append(" Need 1 Capital letter (A,B,C...Z)")
    
    # Must have at least 1 small letter (a,b,c...z)
    if not re.search(r'[a-z]', password):
        problems.append(" Need 1 small letter (a,b,c...z)")
    
    # Must have at least 1 number (0,1,2...9)
    if not re.search(r'\d', password):
        problems.append(" Need 1 number (0,1,2...9)")
    
    # Must have at least 1 special character
    special_chars = "!@#$%^&*()_+-=/"
    has_special = False
    for char in password:
        if char in special_chars:
            has_special = True
            break  # Found one, stop checking
    
    if not has_special:
        problems.append(" Need 1 special char (!@#$%^...)")
    
    # Show results
    if problems:
        print("Password failed these checks:")
        for problem in problems:
            print(problem)
        print(" Try again with all rules!")
        return False
    else:
        print("Perfect password! You are safe! ")
        return True


password = input("Enter password (8+ characters): ").strip()
password_validator(password)
