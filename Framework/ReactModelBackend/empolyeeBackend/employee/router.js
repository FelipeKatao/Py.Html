const express = require("express");
const router = express.Router();
const empolyeeController = require("./controller");

// get employees detailes 

router.get('/getEmployee', empolyeeController.getEmployee)

//add new employee

router.post('/addEmployee', empolyeeController.addEmployee)

// remove employee

router.delete('/removeEmployee/:id', empolyeeController.deleteEmployee)

// modify employee

router.put('/modifyEmployee/:id', empolyeeController.modifyEmployee)

// edit empolyee

router.get('/editEmployee/:id', empolyeeController.editEmployee)

module.exports = router;