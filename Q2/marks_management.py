import sqlite3

DB_FILE = "marks.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Creating tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            roll_number INTEGER,
            subject TEXT,
            marks INTEGER,
            UNIQUE(roll_number, subject)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            subject TEXT UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value INTEGER
        )
    ''')

    cursor.execute("INSERT OR IGNORE INTO settings (key, value) VALUES ('marks_finalized', 0)")

    # Add students if not already present
    cursor.execute("SELECT COUNT(DISTINCT roll_number) FROM students")
    student_count = cursor.fetchone()[0]

    if student_count < 10:
        students = [
            (101, "Priyanshu"), (102, "Ravi"), (103, "Narendar"), (104, "Rahul"),
            (105, "Aurobindo"), (106, "John"), (107, "Jack"), (108, "Amir"),
            (109, "Ivy"), (110, "Jim")
        ]
        subjects = ["Physics", "Chemistry", "Mathematics"]

        for roll_number, name in students:
            for subject in subjects:
                cursor.execute("INSERT OR IGNORE INTO students (name, roll_number, subject, marks) VALUES (?, ?, ?, 50)",
                               (name, roll_number, subject))

    # Add teachers if not already present
    cursor.execute("SELECT COUNT(*) FROM teachers")
    if cursor.fetchone()[0] == 0:
        teachers = [("Physics_T", "Physics"), ("Chemistry_T", "Chemistry"), ("Math_T", "Mathematics")]
        for username, subject in teachers:
            cursor.execute("INSERT OR IGNORE INTO teachers (username, subject) VALUES (?, ?)", (username, subject))

    conn.commit()
    conn.close()

def add_teacher():
    username = input("Enter new teacher's username: ")
    subject = input("Enter subject: ")

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO teachers (username, subject) VALUES (?, ?)", (username, subject))
        conn.commit()
        print(f"Teacher {username} added successfully!")
    except sqlite3.IntegrityError:
        print("Error: This subject or username already exists!")

    conn.close()

def add_student():
    name = input("Enter student name: ")
    roll_number = int(input("Enter roll number: "))

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    subjects = ["Physics", "Chemistry", "Mathematics"]
    for subject in subjects:
        cursor.execute("INSERT OR IGNORE INTO students (name, roll_number, subject, marks) VALUES (?, ?, ?, 50)",
                       (name, roll_number, subject))

    conn.commit()
    conn.close()
    print(f"Student {name} (Roll No: {roll_number}) added successfully!")

def update_marks(teacher_username):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT subject FROM teachers WHERE username = ?", (teacher_username,))
    result = cursor.fetchone()

    if not result:
        print("Teacher not found!")
        return
    
    teacher_subject = result[0]

    while True:
        print(f"\nUpdating marks for {teacher_subject}")

        cursor.execute("SELECT name, roll_number, marks FROM students WHERE subject = ?", (teacher_subject,))
        students = cursor.fetchall()

        for student in students:
            print(f"{student[1]} - {student[0]}: {student[2]} marks")

        roll_number = input("\nEnter Roll Number to update marks (or press Enter to exit): ").strip()
        if not roll_number:
            break

        new_marks = int(input("Enter new marks: ").strip())
        cursor.execute("UPDATE students SET marks = ? WHERE roll_number = ? AND subject = ?", 
                       (new_marks, roll_number, teacher_subject))
        conn.commit()
        print("Marks updated successfully!")

    conn.close()

def finalize_marks():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("UPDATE settings SET value = 1 WHERE key = 'marks_finalized'")
    conn.commit()
    conn.close()
    print("Marks have been finalized!")

def reset_marks():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("UPDATE students SET marks = 50")
    cursor.execute("UPDATE settings SET value = 0 WHERE key = 'marks_finalized'")
    conn.commit()
    conn.close()
    print("Marks have been reset! Students can't see their marks until finalized again.")

import sqlite3

DB_FILE = "marks.db"

def view_student_results():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Check if marks are finalized
    cursor.execute("SELECT value FROM settings WHERE key = 'marks_finalized'")
    is_finalized = cursor.fetchone()[0]

    if is_finalized == 0:
        print("Marks are not finalized yet. Please wait.")
    else:
        cursor.execute("""
            SELECT name, roll_number, SUM(marks) AS total_marks
            FROM students
            GROUP BY roll_number, name
            ORDER BY total_marks DESC
        """)
        students = cursor.fetchall()

        print("\nFinalized Marks (Sorted by Total Marks - Ascending Order):")
        print("-----------------------------------------------------")
        print("| Roll No | Name       | Total Marks |")
        print("-----------------------------------------------------")
        for student in students:
            print(f"| {student[1]:<7} | {student[0]:<10} | {student[2]:<11} |")
        print("-----------------------------------------------------")

    conn.close()


def main():
    init_db()
    
    while True:
        print("\nStudent Marks Management System")
        print("1. Teacher\n2. Student\n3. Add Teacher\n4. Add Student\n5. Finalize Marks\n6. Reset Marks\n7. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            username = input("Enter teacher username: ")
            if username:
                update_marks(username)
        elif choice == "2":
            view_student_results()
        elif choice == "3":
            add_teacher()
        elif choice == "4":
            add_student()
        elif choice == "5":
            finalize_marks()
        elif choice == "6":
            reset_marks()
        elif choice == "7":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
