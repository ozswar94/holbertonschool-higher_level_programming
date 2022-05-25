#!/usr/bin/node

const axios = require('axios');
const dictTrue = {};

axios.get(process.argv[2])
  .then(function (response) {
    for (let i = 0; i < response.data.length; i++) {
      if (response.data[i].completed) {
        if (!(response.data[i].userId in dictTrue)) { dictTrue[response.data[i].userId] = 0; }
        dictTrue[response.data[i].userId] += 1;
      }
    }
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    console.log(dictTrue);
  });
