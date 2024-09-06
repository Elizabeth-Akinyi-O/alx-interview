#!/usr/bin/node
/**
 * Star Wars Characters
 */
const request = require('request');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.log('Usage: ./star_wars_characters.js <movieId>');
  process.exit(1);
}

const movieURL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Function to print the characters recursively
const printMovieCharacter = function (urls, i) {
  if (i >= urls.length) {
    return; // Base case: stop if all characters are printed
  }

  request(urls[i], (err, res, body) => {
    if (err) {
      console.log(err);
      return;
    }
    try {
      const character = JSON.parse(body);
      console.log(character.name);
    } catch (err) {
      console.log('Error parsing character data:', err);
    }

    // Recursive call to print the next character
    printMovieCharacter(urls, i + 1);
  });
};

// Make a request to get the movie details
request(movieURL, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  try {
    const characters = JSON.parse(body).characters;
    printMovieCharacter(characters, 0); // Start printing characters from index 0
  } catch (err) {
    console.log('Error parsing movie data:', err);
  }
});
