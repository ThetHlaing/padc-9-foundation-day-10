from Department import Department
from Employee import Employee

class MainController:

    @staticmethod
    def addNewDepartment():

        deparment = Department()
        deparment.name = input("Please enter the department name : ")
        deparment.save()

    @staticmethod
    def displayAllDepartments():
        department_list = Department.get()
        # cursor.execute("Select * from departments")
        for department in department_list:
            department.display()

    @staticmethod
    def addNewEmployee():
        employee = Employee()
        employee.name = input("Please enter the employee name :")
        employee.position = input("Please enter the job position : ")
        employee.salary = input("Please enter the salary : ")
        MainController.displayAllDepartments()
        employee.department_id = input("Please enter department id : ")
        employee.save()

    @staticmethod
    def displayAllEmployees():
        employees = Employee.get()
        for employee in employees:
            employee.display()

    @staticmethod
    def increaseSalary():
        print("Preparing to increase salary")
        MainController.displayAllEmployees()
        employee_id = input("Please select the employee : ")
        employee = Employee.find(employee_id)
        user_choise = input(
            f"Are you sure you want to raise {employee.name}'s salary? : y/n \n")
        if(user_choise == 'y'):
            increase_amount = int(input("How much do you want to increase : "))
            # employee.name = "This is going to be update"
            employee.salary = increase_amount + int(employee.salary)
            employee.update()
