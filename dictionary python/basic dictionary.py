jobrole={101:'front-end developer',102:'back-end developer'}
print(jobrole)
print(type(jobrole))
print(jobrole[101])
print(jobrole[102])
print()
#to replace element in dict
jobrole[101]='UI developer'
print (jobrole)
print()
#add element in dict
jobrole[104]='data engineer'
jobrole[105]='python developer'
jobrole[106]='data analyst'
print(jobrole)
print()
#deleting an element in dict
jobrole.pop(101)
print(jobrole)
print()
#or this method can be used
del jobrole[102]
print(jobrole)
print()
#to return list of all keys in dict
print(jobrole.keys())
print()
#to check the length of list
print(len(jobrole))
print()
#returns the list of key value pairs(tuples) in the dict
print(jobrole.items())
print()
#adding elements with existing dict
a={108:'four'}
jobrole.update(a)
print(jobrole)
print()
#creating dictionaries from keys and values
key={"apple","ball"}
value="for kids"
d=dict.fromkeys(key,value)
print(d)
