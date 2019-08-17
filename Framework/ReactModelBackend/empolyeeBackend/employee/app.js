let mysql = require('mysql');
let config = require('../config.js');

let connection = mysql.createPool(config);

connection.getConnection(function(err) {
  if (err) {
    return console.error('error: ' );
  }
  console.log('Connected to the MySQL server.');
});

module.exports = {
	getClientFromPool: () => {
		return connection;
	}
};

