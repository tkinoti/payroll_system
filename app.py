#--importing Flask class from flask module
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from config import Development
from resources.payroll import Payslip

#--instance of a class - creating an object i.e instantiating class Flask
app = Flask(__name__)
#--this is a config parameter that shows where our database lives
# --from = we have the database type, then the owner then the password, then the url, the port, then database name
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Owen2013@127.0.0.1:5432/payroll_system'
app.config.from_object(Development) #--similar to above but now referencing the development class
# app.config.from_object(Testing) #--comment the environment not in use

#--initialize sqlalchemy

db = SQLAlchemy(app)
from models.Employees import EmployeesModel
from models.Departments import DepartmentModel

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/employees/<int:dept_id>')
def employees(dept_id):
    #new_department=DepartmentModel.fetch_all()
    this_department=DepartmentModel.fetch_by_id(dept_id)
    employees=this_department.employees
    #department_id =dept_id
    #dept = DepartmentModel.fetch_by_id(dept_id)
    #dept_name = dept.name
    departments=DepartmentModel.fetch_all()
    return render_template('employees.html', this_department=this_department, idara=departments)

#--registering a route
@app.route('/')
#--function to run when clients visit this route
def home():
    departments = DepartmentModel.fetch_all()
    return render_template('index.html',idara = departments)

#--creating another route
# @app.route('/name')
# def name():
#     return 'Tom'

#--run flask
# if __name__ == '__main__':
#     app.run()
@app.route('/new_department',methods=['POST'])
def new_department():
    department_name = request.form['department']
    if DepartmentModel.fetch_by_name(department_name):
        #read more on bootstrap alerts with flash and ensure the message pops up
        flash('department ' + department_name + ' already exists')
        return redirect(url_for('home'))
    department = DepartmentModel(name=department_name)#name is the field name on the database and department is on form in html code
    department.insert_to_db()
    return redirect(url_for('home'))




@app.route('/new_employee',methods=['POST'])
def new_employee():
    name_of_employee=request.form['full_name']#name_of_employee random varible, full_name is in the form and full_name below is the db column name
    kra_pin=request.form['kra_pin']
    gender=request.form['gender']
    national_id=request.form['national_id']
    email=request.form['email']
    department_id=int(request.form['department_id'])
    basic_salary=request.form['basic_sal']
    benefits=request.form['benefits']
    emp=EmployeesModel(full_name=name_of_employee,kra_pin=kra_pin,gender=gender, national_id=national_id,email=email,department_id=department_id,
                       basic_sal=basic_salary,benefits=benefits) # full_name is db column and name_of_employee is the variable created above
    emp.insert_to_db()
    return redirect(url_for('home'))

@app.route('/editemployee/<int:emp_id>',methods=['POST'])
def editemployee(emp_id):
    name_of_employee = request.form['full_name']
    kra_pin = request.form['kra_pin']
    gender = request.form['gender']
    national_id = request.form['national_id']
    email = request.form['email']
    department_id = int(request.form['department_id'])
    basic_salary = request.form['basic_sal']
    benefits = request.form['benefits']

    if gender =="na":
        gender=None
    if department_id=="0":
        department_id=None

    EmployeesModel.update_by_id(emp_id=emp_id, full_name=name_of_employee, kra_pin=kra_pin,gender=gender,national_id=national_id,
                                email=email, department_id=department_id,basic_sal=basic_salary, benefits=benefits)

    this_emp = EmployeesModel.fetch_by_id(emp_id=emp_id)
    this_dept = this_emp.department
    return redirect(url_for('employees',dept_id=this_dept.emp_id))



@app.route('/payroll/<int:emp_id>')
def payroll(emp_id):
    employee=EmployeesModel.fetch_by_id(emp_id)
    return render_template('payroll.html',employee=employee)

@app.route('/generatepayroll/<int:emp_id>',methods=['POST'])
def generatepayroll(emp_id):
    this_employee = EmployeesModel.fetch_by_id(emp_id)
    salary=Payslip(this_employee.full_name,this_employee.department_id,this_employee.kra_pin, "bank", this_employee.basic_sal,
                   this_employee.benefits, 2000)

    # print("Basic", salary.basic_pay)
    # print("Pension", salary.pension)
    # print("Gross", salary.gross_pay)
    # print("Taxable Amount", salary.taxable_amt)
    # print("NSSF", salary.nssf)
    # print("NHIF", salary.nhif)
    # print("PAYE", salary.paye)



    return redirect(url_for('home'))

@app.route('/deleteemployee/<int:emp_id>')
def deleteemployee(emp_id):
    this_emp =EmployeesModel.fetch_by_id(emp_id=emp_id)
    this_dept =this_emp.department
    EmployeesModel.delete_by_id(emp_id)
    return redirect(url_for('employees', dept_id=this_dept.id))
