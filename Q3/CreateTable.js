
const  execute = require("./sql.js")
//Initialize table in Database if not exists
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