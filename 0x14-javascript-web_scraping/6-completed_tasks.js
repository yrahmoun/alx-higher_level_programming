#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const tasksCompleted = {};
    data.forEach(task => {
      if (task.completed) {
        if (tasksCompleted[task.userId]) {
          tasksCompleted[task.userId]++;
        } else {
          tasksCompleted[task.userId] = 1;
        }
      }
    });
    console.log(tasksCompleted);
  }
});
