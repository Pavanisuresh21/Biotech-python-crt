#multiple inheritance
class dance:
    def dancing(self):
        print("I can dance")
class fly:
    def flying(self):
        print("I can fly also")
class peacock(dance,fly):
    def sound(self):
        print("i had a good sound too")
p1=peacock()
p1.dancing()
p1.flying()
p1.sound()
print()

#Hierarchial
class shape:
    def area(self):
        print("calculate area:")
class circle(shape):
    def circlearea(self,radius):
        print("area of circle",3.14*radius*radius)
class square(shape):
    def squarearea(self,side):
        print("area of square=",side*side)
c1=circle()
c1.area()
c1.circlearea(5)
s1=square()
s1.area()
s1.squarearea(5)
