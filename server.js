// ---------------------------------------------- Global Variables ----------------------------------------------

// Importing general libraries.
const fs = require('fs');
const express = require('express');
const cmd = require('node-cmd');

const app = express();

app.use(express.static('website'));

const server = app.listen(process.env.PORT || 3000);

let {PythonShell} = require('python-shell');

// ---------------------------------------------- Create Websocket Server ----------------------------------------------

const { Server } = require('ws');

const wss = new Server({ server });

// ---------------------------------------------- Handle connections ----------------------------------------------
/*
wss.on('connection', (ws) => {
  console.log('Client connected');
  ws.on('close', () => console.log('Client disconnected'));
});
*/
// ---------------------------------------------- Broadcast updates ----------------------------------------------
/*
setInterval(() => {
  wss.clients.forEach((client) => {

    client.send(new Date().toTimeString());
  });
}, 1000);
*/
// ---------------------------------------------- RUN ----------------------------------------------

url = [];
let dataString = '';

// ---------------------------------------------- From Binary to String Function ----------------------------------------------

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

// ---------------------------------------------- Server Receiving Image URL ----------------------------------------------

// Sending data back to interface that resulted from community finding process.
app.get('/run/:url', function (req, res) {

    // ------------------------------
/*
    let options = {
  mode: 'text',
  pythonOptions: ['-u'], // get print results in real-time
  scriptPath: './',
  args: [binaryToString(req.params.url)]
};

PythonShell.run('demo.py', options, function (err, results) {
  if (err) throw err;
  // results is an array consisting of messages collected during execution
  console.log('results: %j', results);
});
*/
    // ------------------------------

    console.log(binaryToString(req.params.url));

    url.push(binaryToString(req.params.url));

    let spawn = require('child_process').spawn;
    let py = spawn('python', ['demo.py', binaryToString(req.params.url)]);

    py.stdin.write(JSON.stringify(url));
    py.stdin.end();

    py.stdout.on('data', function(data){
        dataString = dataString + "hello";
        //console.log("hi");
        //console.log(data);
        dataString += data.toString();
        res.send(dataString);

    });


    py.stdout.on('end', function(){

        console.log(dataString);
        //console.log('Sum of numbers=',dataString);
    });

    //res.send();
/*
    setInterval(() => {
  wss.clients.forEach((client) => {
//dataString = dataString + "hello";
    //client.send(dataString);
      dataString = dataString +  "hello";
    client.send(dataString);
    console.log(dataString)
  });
}, 1000);
*/
});

/*

*/
    //  ----------------------------



    // ----------------------------------------------

/*
app.get('/', (req, res) => {
  console.log(req.query)
});

 */
/*
app.get('/run2/:url', function (req, res) {

    res.send(dataString)

});
*/
