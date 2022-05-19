from app.config import db1


class Employee(db1.Document):
    id = db1.IntegerField(primary_key=True)
    emp_code = db1.IntegerField()
    position = db1.StringField()



