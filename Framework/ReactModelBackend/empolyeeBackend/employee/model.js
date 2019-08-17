const MysqlConnector = require("./app");
var Promise = require('promise');
var moment = require ('moment')

module.exports = {

    getEmployee: async( obj)=>{
        var client = null;
        try {
            client = await MysqlConnector.getClientFromPool();
        } catch (err) {
            throw err;
        }
       
        return new Promise((resolve, reject) => {
            client.query(`SELECT * from employee`,  function(err, result) {
            // client.end()
               
                if (err) {
                    return reject(err);
                }
                resolve(result)

            })
        })
    },

    editEmployee: async( id )=>{
        var client = null;
        try {
            client = await MysqlConnector.getClientFromPool();
        } catch (err) {
            throw err;
        }
       
        return new Promise((resolve, reject) => {
            let editQuery = "SELECT * from employee where id = ?";
            client.query(editQuery, [id], function(err, result) {
            // client.end()
                
                if (err) {
                    return reject(err);
                }
                resolve(result)

            })
        })
    },


    addEmployee: async (obj) => {
        var client = null;
        try {
            client = await MysqlConnector.getClientFromPool();
        } catch (err) {
            throw err;
        }
        return new Promise((resolve, reject) => {
            let sql = "INSERT INTO employee (name, current_address, communication_address, doj) VALUES ?";


            let values = [
                [obj.name, obj.present_address, obj.communication_address, moment(obj.doj).format('YYYY-MM-DD')],
            ];
                client.query(sql, [values], (err, result) =>  {
                // client.end()
                
                if (err) {
                    return reject(err);
                }
                resolve(result)
            })

        })
    },
    deleteEmployee: async (id) => {
        var client = null;
        try {
            client = await MysqlConnector.getClientFromPool();
        } catch (err) {
            throw err;
        }
        return new Promise((resolve, reject) => {
            let deleteQuery = "DELETE from employee where id = ?";
         
            client.query(deleteQuery, [id],  function(err, result) {
            // client.end()
                
                if (err) {
                    return reject(err);
                }
                resolve(result)
            })

        })
    },
    modifyEmployee: async (obj, id) => {
        var client = null;
        try {
            client = await MysqlConnector.getClientFromPool();
        } catch (err) {
            throw err;
        }

        return new Promise((resolve, reject) => {
            client.query('UPDATE employee SET name =?, current_address= ?, communication_address=?, doj=? WHERE id=?',  [obj.name, obj.present_address, obj.communication_address, moment(obj.doj).format('YYYY-MM-DD'), id],  function(err, result) {
            // client.end()
                
                if (err) {
                    return reject(err);
                }
                resolve(result)
            })

        })
    }
}