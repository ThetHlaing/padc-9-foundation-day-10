from abc import ABC,abstractclassmethod

class BaseModel(ABC):
    @abstractclassmethod
    def save(cls):
        pass

    @abstractclassmethod
    def display(cls):
        pass

    @abstractclassmethod
    def update(cls):
        pass

