
<<<<<<< Q3
# Project Title: Task CLI

## Overview

This project is a command-line interface (CLI) tool built with Node.js. It allows users to perform various tasks efficiently through a simple command-line interface. The project utilizes several npm packages to enhance functionality and improve user experience.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Node.js**: You need to have Node.js installed on your machine. You can download it from [nodejs.org](https://nodejs.org/).
- **npm**: npm (Node Package Manager) is included with Node.js. You can check if you have it installed by running `npm -v` in your terminal.

## Getting Started

Follow these steps to set up your project locally:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/hembramsushar/SE_Lab_2025_A2_04_Repo.git
   cd SE_Lab_2025_A2_04_Repo
   ```
2. **Proced to the TASK_CLI folder**

   ```bash
   cd TASK_CLI
   ```

3. **Install the dependencies(most crucial part)**

   ```bash
   npm i
   ```
   This installs all the npm dependencies in the project folders from **.json** and stores them in a folder titled **node_modules**

4. **Run the program**

   ```bash
   node task-cli.js
   ```
   It lists all the commands present and can be done while running the program

## Using the CLI Tool

- After starting the tool, you can use the following commands:
  - Get help if you are unable to do it :
    ```bash
    node task-cli.js help
    ```
    This lists all the commands that can be run inside the terminal or the program  
  - Add a new task:
    ```bash
    node task-cli.js add Your_Task_Here
    ```
    By default the tasks are turned not completed as the requirement of the Task mangement for the CLI tool

  - List all tasks:
    ```bash
    node task-cli.js list
    ```
    Lists all the tasks available and stored inside the program

  - Complete a task
    ```bash
    node task-cli.js complete <task-id>
    ```
    Marks them complete by giving a ✔ instead of a **X** symbol beside them while listing them.

  - Edit a task
    ```bash
    node task-cli.js edit <task-id> New_task
    ```
    This edits the tasks mentioned earlier or given earlier.

  - Delete a task
    ```bash
    node task-cli.js delete <task-id>
    ```
    This deletes that task from the list of tasks that can be seen after running the ```  node task-cli.js list ``` command.


  ## Version Control
    If you want to implement version control for tracking task changes, consider using a version control system like Git. You can commit changes to your tasks and maintain a history of modifications.

  # Conclusion
  By following these steps, you should be able to successfully run and use the Task Management CLI Tool. Enjoy managing your tasks!
=======
>>>>>>> main



Usage: task-cli [options] [command]
 
Options:
  -h, --help           display help for command
 
Commands:
  add [task]            Add a new task
	
  list                  List all tasks
	
  complete [id]         Mark a task as complete
	
  edit [id] [newTask]  	 Edit an existing task
	
  delete [id]         	 Delete an existing task
	
  help [command]       	display help for command
