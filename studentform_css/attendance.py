import csv
import os

FILE = "attendance.csv"
students = ["Alice", "Bob", "Charlie", "Diana"]

if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as file:
        pass


def mark_attendance():
    date = input("Enter date (DD-MM-YYYY): ")

    with open(FILE, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == date:
                print("Attendance already marked for this date!")
                return

    with open(FILE, "a", newline="") as file:
        writer = csv.writer(file)
        for student in students:
            while True:
                status = input(f"{student} (P/A/L): ").upper()
                if status in ["P", "A", "L"]:
                    break
                else:
                    print("Invalid input! Enter P, A, or L only.")
            writer.writerow([date, student, status])

    print("Attendance marked successfully!")


def attendance_percentage():
    name = input("Enter student name: ").lower()
    total = 0
    score = 0

    with open(FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 3 and row[1].lower() == name:
                total += 1
                if row[2] == "P":
                    score += 1
                elif row[2] == "L":
                    score += 0.5

    if total > 0:
        percent = (score / total) * 100
        print(f"{name.capitalize()} Attendance: {percent:.2f}%")

        if percent < 75:
            print("⚠ Warning: Attendance below 75%")
    else:
        print("No records found for this student.")


def absentees_by_date():
    date = input("Enter date: ")
    found = False

    print("Absent students:")
    with open(FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 3 and row[0] == date and row[2] == "A":
                print("-", row[1])
                found = True

    if not found:
        print("No absentees found for this date.")


if __name__ == "__main__":
    while True:
        print("\n--- Attendance System ---")
        print("1. Mark Attendance")
        print("2. Check Attendance Percentage")
        print("3. View Absentees by Date")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            mark_attendance()
        elif choice == "2":
            attendance_percentage()
        elif choice == "3":
            absentees_by_date()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
