# A9Q4
# Question: Create a class to calculate student grade. The attributes of the class are name,
#           registration number, mark and grade. Operations are input details, display details,
#           calculate grade: O(>=90), A(80-89), B(70-79), C(60-69), D(50-59), E(40-49), F(<40)
# Name: Satyajeet Nayak
# Appl No: 25C200429

class Student:
    def __init__(self, name, reg, mark):
        self.name = name
        self.reg = reg
        self.mark = mark
        self.grade = ""

    def calc_grade(self):
        if self.mark >= 90:
            self.grade = "O"
        elif self.mark >= 80:
            self.grade = "A"
        elif self.mark >= 70:
            self.grade = "B"
        elif self.mark >= 60:
            self.grade = "C"
        elif self.mark >= 50:
            self.grade = "D"
        elif self.mark >= 40:
            self.grade = "E"
        else:
            self.grade = "F"

    def display(self):
        print("Name:", self.name)
        print("Reg No:", self.reg)
        print("Mark:", self.mark)
        print("Grade:", self.grade)

obj = Student("Sarthak", "25C2001", 76)
obj.calc_grade()
obj.display()
