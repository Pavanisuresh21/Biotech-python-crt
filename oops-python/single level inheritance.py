class father:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)
class son(father):
    def __init__(self,name):
        self.name=name
    def show1(self):
        print(self.name)
x=father('Suresh')
x.show()
y=son('Akhil')
y.show1()
y.show()

