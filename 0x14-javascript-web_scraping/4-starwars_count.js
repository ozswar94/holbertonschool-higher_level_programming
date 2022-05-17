#!/usr/bin/node

const axios = require('axios');
let count = 0;

axios.get(process.argv[2])
  .then(function (response) {
    response.data.results.forEach(element => {
      for (let i = 0; i < element.characters.length; i++) {
        if (element.characters[i] === 'https://swapi-api.hbtn.io/api/people/18/') { count++; }
      }
    });
  })
  .catch(function (error) {
    console.log(error);
  })
  .then(function () {
    console.log(count);
  });
