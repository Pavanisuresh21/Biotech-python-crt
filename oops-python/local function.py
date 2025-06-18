def a1():
    a=5
    c=a+b
    print(c)
    print(a)
    print(id(a))
    
#local variable - we can use only inside the function
def a2():
    a=10
    print(a)
    print(id(a))
    
#golabal variable - we can use outside the function
b=15
print(b)
print(id(b))
a1() #calling function
a2()
