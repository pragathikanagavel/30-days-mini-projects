# Simple URL Shortener (Beginner Level)

file_name = "urls.txt"

# Create short code using numbers
def create_short_code():
    import random
    return str(random.randint(1000, 9999))


# Save URL in file
def save_url(short_code, long_url):
    file = open(file_name, "a")
    file.write(short_code + "," + long_url + "\n")
    file.close()


# Find URL from file
def find_url(short_code):
    try:
        file = open(file_name, "r")
        for line in file:
            if line.strip():  # Skip empty lines
                code, url = line.strip().split(",", 1)
                if code == short_code:
                    file.close()
                    return url
        file.close()
    except FileNotFoundError:
        print("Error: urls.txt file not found")
    except ValueError as e:
        print(f"Error reading file: {e}")
    return None


# Main program
while True:
    print("\n--- URL SHORTENER ---")
    print("1. Shorten URL")
    print("2. Retrieve URL")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        long_url = input("Enter long URL: ")
        short_code = create_short_code()
        save_url(short_code, long_url)
        print("Short URL is: short.ly/" + short_code)

    elif choice == "2":
        code = input("Enter short code: ").strip()
        print(f"Searching for code: '{code}'")
        
        # Debug: Show what's in the file
        try:
            with open(file_name, "r") as f:
                lines = f.readlines()
                print(f"File has {len(lines)} entries")
                for line in lines:
                    if line.strip():
                        stored_code = line.strip().split(",", 1)[0]
                        print(f"Found code in file: '{stored_code}'")
        except Exception as e:
            print(f"Debug error: {e}")
        
        result = find_url(code)
        if result:
            print("Original URL:", result)
        else:
            print("Short code not found")

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice")
