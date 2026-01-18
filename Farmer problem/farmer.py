import csv
from collections import Counter

FILENAME = "farmer_problems.csv"

def log_problem():
    print("\nSelect Problem Type:")
    print("1. Water Logging")
    print("2. Weeds")
    print("3. Animal Damage (Pig/Cow/etc.)")
    print("4. Middleman Exploitation")
    print("5. Other (Manual Entry)")

    choice = input("Enter choice (1-5): ")

    problems = {
        "1": "Water Logging",
        "2": "Weeds",
        "3": "Animal Damage",
        "4": "Middleman Exploitation"
    }

    if choice == "5":
        problem_type = input("Enter the problem manually: ")
    elif choice in problems:
        problem_type = problems[choice]
    else:
        print(" Invalid choice!")
        return

    location = input("Enter Village/Location: ")
    description = input("Short Description: ")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([problem_type, location, description])

    print(" Problem logged successfully!")

def view_common_problems():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            problem_list = [row[0] for row in reader]

        count = Counter(problem_list)

        print("\n Most Common Farmer Problems:")
        for problem, freq in count.items():
            print(f"{problem}: {freq}")

    except FileNotFoundError:
        print(" No data found yet!")

def main():
    while True:
        print("\n Farmer Problem Logger")
        print("1. Log a Problem")
        print("2. View Common Problems")
        print("3. Exit")

        option = input("Choose an option: ")

        if option == "1":
            log_problem()
        elif option == "2":
            view_common_problems()
        elif option == "3":
            print(" Exiting... Thank you!")
            break
        else:
            print(" Invalid option!")

main()
