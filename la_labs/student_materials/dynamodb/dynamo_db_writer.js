var AWS = require('aws-sdk');
AWS.config.update({region: 'us-east-1'});
var documentClient = new AWS.DynamoDB.DocumentClient();

var csvToJson = require('convert-csv-to-json');

var json = csvToJson.fieldDelimiter(',').getJsonFromCsv("musicData.csv");

for (entry in json) {
    console.log("THIS IS THE ENTRY")
    console.log(json[entry])

    var params = {
        TableName : 'PrometheonMusic',
        Item: json[entry]
    };

    documentClient.put(params, function(err, data) {
        if (err) console.log(err);
        else console.log(data);
    });
    

}