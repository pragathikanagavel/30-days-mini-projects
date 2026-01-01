import random

special_chars = "!@#$%^&*"

def check_password(password):
    missing = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        missing.append("Minimum length 8")

    if any(c.isupper() for c in password):
        score += 1
    else:
        missing.append("At least one uppercase letter")

    if any(c.islower() for c in password):
        score += 1
    else:
        missing.append("At least one lowercase letter")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        missing.append("At least one digit")

    if any(c in special_chars for c in password):
        score += 1
    else:
        missing.append("At least one special character")

    if score <= 2:
        strength = "Very Weak"
    elif score == 3:
        strength = "Weak"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, missing


def generate_password():
    password = ""
    password += chr(random.randint(65, 90))    # Uppercase
    password += chr(random.randint(97, 122))   # Lowercase
    password += str(random.randint(0, 9))       # Digit
    password += random.choice(special_chars)   # Special

    while len(password) < 10:
        password += chr(random.randint(33, 126))

    password_list = list(password)
    random.shuffle(password_list)
    return "".join(password_list)


while True:
    print("\n=== Password Strength Checker ===")
    print("1. Check Password Strength")
    print("2. Generate Strong Password")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        pwd = input("Enter password: ")
        strength, missing_rules = check_password(pwd)

        print("\nPassword Strength:", strength)

        if strength in ["Very Weak", "Weak"]:
            print("Suggestions to improve:")
            for rule in missing_rules:
                print("-", rule)

    elif choice == "2":
        new_pwd = generate_password()
        print("\nGenerated Strong Password:", new_pwd)

    elif choice == "3":
        print("Exiting... Stay Secure 🔐")
        break

    else:
        print("Invalid choice. Try again!")
