from Observer import Observer

class Accoutant(Observer):

    name = ''

    def __init__(self,name):
        self.name = name
    
    def work(self):
        print(f"{self.name} is started creating reports")

    def update(self,subject):
        if subject.project_type == 'finance':
            self.work()