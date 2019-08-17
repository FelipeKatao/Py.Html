const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const app = express();
const http = require('http').Server(app);

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(cors());

app.use('/employee', require('./employee/router'));


http.listen(4000, function () {
    console.log('listening on *:', 4000);
});


