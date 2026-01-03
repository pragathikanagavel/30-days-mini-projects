import sqlite3

# ---------- DATABASE CONNECTION ----------
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# ---------- CREATE TABLES ----------
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    book_id TEXT PRIMARY KEY,
    name TEXT,
    author TEXT,
    status TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS issued (
    book_id TEXT,
    student TEXT
)
""")

conn.commit()

# ---------- ADD BOOK ----------
def add_book():
    book_id = input("Enter Book ID: ")
    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    try:
        cursor.execute(
            "INSERT INTO books VALUES (?, ?, ?, ?)",
            (book_id, name, author, "Available")
        )
        conn.commit()
        print("✅ Book added successfully!\n")
    except sqlite3.IntegrityError:
        print("❌ Book ID already exists!\n")

# ---------- ISSUE BOOK ----------
def issue_book():
    book_id = input("Enter Book ID to issue: ")
    student = input("Enter Student Name: ")

    cursor.execute(
        "SELECT status FROM books WHERE book_id = ?", (book_id,)
    )
    book = cursor.fetchone()

    if book and book[0] == "Available":
        cursor.execute(
            "UPDATE books SET status = 'Issued' WHERE book_id = ?",
            (book_id,)
        )
        cursor.execute(
            "INSERT INTO issued VALUES (?, ?)",
            (book_id, student)
        )
        conn.commit()
        print("📕 Book issued successfully!\n")
    else:
        print("❌ Book not available or not found!\n")

# ---------- RETURN BOOK ----------
def return_book():
    book_id = input("Enter Book ID to return: ")

    cursor.execute(
        "SELECT * FROM issued WHERE book_id = ?", (book_id,)
    )
    record = cursor.fetchone()

    if record:
        cursor.execute(
            "DELETE FROM issued WHERE book_id = ?",
            (book_id,)
        )
        cursor.execute(
            "UPDATE books SET status = 'Available' WHERE book_id = ?",
            (book_id,)
        )
        conn.commit()
        print("📗 Book returned successfully!\n")
    else:
        print("❌ This book was not issued!\n")

# ---------- DISPLAY BOOKS ----------
def display_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    print("\n--- Library Books ---")
    for book in books:
        print(book)
    print()

# ---------- MENU ----------
def menu():
    while True:
        print("===== LIBRARY MANAGEMENT SYSTEM (DB) =====")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Display Books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            issue_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            print("👋 Exiting system")
            break
        else:
            print("⚠ Invalid choice!\n")

# ---------- MAIN ----------
if __name__ == "__main__":
    menu()
    conn.close()
