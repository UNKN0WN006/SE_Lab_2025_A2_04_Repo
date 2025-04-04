/*        IMPORTANT
    CREATE A package.json file and insert:
    
    {
    "dependencies": {
        "commander": "^13.1.0",
        "sqlite3": "^5.1.7"
    },
    "scripts": {
      "start": "node task-cli.js"
    }
  }
    ONLY THEN IT WILL WORK
    INSTALL npm PACKAGE
    USE npm install COMMAND FIRST
    THEN INSTALL NODEJS
    USE node <filename> to start
*/
const { Command } = require("commander");
const program = new Command();
const sqlite3 = require('sqlite3')
//Initialize table in Database if not exists
const execute = async (sql) => {
  const db = new sqlite3.Database("task.db", sqlite3.OPEN_READWRITE);
  return new Promise((resolve, reject) => {
    db.exec(sql, (err) => {
      if (err) reject(err);
      resolve();
    });
    db.close();
  });
};
const fetchAll = async (sql) => {
  const db = new sqlite3.Database("task.db", sqlite3.OPEN_READWRITE);
  return new Promise((resolve, reject) => {
    db.all(sql, (err, rows) => {
      if (err) reject(err);
      resolve(rows);
    });
    db.close();
  });
};
const fetchFirst = async (sql) => {
  const db = new sqlite3.Database("task.db", sqlite3.OPEN_READWRITE);
  return new Promise((resolve, reject) => {
    db.get(sql, (err, row) => {
      if (err) reject(err);
      resolve(row);
    });
    db.close();
  });
};
// Add Task
program
  .command("add <task>")
  .description("Add a new task")
  .action(async (task) => {
    try {
      await execute(`INSERT INTO TASKS(task) VALUES("${task}")`);
    } catch (e) {
      console.log(e);
    }
  });
const main = async () => {
  try {
    await execute(
      `CREATE TABLE IF NOT EXISTS tasks (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          task TEXT NOT NULL,
          completed BOOLEAN  DEFAULT FALSE)`
    );
  } catch (error) {
    console.log(error);
  }
};
main();

// List Tasks
program
  .command("list")
  .description("List all tasks")
  .action(async () => {
    try {
      const tasks = await fetchAll(`SELECT * FROM TASKS`);
      tasks.forEach((t) => {
        console.log(
          `Id:${t.id} | Task: ${t.task} | Checked ${t.completed == 1 ? "✔" : "✖"
          }`
        );
      });
    } catch (e) {
      console.log(e);
    }
  });

// Complete Task
program
  .command("complete <id>")
  .description("Mark a task as complete")
  .action(async (id) => {
    try {
      await execute(`UPDATE tasks SET completed=1 WHERE id=${id}`).then(() =>
        console.log("Task Updated!!!")
      );
    } catch (e) {
      console.log(e);
    }
  });

// Edit Task
program
  .command("edit <id> <newTask>")
  .description("Edit an existing task")
  .action(async (id, newTask) => {
    try {
      await execute(`UPDATE tasks SET task="${newTask}",completed=0 WHERE id=${id}`).then(() =>
        console.log("Task Edited!!!")
      );
    } catch (e) {
      console.log(e);
    }
  });
//Delete Task
program
  .command("delete <id>")
  .description("Delete an existing task")
  .action(async (id) => {
    try {
      const task = await fetchFirst(`SELECT * FROM TASKS WHERE id=${id}`);
      if (!task) console.log("Task id doesn't exist!!")
      else {
        await execute("DELETE FROM tasks WHERE id =" + id).then(() => console.log("Task Deleted!!!"))
      }
    } catch (e) {
      console.log(e);
    }
  });
// Run CLI
program.parse(process.argv);
