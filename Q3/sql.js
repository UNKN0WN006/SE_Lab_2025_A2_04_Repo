const sqlite3=require('sqlite3')
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
        db.all(sql, (err,rows) => {
          if (err) reject(err);
          resolve(rows);
        });
        db.close();
      });
    };
    const fetchFirst = async (sql) => {
      const db = new sqlite3.Database("task.db", sqlite3.OPEN_READWRITE);
        return new Promise((resolve, reject) => {
          db.get(sql, (err,row) => {
            if (err) reject(err);
            resolve(row);
          });
          db.close();
        });
      };
  module.exports={execute,fetchAll,fetchFirst};