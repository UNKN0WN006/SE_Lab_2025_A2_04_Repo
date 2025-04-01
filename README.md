# Software Engineering Lab, 2025
## Assignment on Version Control Using Git

### Assignment-4

This repository contains three projects developed as part of the Software Engineering Lab assignment for the year 2025. Each project is implemented in a separate branch, and Git is used for version control to track changes and maintain history.

---

## Projects Overview

### 1. Inventory Management System with Git (Branch: Q1)
- **Description**: This project is designed to manage products for a store. Customers can make purchases, and sellers can update the list of products.
- **Features**:
  - Add, update, and view products.
  - Customers can search for products and make purchases.
  - Maintains a purchase history of items.
- **Technologies Used**: Python, SQLite, Git

### 2. Marks Management System with Git (Branch: Q2)
- **Description**: This project is a Student Marks Management System that uses Git for version control.
- **Features**:
  - A central database stores students' marks for different subjects in a tabular format.
  - Subject teachers can update marks as needed before the final submission.
  - Teachers can view student names and roll numbers but can only edit the marks for their subject.
  - Once all teachers have completed their updates, the database is sorted by total marks and made available for students to view.
- **Technologies Used**: Python, SQLite, Git

### 3. Task Management CLI Tool (Branch: Q3)
- **Description**: This project is a command-line task management tool where users can add, edit, and complete tasks.
- **Features**:
  - Users can add new tasks, edit existing tasks, and mark tasks as complete.
  - Implements version control to track task changes and provide a task history.
- **Technologies Used**: Python, Git

---

## Accessing the Projects

To access the individual projects, follow these steps:

1. **Clone the Repository**:
   Open your terminal and run the following command to clone the repository:
   ```bash
   git clone https://github.com/hembramsushar/SE_Lab_2025_A2_04_Repo.git
   ```
2. **Navigate to the Project Directory**:
   Change into the project directory:
    ```bash
    cd SE_Lab_2025_A2_04_Repo
    ```
3. **Checkout the Desired Branch**:
   Use the following commands to switch to the branch of the project you want to work on:
   
      - For the Inventory Management System:
        ```bash
        git checkout Q1
        ```
      - For the Marks Management System
        ```bash
        git checkout Q2
        ```
      - For the Task Management CLI Tool:
        ```bash
        git checkout Q3
        ```
4. **Run the Project**:
   Follow the instructions in the respective project directories to set up and run the projects. Each project may have its own README.md file with specific setup instructions.


## Version Control ##
  This repository uses Git for version control. Make sure to commit your changes with meaningful messages and push them to the respective branches. To commit changes, use the following commands:
  ```bash
  git add .
  git commit -m "Your commit message here"
  git push origin branch-name
  ```
# License #
This project is licensed under the Apache License 2.0. See the LICENSE file for more details.

## Acknowledgments ##
[Sushar Hembram](https://github.com/hembramsushar) - Creator of the Github repo and alloted Q1

[Priyanshu Dan](https://github.com/Priyanshu-Dan) - Alloted Q2

[Anay Saha](https://github.com/AnaySaha2005) - Alloted Q3
