const empolyeeModel = require("./model");


const getEmployee = async (request, response) => {
    try {
        const employee = await empolyeeModel.getEmployee();
        try {
            response.status(200).send(JSON.stringify(employee));
        } catch (err) {
            // show error?
        }
    } catch (err) {
        response.status(200).send(
            JSON.stringify({
                error: true,
                message: err.toString()
            })
        );
    }
};

const editEmployee = async (request, response) => {
    try {
        const result = await empolyeeModel.editEmployee(request.params.id);

        try {
            response.status(200).send(JSON.stringify(result));
        } catch (err) {
            // show error?
        }
    } catch (err) {
        response.status(200).send(
            JSON.stringify({
                error: true,
                message: err.toString()
            })
        );
    }
};

const addEmployee = async (request, response) => {
    try {
        const result = await empolyeeModel.addEmployee(request.body.values);

        try {
            response.status(200).send(JSON.stringify(result));
        } catch (err) {
            // show error?
        }
    } catch (err) {
        response.status(200).send(
            JSON.stringify({
                error: true,
                message: err.toString()
            })
        );
    }
};


const modifyEmployee = async (request, response) => {
    try {
        const result = await empolyeeModel.modifyEmployee(request.body.values,request.params.id);
        try {
            response.status(200).send(JSON.stringify(result));
        } catch (err) {
            // show error?
        }
    } catch (err) {
        response.status(200).send(
            JSON.stringify({
                error: true,
                message: err.toString()
            })
        );
    }
};


const deleteEmployee = async (request, response) => {
    try {
        const result = await empolyeeModel.deleteEmployee(request.params.id);
        try {
            response.status(200).send(JSON.stringify(result));
        } catch (err) {
            // show error?
        }
    } catch (err) {
        response.status(200).send(
            JSON.stringify({
                error: true,
                message: err.toString()
            })
        );
    }
};

 
 



module.exports = {
    getEmployee,
    addEmployee,
    deleteEmployee,
    modifyEmployee,
    editEmployee
};
