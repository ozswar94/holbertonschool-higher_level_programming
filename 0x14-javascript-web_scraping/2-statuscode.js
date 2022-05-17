#!/usr/bin/node

const axios = require('axios');

axios.get(process.argv[2])
  .then(function (response) {
    // handle success
    console.log('code:', response.status);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed
  });
