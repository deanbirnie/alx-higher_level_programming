#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  }

  try {
    const tasks = JSON.parse(body);
    const tasksCompleted = {};

    tasks.forEach(task => {
      if (task.completed) {
        const userId = task.userId;
        tasksCompleted[userId] = (tasksCompleted[userId] || 0) + 1;
      }
    });

    console.log(tasksCompleted);
  } catch (e) {
    console.error(e);
  }
});
