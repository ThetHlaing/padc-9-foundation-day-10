from Database import Database
from BaseModel import BaseModel

class Department(BaseModel):
    id = None
    name = None
    table_name = 'departments'

    def __init__(self,tuple_data = None):
        if(tuple_data):
            self.id = tuple_data[0]
            self.name = tuple_data[1]
        #print("Department class is initialized")

    def save(self):
        Database._cursor.execute(
            "insert into departments (name) values (%s)", [self.name])
        Database._db.commit()
        self.id = Database._cursor.lastrowid
        self.display()

    def update(self):
        pass

    def display(self):
        print(f'[{self.id}] - {self.name} Department')

    @staticmethod
    def find(id): 
        result_tuple = Database.base_find(id,'departments')
        return Department(result_tuple)
    
    @staticmethod
    def get():
        department_list = []
        for departmentTuple in Database.base_get('departments'):
            department = Department(departmentTuple)
            department_list.append(department)
        return department_list
