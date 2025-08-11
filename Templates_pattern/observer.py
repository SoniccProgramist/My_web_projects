from abc import ABC, abstractmethod


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message:str):
        for observer in self._observers:
            observer.update(message)

class Observer(ABC):
    @abstractmethod
    def update(self, message:str):
        pass

class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message:str):
        print(f"Observer {self.name}. Get message: {message}")


subject = Subject()

observer1 = ConcreteObserver("Obs 1")
observer2 = ConcreteObserver("Obs 2")

subject.attach(observer1)
subject.attach(observer2)

subject.notify("Get message to all observers")
