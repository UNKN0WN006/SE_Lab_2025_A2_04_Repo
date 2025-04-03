# Student Marks Management System

## Project Overview
The Student Marks Management System is a Python application designed to facilitate the management of student marks across various subjects. This system allows teachers to update marks, finalize them, and enables students to view their total marks once finalized. The application uses SQLite as the database to store information and Git for version control.

## Features
- **Central Database**: Stores students' marks for different subjects in a structured format.
- **Teacher Functionality**: Teachers can update marks for their respective subjects and finalize them.
- **Student Functionality**: Students can view their total marks after all subjects have been finalized.
- **User  Authentication**: Simple username and password authentication for teachers.

## Technologies Used
- **Python**: The programming language used to develop the application.
- **SQLite**: A lightweight database used to store student and teacher information.
- **Git**: A version control system used to manage code changes and collaboration.

## Setup Instructions

### Prerequisites
- **Python 3.x**: Ensure Python is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
- **SQLite3**: This comes pre-installed with Python. You can check if it's available by running `sqlite3` in your terminal.
- **Git**: Install Git from [git-scm.com](https://git-scm.com/downloads) if you haven't already.

### Cloning the Repository
1. Open your terminal or command prompt.
2. Clone the repository using the following command:
   ```bash
   git clone https://github.com/hembramsushar/SE_Lab_2025_A2_04_Repo.git
   ```
3. Navigate to the project directory:
   ```bash
    cd SE_Lab_2025_A2_04_Repo
    ```
### Running the Application

- **Step 1**: Running the Database
The application will automatically create the marks.db database file when you run the Python script for the first time. You do not need to run any separate commands to create the database.

- **Step 2**: Running the Python Script
Ensure you have the marks_management.py file in your project directory.
Open your terminal or command prompt.
Run the application using the following command:
```bash
python marks_management.py
```
## Initial Database Setup

The first time you run the application, it will initialize the database and populate it with sample data for students and teachers. The default usernames and passwords for teachers are as follows:
- **Physics Teacher**: **Physics_T** with password **Physics_T123**
- **Chemistry Teacher**: **Chemistry_T** with password **Chemistry_T123**
- **Math Teacher**: **Math_T** with password **Math_T123**

### Version Control with Git

# Committing Changes
After making changes, you can commit them using:
```bash
git add .
git commit -m "Your commit message"
```
# Pushing Changes
Push your changes to the remote repository:
```bash
git push origin Q2
```

## Modifying the Database Using SQLite3
To change the database using SQLite3 with the marks.db file, follow these structured steps:

### 1. Open the SQLite Command Line Interface
Open your terminal or command prompt.
Start the SQLite command line interface with the database:
```bash
sqlite3 marks.db
```
### 2. Viewing Tables in the Database
To see the tables in the database, run:
```sql
.tables
```
### 3. Viewing Table Structure
To view the structure of a specific table (e.g., students or teachers), use:
```sql
.schema students
```
#### or
```sql
.schema teachers
```
### 4. Querying Data
To view the data in a table, use a SELECT statement. For example, to view all students:
```sql
SELECT * FROM students;
```
### 5. Inserting New Data
To add a new student, use the INSERT statement. For example:
```sql
INSERT INTO students (name, roll_number, subject, marks) VALUES ('New Student', 111, 'Physics', 75);
```
### 6. Updating Existing Data
To update a student's marks, use the UPDATE statement. For example:
```sql
UPDATE students SET marks = 85 WHERE roll_number = 101 AND subject = 'Physics';
```
### 7. Deleting Data
To delete a student record, use the DELETE statement. For example:
```sql
DELETE FROM students WHERE roll_number = 111;
```
### 8. Committing Changes
If you are making changes that require a transaction, ensure to commit your changes:
```sql
COMMIT;
```
### 9. Exiting SQLite
To exit the SQLite command line interface, type:
```sql
.exit
```
## Inserting New Teachers
To insert new teachers into your SQLite database (assuming you have a table for teachers), follow these steps:

**Open SQLite3**:

First, open your SQLite3 command line interface and connect to your database:
```bash
sqlite3 marks.db
```
**Check the Structure of the Teachers Table**:

Before inserting data, check the structure of the teachers table:
```sql
.schema teachers
```
**Insert New Teachers**:

Assuming your teachers table has the following columns: id, name, subject, and email, you can insert a new teacher using the INSERT INTO statement. Here’s an example:
```sql
INSERT INTO teachers (id, name, subject, email) VALUES (1, 'John Doe', 'Mathematics', 'john.doe@example.com');
```
**Inserting Multiple Teachers**:

To insert multiple teachers at once, you can do so in a single INSERT statement:
```sql
INSERT INTO teachers (username, subject, finalized) VALUES ('Bioinformatics_T', 'Bioinformatics', 0)
```
**Verify the Insertion**:

To verify that the new teachers have been added, you can run a SELECT query:
```sql
SELECT * FROM teachers;
```
**Exiting SQLite**:

Once you are done, you can exit the SQLite command line interface by typing:
```sql
.exit
```
## By following these steps, you can successfully insert new teachers into your SQLite database. Adjust the column names and values as necessary to fit your specific database schema.

## Conclusion
This Student Marks Management System provides a straightforward way for teachers to manage student marks and for students to view their performance. Follow the setup instructions to get started, and refer to the function descriptions for a better understanding of the code structure. If you encounter any issues, please check the code for any errors or consult the documentation for further assistance. Happy coding!
