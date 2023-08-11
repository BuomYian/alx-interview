#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

  request(apiUrl, (err, _, body) => {
    if (err) {
      console.log(err);
      return;
    }

    const charactersUrl = JSON.parse(body).characters;
    const charactersName = charactersUrl.map(
      (url) =>
        new Promise((resolve, reject) => {
          request(url, (promiseErr, __, charactersReqBody) => {
            if (promiseErr) {
              reject(promiseErr);
              return;
            }
            resolve(JSON.parse(charactersReqBody).name);
          });
        })
    );

    Promise.all(charactersName)
      .then((names) => console.log(names.join('\n')))
      .catch((allErr) => console.log(allErr));
  });
} else {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
}
