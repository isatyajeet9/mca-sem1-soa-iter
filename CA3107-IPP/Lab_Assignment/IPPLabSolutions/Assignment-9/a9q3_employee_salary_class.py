# A9Q3
# Question: Create a class to calculate employee salary. The attributes of the class are
#           emp_id, name, basic salary and gross salary. The operations are input details,
#           display details, calculate gross salary: gross = basic + HRA(40%) + DA(60%)
# Name: Satyajeet Nayak
# Appl No: 25C200429

class Employee:
    def __init__(self, emp_id, name, basic):
        self.emp_id = emp_id
        self.name = name
        self.basic = basic
        self.gross = 0

    def calculate(self):
        hra = 0.4 * self.basic
        da = 0.6 * self.basic
        self.gross = self.basic + hra + da

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic)
        print("Gross Salary:", self.gross)

obj = Employee(101, "Sarthak", 20000)
obj.calculate()
obj.display()
