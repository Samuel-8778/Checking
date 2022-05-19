from flask import request, jsonify
from app.config import logger
from app.models import Employee, Person, Address, db
from app import app
import uuid


@app.route('/add_emp', methods=['POST'])
def emp_test():
    try:

        data = request.json
        if request.method == 'POST':
            position = data['position']
            add_emp = Employee(position=position, emp_code=str(uuid.uuid4()))
            db.session.add(add_emp)
            db.session.commit()
            return jsonify({'message': 'ADD Session Success'})
        logger.debug("New employee Added")
    except:
        raise KeyError("Some errors on your key values")

    logger.warning("Add Employee session failed")


@app.route('/add_per', methods=['POST'])
def per_test():
    try:
        data = request.json
        if request.method == 'POST':
            name = data['name']
            age = data['age']
            employee_id = data['employee_id']
            add_per = Person(name=name, age=age, employee_id=employee_id)
            db.session.add(add_per)
            db.session.commit()
            return jsonify({'message': 'Person added'})
        logger.debug("New Person Added")
    except :

        raise ValueError("Some Errors on your values")


@app.route('/add_add', methods=['POST'])
def add_test():
    try:

        data = request.json
        if request.method == 'POST':
            role = data['role']
            employee_id = data['employee_id']
            add_per = Address(role=role, employee_id=employee_id)
            db.session.add(add_per)
            db.session.commit()
            return jsonify({'message': 'Address added'})
        logger.debug("New Address Added")

    except:
        raise SyntaxError("Some Errors involved on your Syntax")
    logger.warning("Add Address session failed")


if __name__ == '__main__':
    app.run(debug=True)
