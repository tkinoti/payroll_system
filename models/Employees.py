# importing sqlalchemy object from main file
from app import db


class EmployeesModel(db.Model):
    __tablename__ = 'employees'
    emp_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    kra_pin = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    national_id = db.Column(db.String(20), unique=True)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    basic_sal = db.Column(db.Float, nullable=False)
    benefits = db.Column(db.Float)

    # create
    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()

    # read
    @classmethod
    def fetch_by_id(cls, emp_id):
        return cls.query.filter_by(emp_id=emp_id).first()

    # update
    @classmethod
    def update_by_id(cls, emp_id, full_name=None, gender=None, kra_pin=None, email=None, national_id=None,
                  department_id=None, basic_sal=None, benefits=None):
        record = cls.fetch_by_id(emp_id=emp_id)
        if full_name:
            record.full_name = full_name
        if gender:
            record.gender = gender
        if kra_pin:
            record.kra_pin = kra_pin
        if email:
            record.email = email
        if national_id:
            record.national_id = national_id
        if department_id:
            record.department_id = department_id
        if basic_sal:
            record.basic_sal = basic_sal
        if benefits:
            record.benefits = benefits
        db.session.commit()
        return True

    @classmethod
    def delete_by_id(cls, emp_id):
        record = cls.query.filter_by(emp_id=emp_id)
        record.delete()
        db.session.commit()
        return True
