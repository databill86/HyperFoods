// ---------------------------------------------- Global Variables ----------------------------------------------

// Importing general libraries.
const fs = require('fs');
const express = require('express');
const cmd = require('node-cmd');

const app = express();

app.use(express.static('website'));
app.listen(process.env.PORT || 3000);

// ---------------------------------------------- RUN ----------------------------------------------

url = [];
let dataString = '';

function binaryToString(str) {
    // Removes the spaces from the binary string
    str = str.replace(/\s+/g, '');
    // Pretty (correct) print binary (add a space every 8 characters)
    str = str.match(/.{1,8}/g).join(" ");

    let newBinary = str.split(" ");
    let binaryCode = [];

    for (let i = 0; i < newBinary.length; i++) {
        binaryCode.push(String.fromCharCode(parseInt(newBinary[i], 2)));
    }

    return binaryCode.join("");
}

// Sending data back to interface that resulted from community finding process.
app.get('/run/:url', function (req, res) {

    console.log(binaryToString(req.params.url));

    url.push(binaryToString(req.params.url));

    let spawn = require('child_process').spawn;
    let py = spawn('python', ['demo.py', binaryToString(req.params.url)]);

    py.stdin.write(JSON.stringify(url));
    py.stdin.end();

    py.stdout.on('data', function(data){
        console.log("hi");
        console.log(data);
        dataString += data.toString();
        res.send();

    });


    py.stdout.on('end', function(){

        console.log(dataString);
        console.log('Sum of numbers=',dataString);
    });

});

app.get('/', (req, res) => {
  console.log(req.query)
});
/*
app.get('/run2/:url', function (req, res) {

    res.send(dataString)

});
*/
