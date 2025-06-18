class base:
    def __init__(self):
        self.__a=32
        print(self.__a)
class derived(base):
    def __init__(self):
        base.__init__(self)
        print(self.__a+2)
b1=base()
print()

#abstract method
from abc import ABC,abstractmethod
class car(ABC):
    @abstractmethod
    def mileage(self):
        pass
class tesla(car):
    def mileage(self):
        print("mileage is 20kmph")

class suzuka(car):
    def mileage(self):
        print("mileage is 12kmph")

t1=tesla()
t1.mileage()
s1=suzuka()
s1.mileage()
print()

