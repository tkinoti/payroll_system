#--importing Flask class from flask module
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from config import Development

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
    return render_template('employees.html')

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
    pass