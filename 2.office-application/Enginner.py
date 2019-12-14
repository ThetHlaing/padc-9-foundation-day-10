from Observer import Observer

class Enginner(Observer):

    name = ''

    def __init__(self,name):
        self.name = name
    
    def work(self):
        print(f"{self.name} is started building things")

    def update(self,subject):
        if subject.project_type == 'construction':
            self.work()