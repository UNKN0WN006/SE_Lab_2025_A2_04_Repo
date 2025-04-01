import sqlite3
import getpass

DB_FILE = "marks.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    #Creating Students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            roll_number INTEGER,
            subject TEXT,
            marks INTEGER
        )
    ''')
    
    # Creating teachers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            subject TEXT,
            finalized INTEGER DEFAULT 0  -- 0 = Not Finalized, 1 = Finalized
        )
    ''')

    # First addtion of Students
    cursor.execute("SELECT COUNT(*) FROM students")
    if cursor.fetchone()[0] == 0:
        students = [
            (101, "Priyanshu"), (102, "Ravi"), (103, "Narendar"), (104, "Rahul"),
            (105, "Aurobindo"), (106, "John"), (107, "Jack"), (108, "Amir"),
            (109, "Ivy"), (110, "Jim")
        ]
        subjects = ["Physics", "Chemistry", "Mathematics"]

        for roll_number, name in students:
            for subject in subjects:
                cursor.execute("INSERT INTO students (name, roll_number, subject, marks) VALUES (?, ?, ?, 50)",
                               (name, roll_number, subject))

    # First addition of teachers 
    cursor.execute("SELECT COUNT(*) FROM teachers")
    if cursor.fetchone()[0] == 0:
        teachers = [("Physics_T", "Physics"), ("Chemistry_T", "Chemistry"), ("Math_T", "Mathematics")]
        for username, subject in teachers:
            cursor.execute("INSERT INTO teachers (username, subject, finalized) VALUES (?, ?, 0)", (username, subject))

    conn.commit()
    conn.close()

# Auth function
def authenticate():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    # Password Matching
    if password == f"{username}123":
        return username
    else:
        print("Invalid credentials!")
        return None

# Updatation on marks
def teacher_menu(teacher_username):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT subject FROM teachers WHERE username = ?", (teacher_username,))
    teacher_subject = cursor.fetchone()

    if not teacher_subject:
        print("Teacher not found!")
        conn.close()
        return

    teacher_subject = teacher_subject[0]

    while True:
        print(f"\nWelcome {teacher_username} - You can update marks for {teacher_subject}")

        # Student List for teachers
        cursor.execute("SELECT id, name, roll_number, marks FROM students WHERE subject = ?", (teacher_subject,))
        students = cursor.fetchall()

        if not students:
            print(f"No students found for {teacher_subject}!")
            conn.close()
            return

        print("\nStudents:")
        for student in students:
            print(f"{student[1]} (Roll: {student[2]}) - Marks: {student[3]}")
        
        roll_number = input("\nEnter Roll Number to update marks (or press Enter to skip): ").strip()
        if roll_number:
            new_marks = input("Enter new marks: ").strip()
            cursor.execute("UPDATE students SET marks = ? WHERE roll_number = ? AND subject = ?", 
                        (new_marks, roll_number, teacher_subject))
            print("Marks updated successfully!")

        #Finalization
        finalize = input("\nDo you want to finalize marks for this subject? (yes/no): ").strip().lower()
        if finalize == "yes":
            cursor.execute("UPDATE teachers SET finalized = 1 WHERE username = ?", (teacher_username,))
            print(f"Marks for {teacher_subject} have been finalized!")

        conn.commit()

        choice = input("\nDo you want to continue updating marks? (yes/no): ").strip().lower()
        if choice != "yes":
            break

    conn.close()

# Finalization check
def all_subjects_finalized():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM teachers WHERE finalized = 0")
    count = cursor.fetchone()[0]
    conn.close()
    return count == 0

# Sorting a/c to total marks
def student_menu():
    while True:
        if not all_subjects_finalized():
            print("\nMarks are not finalized yet! Please wait for all subjects to be updated.")
        else:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            
            # Sort by total marks before displaying
            cursor.execute("""
                SELECT name, roll_number, SUM(marks) AS total_marks
                FROM students
                GROUP BY roll_number
                ORDER BY total_marks DESC
            """)
            students = cursor.fetchall()
            
            print("\nSorted Marks (Total):")
            for student in students:
                print(f"{student[0]} (Roll: {student[1]}) - Total Marks: {student[2]}")
            
            conn.close()

        choice = input("\nDo you want to log in again or exit? (yes to continue, no to exit): ").strip().lower()
        if choice != "yes":
            break

# main funcion
def main():
    init_db()
    
    while True:
        print("\nWelcome to Student Marks Management System")
        print("1. Teacher\n2. Student\n3. Exit")
        user_type = input("Enter your choice: ").strip()

        if user_type == "3":
            print("Exiting the system. Goodbye!")
            break

        username = authenticate()
        if username:
            if user_type == "1":
                teacher_menu(username)
            elif user_type == "2":
                student_menu()
            else:
                print("Invalid option!")

if __name__ == "__main__":
    main()
