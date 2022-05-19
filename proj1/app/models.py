from app.config import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emp_code = db.Column(db.String(100), unique=True)
    position = db.Column(db.String(20))
    person = db.relationship('Person', backref='employee', lazy='dynamic')
    address_add = db.relationship('Address', backref='employee', lazy='joined')


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), unique=True)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.String(30))
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))


db.create_all()



