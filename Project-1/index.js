const express = require('express');
const redis = require('redis');

const app = express();

const client = redis.createClient(6379, 'redis-server');

client.on('connect', function () {
  console.log('Connected to Redis');
});

client.on('error', function (err) {
  console.log('Redis error:', err);
});

app.get('/', (req, res) => {
  client.get('visits', (err, visits) => {
    if (err) {
      return res.send('Error connecting to Redis');
    }

    if (visits === null) {
      visits = 0;
    }

    client.set('visits', parseInt(visits) + 1);

    res.send('Number of visits is ' + visits);
  });
});

app.listen(8081, () => {
  console.log('Listening on port 8081');
});
