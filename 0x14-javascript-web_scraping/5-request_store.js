#!/usr/bin/node

const axios = require('axios');
const fs = require('fs');

axios.get(process.argv[2])
  .then(function (response) {
    fs.writeFile(process.argv[3], response.data, 'utf-8', function (err) {
      if (err) console.log(err);
    });
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed
  });
