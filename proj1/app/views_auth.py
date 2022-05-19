from app import app
from functools import wraps
from flask import request, jsonify
import jwt
from app.config import logger
from app.models import Employee, Person, Address, db
from datetime import datetime, timedelta


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({"message": "Please enter your admin-token"})
        try:
            data = jwt.decode(token, options={"verify_signature": False})
            admin_data = Employee.query.filter_by(emp_code=data['emp_code']).all()
        except:
            return jsonify({"message": "token Invalid"})
        return func(admin_data, *args, **kwargs)

    return decorated


@app.route('/emp_all/<int:page_num>', methods=['GET'])
@token_required
def user_all(admin_data, page_num):
    logger.info("Admin Entered")
    employees = Employee.query.paginate(per_page=3, page=page_num)
    output = []
    for emp in employees.items:
        output.append({
            "position": emp.position,
            "emp_code": emp.emp_code
        })
    return jsonify({'Employees': output})


@app.route('/admin_log', methods=['POST'])
def ad_log():
    logger.info("Admin login")
    data = request.json
    if not data['position'] or not data['emp_code']:
        return jsonify({"message": " Please, Enter name and emp_code"})
    elif "Admin" != data['position']:
        logger.warning("You are not eligible for this session")
        return jsonify({"message": "Unauthorised Person"})
    user = Employee.query.filter_by(position=data['position']).first()
    if not user:
        return jsonify('First you have to join')
    else:
        logger.info("Admin has to create token")
        token = jwt.encode({
            'emp_code': user.emp_code,
            'exp': datetime.utcnow() + timedelta(seconds=10)
        }, app.config['SECRET_KEY'])
        return jsonify({'Token': token})


@app.route('/per_all/<int:page_num>', methods=['GET'])
@token_required
def get_emp(admin_data, page_num):
    try:
        if request.method == 'GET':
            user = Person.query.paginate(per_page=2, page=page_num)
            output = []
            for users in user:
                output.append({
                    "id": users.id,
                    "name": users.name,
                    "age": users.age,
                    "employee_id": users.employee_id

                })
                return jsonify({"Persons": output})
    except:
        return jsonify({"message": "Some error in getting employees"})


@app.route('/add_all/<int:page>', methods=['GET'])
@token_required
def add_all(admin_data, page):
    try:
        if request.method == 'GET':
            user = Address.query.paginate(per_page=2, page=page)
            output = []
            for users in user:
                output.append({
                    "role": users.role,
                    "employee_id": users.employee_id
                })
                return jsonify({"Persons": output})
    except:
        return jsonify({
            "message": "some errors in getting Persons"
        })


@app.route('/emp_put/<int:id>', methods=['GET', 'PUT'])
def emp_put(id):
    data = Employee.query.filter_by(id=id).first()
    try:
        val = request.json
        data.position = val['position']
        db.session.add(data)
        db.session.commit()
        return jsonify({"Message": "Updating success"
                        })

    except:
        return jsonify({
            "message": "some errors in Updating Employee"
        })


@app.route('/per_put/<id>', methods=['PUT'])
def per_put(id):
    try:
        try:
            data = Person.query.filter_by(id=id).first()
            data1 = request.json
            data.name = data1['name']
            data.age = data1['age']
            data.employee_id = data['employee_id']
            db.session.add(data)
            db.session.commit()

            return jsonify({"Message": "Updating success"})
        except:
            raise AttributeError("Errors Involved ")
    except:

        return jsonify({
            "message": "some errors in Updating Employee"
        })


@app.route('/add_put/<id>', methods=['PUT'])
def add_put(id):
    data = Address.query.filter_by(id=id).first()
    try:
        try:
            val = request.json
            data.role = val['role']
            db.session.add(data)
            db.session.commit()
            return jsonify({"Message": "Updating success"
                            })
        except:
            raise KeyError("Some Errors in Key values")

    except:
        return jsonify({
            "message": "some errors in Updating Employee"
        })


@app.route('/emp_del/<int:id>', methods=['DELETE'])
def emp_del(id):
    try:
        if request.method == "DELETE":
            del_val = Employee.query.filter_by(id=id).first()
            db.session.delete(del_val)
            db.session.commit()
            val1 = {"Deleted_id": del_val.position}
            return jsonify(val1)

    except:
        logger.warning(" Someone deleted the Employee")
        return jsonify({"Warning": " Session Failed"})


@app.route('/per_del/<int:id>', methods=['DELETE'])
def per_del(id):
    try:
        if request.method == "DELETE":
            del_val = Person.query.filter_by(id=id).first()
            db.session.delete(del_val)
            db.session.commit()
            val1 = {"Deleted_person": del_val.name}
            return jsonify(val1)

    except:
        logger.warning(" Someone deleted the Person")
        return jsonify({"Warning": " Session Failed"})


@app.route('/add_del/<int:id>', methods=['DELETE'])
def add_del(id):
    try:
        if request.method == "DELETE":
            del_val = Address.query.filter_by(id=id).first()
            db.session.delete(del_val)
            db.session.commit()
            val1 = {"Deleted_role": del_val.role}
            return jsonify(val1)

    except:
        logger.warning(" Someone deleted the Address")
        return jsonify({"Warning": " Session Failed"})


