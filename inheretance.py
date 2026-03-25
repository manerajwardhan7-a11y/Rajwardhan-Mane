class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    def _init_(self, name, age, employee_id, salary):
        super()._init_(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ₹{self.salary}")


class Manager(Employee, Person):
    def _init_(self, name, age, employee_id, salary, department):
        super()._init_(name, age, employee_id, salary)
        self.department = department

    def display_manager_info(self):
        print("\n--- Manager Details ---")
        self.display_person_info()
        self.display_employee_info()
        print(f"Department: {self.department}")

    def approve_leave(self):
        print(f"{self.name} has approved the leave request.")



manager1 = Manager(
    name="Dipak Patil",
    age=40,
    employee_id="M101",
    salary=85000,
    department="IT"
)


manager1.display_manager_info()
manager1.approve_leave()