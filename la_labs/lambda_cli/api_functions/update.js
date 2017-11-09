'use strict';

const AWS = require('aws-sdk');
AWS.config.update({region:'us-east-1'});

const dynamoDb = new AWS.DynamoDB.DocumentClient();

module.exports.update = (event, context, callback) => {
  const data = JSON.parse(event.body);

  const params = {
    TableName: 'PrometheonMusic',
    Key: {
      Artist: data.Artist,
      SongTitle: data.SongTitle
    },
    UpdateExpression: "set AlbumTitle=:AlbumTitle, CriticRating=:CriticRating, Genre=:Genre, Price=:Price",
    ExpressionAttributeValues:{
        ":AlbumTitle": data.AlbumTitle,
        ":CriticRating": data.CriticRating,
        ":Genre": data.Genre,
        ":Price": data.Price
    },
    ReturnValues:"UPDATED_NEW"
  };

  // write the item to the database
  dynamoDb.update(params, (error) => {
    // handle potential errors
    if (error) {
      console.error(error);
      callback(null, {
        statusCode: error.statusCode || 501,
        headers: { 'Content-Type': 'text/plain' },
        body: 'Couldn\'t create the item.',
      });
      return;
    }

    // create a response
    const response = {
      statusCode: 200,
      body: JSON.stringify(params.Item),
    };
    callback(null, response);
  });
};