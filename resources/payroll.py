
class Payslip:
    emp_name =""
    department =""
    pin = ""
    bank_details=""
    basic_pay = 0.00
    other_allowances = 0.00
    pension_contrib =0.06
    monthly_relief = 1408.00
    nssf = 200.00
    pension = 0.00
    gross_pay = 0.00
    taxable_amt = 0.00
    nhif = 0.00
    paye = 0.00
    other_deductions = 0.00
    total_deductions = 0.00
    net_pay=0.00

    def __init__(self, emp,	dept, pin, bank, basic, allow, deduc):
        Payslip.emp_name = emp
        Payslip.department = dept
        Payslip.pin = pin
        Payslip.bank_details = bank
        Payslip.basic_pay = basic
        Payslip.other_allowances = allow
        Payslip.other_deductions = deduc
        Payslip.pension(self)
        Payslip.gross_pay(self)
        Payslip.taxable_amt(self)
        Payslip.nhif(self)
        Payslip.paye(self)
        Payslip.total_deductions(self)
        Payslip.net_pay(self)




    def pension(self):
        self.pension = self.basic_pay * self.pension_contrib
        # return(self.pension)

    def gross_pay(self):
        self.gross_pay = self.basic_pay + self.other_allowances
        # return(self.gross_pay)

    def taxable_amt(self):
        if self.pension > 20000.00:
            self.taxable_amt = self.gross_pay - 20000.00 - 00.00
        else:
            self.taxable_amt= self.gross_pay - self.pension - 00
        # return(self.taxable_amt)

    def nhif(self):
        if self.basic_pay <= 5999.00:
            self.nhif = 150
        elif self.basic_pay<=7999:
            self.nhif = 300
        elif self.basic_pay<=11999:
            self.nhif = 400
        elif self.basic_pay<=14999:
            self.nhif = 500
        elif self.basic_pay<=19999:
            self.nhif = 600
        elif self.basic_pay<=24999:
            self.nhif = 750
        elif self.basic_pay<=29999:
            self.nhif = 850
        elif self.basic_pay<=34999:
            self.nhif = 900
        elif self.basic_pay<=39999:
            self.nhif = 950
        elif self.basic_pay<=44999:
            self.nhif = 1000
        elif self.basic_pay<=49999:
            self.nhif = 1100
        elif self.basic_pay<=59999:
            self.nhif = 1200
        elif self.basic_pay<=69999:
            self.nhif = 1300
        elif self.basic_pay<=79999:
            self.nhif = 1400
        elif self.basic_pay<=89999:
            self.nhif = 1500
        elif self.basic_pay<=99999:
            self.nhif = 1600
        else:
            self.nhif = 1700.00
        # return(self.nhif)

    def paye(self):
        if self.taxable_amt <= 12298:
            self.paye = self.taxable_amt * 0.1
        elif self.taxable_amt <= 23885:
            self.paye = (12298 * 0.1) + ((self.taxable_amt - 12298) * 0.15)
        elif self.taxable_amt <= 35472:
            self.paye = (12298 * 0.1) + ((23885-12298) * 0.15)+ ((self.taxable_amt - 23885) * 0.20)
        elif self.taxable_amt <= 47059:
            self.paye = (12298 * 0.1) + ((23885-12298) * 0.15)+ ((35472-23885) * 0.2)+((self.taxable_amt - 35472) * 0.25)
        else:
            self.paye = (12298 * 0.1) + ((23885-12298) * 0.15) + ((35472-23885) * 0.2) + ((47059-35472) * 0.25)+((self.taxable_amt - 47059) * 0.3)
        # return(self.paye)

    def total_deductions(self):
        self.total_deductions = self.paye + self.nhif + self.nssf + self.pension + self.other_deductions
        # return(self.total_deductions)

    def net_pay(self):
        self.net_pay = self.gross_pay - self.total_deductions + self.monthly_relief
        # return(self.net_pay)