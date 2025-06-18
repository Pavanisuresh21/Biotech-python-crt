class base:
    def __init__(self):
        self._a=32
        print(self._a)
class derived(base):
    def __init__(self):
        base.__init__(self)
        print(self._a+2)
x=base()
y=derived()
print(x._a)
print(y._a)
print()

class base:
    def __init__(self):
        self._a=32
        print(self._a)
class derived(base):
    def __init__(self):
        base.__init__(self)
        print(self._a+2)
class derived1(derived):
    def __iinit__(self):
        derived.__init__(self)
        print(sef._a*2)
x=derived1()
