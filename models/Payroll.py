from app import  db

class PayrollModel(db.Model)
    __tablename__ = 'payroll'
    id = db.column(db.Integer, primary=True)
    overtime = db.column(db.Float)
    month=db.column(db.String(20),nullable=False)
    loan_deducted = db.column(db.Float
    advance_pay = db.column(db.Float)
    gross_salary = db.column(db.Float)
    personal_relief = db.column(db.Float)
    taxable_amount = db.column(db.Float)
    PAYE = db.column(db.Float)
    NHIF = db.column(db.Float)
    NSSF = db.column(db.Float)
    net_salary = db.column(db.Float)
    employee_id=db.column(db.Integer,db.ForeignKey('employee_id'))

    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()