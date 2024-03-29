from Database import Database
from Department import Department
from BaseModel import BaseModel


class Employee(BaseModel):

    id = None
    name = None
    position = None
    salary = None
    department_id = None
    table_name = 'employees'

    def __init__(self, tuple=None):
        if(tuple):
            self.id = tuple[0]
            self.name = tuple[1]
            self.position = tuple[2]
            self.department_id = tuple[3]
            self.department = Department.find(self.department_id)
            self.salary = tuple[4]

    def display(self):
        print(f'[{self.id}] - {self.name} - Position - {self.position}'
              f' - Department {self.department.name}'
              f' - Salary {self.salary} Ks')

    def save(self):
        Database._cursor.execute(
            "insert into employees set name = %s, position = %s, salary = %s, department_id = %s",
            [self.name, self.position, self.salary, self.department_id])
        Database._db.commit()
        self.id = Database._cursor.lastrowid
        self.department = Department.find(self.department_id)
        self.display()

    def update(self):
        Database._cursor.execute("Update employees set salary = %s,name = %s, position=%s, department_id = %s where id = %s",
                       [self.salary, self.name,self.position,self.department_id,self.id])
        Database._db.commit()
        self.department = Department.find(self.department_id)
        self.display()


    @staticmethod
    def find(id):        
        return Employee(Database.base_find(id,Employee.table_name))

    @staticmethod
    def get():
        employee_list = []
        for employeeTuple in Database.base_get(Employee.table_name):
            employee = Employee(employeeTuple)
            employee_list.append(employee)
        return employee_list
