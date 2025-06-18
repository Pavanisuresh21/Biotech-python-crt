#multiple constructors in a class.
class person:
    def __init__(self):
        print("I'm a first constructor")
    def __init__(self):
        print("I'm a second constructor")
    def __int__(self):
        print("I'm a third constructor")
p1.person()
