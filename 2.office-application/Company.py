from Subject import Subject


class Company(Subject):

    subscribers = []
    project_type = ''
    projects = []

    def hire(self, observer):
        self.subscribers.append(observer)
        print(f"{observer.name} is hired")

    def fire(self, observer):
        self.subscribers.remove(observer)
        print(f"{observer.name} is fired")

    def notify(self):
        for staff in self.subscribers:
            staff.update(self)

    def getNewProject(self, project):
        self.projects.append(project)
        self.project_type = project.type
        self.notify()
