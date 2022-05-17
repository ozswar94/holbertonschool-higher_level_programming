#!/usr/bin/node

const axios = require('axios');
const path = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

axios.get(path)
  .then(function (response) {
    console.log(response.data.title);
  })
  .catch(function (error) {
    console.log(error);
  })
  .then(function () {
  // always executed
  });
