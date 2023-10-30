class Employee():

    name = None
    age = None
    salary = None

    def show(self):
        return f"{self.name} --- {self.salary}"
    
emp = Employee()
emp.name = "Ksyusha"
emp.salary = 3000000
print(emp.show())
