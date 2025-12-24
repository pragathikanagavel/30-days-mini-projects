import csv


def get_student_details():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    return name, roll
def get_marks():
    marks = []
    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"Enter marks for Subject {i}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print(" Marks must be between 0 and 100.")
            except ValueError:
                print(" Enter numbers only.")
    return marks
def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"
def save_to_file(name, roll, total, avg, grade, status):
    with open("student_results.txt", "a") as file:
        file.write(f"Name: {name}, Roll: {roll}, Total: {total}, "
                   f"Average: {avg:.2f}, Grade: {grade}, Status: {status}\n")


def save_to_csv(name, roll, marks, total, avg, grade, status):
    with open("student_results.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, roll] + marks + [total, avg, grade, status])
def display_result(name, roll, total, avg, grade, status):
    print("\n----- STUDENT RESULT -----")
    print(f"Student Name : {name}")
    print(f"Roll No      : {roll}")
    print(f"Total Marks  : {total}")
    print(f"Average      : {avg:.2f}")
    print(f"Grade        : {grade}")
    print(f"Status       : {status}")

def main():
    print("===== STUDENT GRADING SYSTEM =====")
    
    while True:
        # Get student details
        name, roll = get_student_details()
        
        # Get marks for 5 subjects
        marks = get_marks()
        
        # Calculate total and average
        total = sum(marks)
        avg = total / len(marks)
        
        # Determine grade
        grade = calculate_grade(avg)
        
        # Determine pass/fail status
        status = "Pass" if avg >= 40 else "Fail"
        
        # Display result
        display_result(name, roll, total, avg, grade, status)
        
        # Save to files
        save_to_file(name, roll, total, avg, grade, status)
        save_to_csv(name, roll, marks, total, avg, grade, status)
        
        print("\nResult saved successfully!")
        
        # Ask if user wants to continue
        choice = input("\nDo you want to add another student? (yes/no): ").lower()
        if choice != "yes":
            print("\nThank you for using the Student Grading System!")
            break

if __name__ == "__main__":
    main()
