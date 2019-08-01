#importing sqlalchemy object from main file
from app import db
class EmployeesModel(db.Model):
    __tablename__ = 'employees'
    emp_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), unique=True, nullable=False)
    gender =db.Column(db.String(10), nullable=False)
    kra_pin = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    national_id = db.Column(db.String(20), unique=True)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    basic_sal = db.Column(db.Float, nullable=False)
    benefits = db.Column(db.Float)