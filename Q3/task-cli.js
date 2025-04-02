const { Command } = require("commander");
const { execute, fetchAll ,fetchFirst} = require("./sql.js");
const program = new Command();
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

// List Tasks
program
  .command("list")
  .description("List all tasks")
  .action(async () => {
    try {
      const tasks = await fetchAll(`SELECT * FROM TASKS`);
      tasks.forEach((t) => {
        console.log(
          `Id:${t.id} | Task: ${t.task} | Checked ${
            t.completed == 1 ? "✔" : "✖"
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
  .action(async(id, newTask) => {
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
  .action(async(id) => {
    try {
        const task=await fetchFirst(`SELECT * FROM TASKS WHERE id=${id}`);
        if(!task) console.log("Task id doesn't exist!!")
            else{
          await execute("DELETE FROM tasks WHERE id ="+id).then(()=>console.log("Task Deleted!!!"))
        }
      } catch (e) {
        console.log(e);
      }
  });
// Run CLI
program.parse(process.argv);
