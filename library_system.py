# Library Management System - Day 10 Project

BOOKS_FILE = "books.txt"
ISSUED_FILE = "issued.txt"

# ---------- ADD BOOK ----------
def add_book():
    book_id = input("Enter Book ID: ")
    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    with open(BOOKS_FILE, "a") as file:
        file.write(f"{book_id},{name},{author}\n")

    print("✅ Book added successfully!\n")

# ---------- ISSUE BOOK ----------
def issue_book():
    book_id = input("Enter Book ID to issue: ")
    student = input("Enter Student Name: ")

    with open(BOOKS_FILE, "r") as file:
        books = file.readlines()

    found = False
    with open(BOOKS_FILE, "w") as file:
        for book in books:
            if book.startswith(book_id + ","):
                found = True
            else:
                file.write(book)

    if found:
        with open(ISSUED_FILE, "a") as file:
            file.write(f"{book_id},{student}\n")
        print("📕 Book issued successfully!\n")
    else:
        print("❌ Book not found!\n")

# ---------- RETURN BOOK ----------
def return_book():
    book_id = input("Enter Book ID to return: ")

    with open(ISSUED_FILE, "r") as file:
        issued = file.readlines()

    found = False
    with open(ISSUED_FILE, "w") as file:
        for record in issued:
            if record.startswith(book_id + ","):
                found = True
            else:
                file.write(record)

    if found:
        print("📗 Book returned successfully!\n")
    else:
        print("❌ Book not issued!\n")

# ---------- MENU ----------
def menu():
    while True:
        print("===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            issue_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            print("👋 Exiting Library System. Goodbye!")
            break
        else:
            print("⚠ Invalid choice! Try again.\n")

# ---------- MAIN ----------
if __name__ == "__main__":
    menu()
