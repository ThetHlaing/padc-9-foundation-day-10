from abc import ABC,abstractmethod

class Subject(ABC):

    @abstractmethod
    def hire(self,subscriber):
        pass

    @abstractmethod 
    def fire(self,subscriber):
        pass

    @abstractmethod
    def notify(self):
        pass
