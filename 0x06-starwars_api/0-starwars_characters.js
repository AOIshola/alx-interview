#!/usr/bin/node

const request = require('request');
const { promisify } = require('util');

const requestPromise = promisify(request);

const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a Movie ID as a positional argument.');
  process.exit(1);
}

const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

async function fetchAndPrintCharacters (characters) {
  try {
    const promises = characters.map(characterUrl => requestPromise({ url: characterUrl, json: true }));
    const responses = await Promise.all(promises);

    responses.forEach(response => {
      console.log(response.body.name);
    });
  } catch (error) {
    console.error(error);
  }
}

async function fetchMovieDetails () {
  try {
    const response = await requestPromise({ url: filmUrl, json: true });
    const characters = response.body.characters;
    fetchAndPrintCharacters(characters);
  } catch (error) {
    console.error(`Failed to fetch movie details: ${error.message}`);
  }
}

fetchMovieDetails();
