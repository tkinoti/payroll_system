#--importing Flask class from flask module
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from config import Development
from resources.payroll import Payslip
import pygal

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

    #creating a pie chart in the home page
    all_employees = EmployeesModel.fetch_all()
    male = 0
    female = 0
    others = 0

    for each in all_employees:
        if each.gender == 'male':
            male += 1
        elif each.gender == 'female':
            female += 1
        else:
            others += 1

    pie_chart = pygal.Pie() # instantiating the pie class
    pie_chart.title = 'Analysing Company Employees By Gender'
    pie_chart.add('Male', male)
    pie_chart.add('Female', female)
    pie_chart.add('Others', others)
    chart=pie_chart.render_data_uri()

    # creating a  bar graph in the home page
    line_chart = pygal.Bar() # instantiating the bar graph class
    line_chart.title = 'Salary Cost Per Department'

    #loop over departments
    for each_dept in departments:
        line_chart.add(each_dept.name, DepartmentModel.fetch_total_payroll_by_id(each_dept.id))
    bar_graph = line_chart.render_data_uri()

    return render_template('index.html',idara = departments, chart=chart, bar_graph=bar_graph)



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

# @app.route('/generatepayroll/<int:emp_id>',methods=['POST'])
# def generatepayroll(emp_id):
#     this_employee = EmployeesModel.fetch_by_id(emp_id)
#     salary=Payslip(this_employee.full_name,this_employee.department_id,this_employee.kra_pin, "bank", this_employee.basic_sal,
#                    this_employee.benefits, 2000)
    # return redirect(url_for('home'))


@app.route('/deleteemployee/<int:emp_id>')
def deleteemployee(emp_id):
    this_emp =EmployeesModel.fetch_by_id(emp_id=emp_id)
    this_dept =this_emp.department
    EmployeesModel.delete_by_id(emp_id)
    return redirect(url_for('employees', dept_id=this_dept.id))

#from Keith

@app.route('/generate_payroll/<int:emp_id>', methods=['POST'])
def generate_payroll(emp_id):
    this_employee = EmployeeModel.fetch_employee_by_id(emp_id)
    overtime = request.form['overtime']

    payroll = Payslip(this_employee.full_name, this_employee.basic_salary, this_employee.benefits, float(overtime))

    name = payroll.name
    month = request.form['month']
    loan = request.form['loan']
    salary_advance = request.form['salary_advance']
    gross_salary =  payroll.gross_salary
    taxable_income = payroll.taxable_income
    nssf =  round(payroll.NSSF, 2)
    paye =  round(payroll.PAYE, 2)
    personal_relief = payroll.personal_relief
    tax_net_off_relief =  round(payroll.after_relief, 2)
    nhif =  payroll.NHIF
    net_salary =  round(payroll.net_salary, 2)
    take_home_pay = net_salary - (float(loan)  + float(salary_advance))

    payslip = PayrollModel(full_name=name, month=month, overtime=overtime,loan_deduction=loan, salary_advance=salary_advance, gross_salary=gross_salary, NSSF=nssf, taxable_income=taxable_income, PAYE=paye, personal_relief=personal_relief, tax_net_off_relief=tax_net_off_relief, NHIF=nhif, net_salary=net_salary, take_home_pay=take_home_pay, employee_id=this_employee.id)
    payslip.insert_to_db()
    flash('Payslip for ' + this_employee.full_name + ' has been successfully generated', 'success')
    return redirect(url_for('index'))
