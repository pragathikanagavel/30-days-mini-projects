import sqlite3

# Connect to database (creates if it doesn't exist)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Drop existing table if it exists
cursor.execute("DROP TABLE IF EXISTS students")
conn.commit()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT,
    marks INTEGER CHECK(marks BETWEEN 0 AND 100)
)
""")

# Insert sample records
cursor.executemany("""
INSERT INTO students (id, name, department, marks) VALUES (?, ?, ?, ?)
""", [
    (1, 'Pragathi', 'CSE', 87),
    (2, 'Arun', 'ECE', 72),
    (3, 'Divya', 'IT', 91),
    (4, 'Karthik', 'EEE', 65),
    (5, 'Meena', 'CSE', 48)
])
conn.commit()

# Query 1: Show all students
print("📚 All Students:")
print("-" * 50)
print(f"{'ID':<5} {'Name':<15} {'Department':<12} {'Marks':<5}")
print("-" * 50)
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(f"{row[0]:<5} {row[1]:<15} {row[2]:<12} {row[3]:<5}")

# Query 2: Students with marks >= 75
print("\n📊 Students with marks >= 75:")
print("-" * 45)
print(f"{'Name':<15} {'Department':<12} {'Marks':<5}")
print("-" * 45)
cursor.execute("SELECT name, department, marks FROM students WHERE marks >= 75")
for row in cursor.fetchall():
    print(f"{row[0]:<15} {row[1]:<12} {row[2]:<5}")

# Query 3: Students who failed
print("\n❌ Students who failed (marks < 50):")
print("-" * 30)
print(f"{'Name':<15} {'Marks':<5}")
print("-" * 30)
cursor.execute("SELECT name, marks FROM students WHERE marks < 50")
for row in cursor.fetchall():
    print(f"{row[0]:<15} {row[1]:<5}")

conn.close()
print("\n✓ Database operations completed successfully!")
