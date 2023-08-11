#!/usr/bin/node

const request = require('request');
const movieId = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${movieId}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }

    const charactersUrl = JSON.parse(body).characters;
    const charactersName = charactersUrl.map(
      (url) =>
        new promiseHooks((resolve, reject) => {
          request(url, (promiseErr, __, charactersReqBody) => {
            if (promiseErr) {
              reject(promiseErr);
            }
            resolve(JSON.parse(charactersReqBody).name);
          });
        })
    );

    Promise.all(charactersName)
      .then((names) => console.log(names.join('\n')))
      .catch((allErr) => console.log(allErr));
  });
}
