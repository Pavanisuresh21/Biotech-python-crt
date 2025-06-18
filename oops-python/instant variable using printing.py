class person:
    def __init__(se,name,age):
        se.name=name
        se.age=age
    def printing(self):
        print(self.name,self.age)
    def decide(self):
        if self.age>18:
            print ("Major")
        else:
            print("Minor")
    def upercaseconversion(self):
        print(self.name.upper())

    def length(self):
        print(len(self.name))
p1=person('kiran',17)
p2=person('sandeep',42)
p3=person('jaideepthi',18)
p1.printing() #calling function
p2.printing()
p3.printing()
p1.decide()
p2.decide()
p3.decide()
p1.upercaseconversion()
p2.upercaseconversion()
p3.upercaseconversion()
p1.length()
p2.length()
p3.length()
print()

