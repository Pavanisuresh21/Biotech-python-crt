class mathematics:
    def addnumber(x,y):
        return x+y
m=staticmethod(mathematics.addnumber)
print(m(4,44))
print()

class mathematics:
    @staticmethod
    def addnumbers(x,y):
        return x+y
print(mathematics.addnumbers(4,44))
print()
