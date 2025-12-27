# Student Record System using File Handling

FILE_NAME = "students.txt"

def add_student():
    try:
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        dept = input("Enter Department: ")
        marks = int(input("Enter Marks (0-100): "))

        if marks < 0 or marks > 100:
            print(" Marks must be between 0 and 100")
            return

        with open(FILE_NAME, "a") as file:
            file.write(f"{roll},{name},{dept},{marks}\n")

        print(" Student record added successfully")

    except ValueError:
        print(" Invalid input. Marks must be a number")


def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

            if not records:
                print("No student records found")
                return

            print("\nRoll | Name | Department | Marks")
            print("-" * 35)

            for line in records:
                roll, name, dept, marks = line.strip().split(",")
                print(f"{roll} | {name} | {dept} | {marks}")

    except FileNotFoundError:
        print(" File not found")


def search_student():
    roll_search = input("Enter Roll Number to search: ")
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                roll, name, dept, marks = line.strip().split(",")

                if roll == roll_search:
                    print("\n Student Found")
                    print(f"Roll Number : {roll}")
                    print(f"Name        : {name}")
                    print(f"Department  : {dept}")
                    print(f"Marks       : {marks}")
                    found = True
                    break

        if not found:
            print("Student not found")

    except FileNotFoundError:
        print("File not found")


def main():
    while True:
        print("\n--- Student Record System ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print(" Exiting program")
            break
        else:
            print("Invalid choice. Try again")


main()
