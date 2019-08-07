from payroll import Payslip

emp1 = Payslip("Tom", "Finance", "A000AA", "SBK", 70000, 1000,500)

# print(emp1.emp_name)
# print(emp1.pension())
# print(emp1.gross_pay())
# print(emp1.taxable_amt())
# print(emp1.paye())
# print(emp1.nhif())
# print(emp1.total_deductions())
# print(emp1.net_pay())

print(f' Name: {emp1.emp_name} \n basic pay: {emp1.basic_pay} \n gross pay: {emp1.gross_pay} \n '
      f'taxable amount: {emp1.taxable_amt}  \n nhif: {emp1.nhif}\n paye: {emp1.paye} \n net salary:{emp1.net_pay}')

#
# emp2 = Payslip("Tim", "Credit", "A0099BB", "BBK", 588528.22, 10310.00,75264.03)
# print(emp2.emp_name)
# print(emp2.pension())
# print(emp2.gross_pay())
# print(emp2.taxable_amt())
# print(emp2.paye())
# print(emp2.nhif())
# print(emp2.total_deductions())
# print(emp2.net_pay())
#
# emp3 = Payslip("Timmy", "Credit", "A0099BB", "BBK", 1588528.22, 103190.00,75264.03)
# print(emp3.emp_name)
# print(emp3.pension())
# print(emp3.gross_pay())
# print(emp3.taxable_amt())
# print(emp3.paye())
# print(emp3.nhif())
# print(emp3.total_deductions())
# print(emp3.net_pay())