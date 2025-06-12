set={'python','c','c++','javascript','HTML','AngulaR js'}
print(set)
print(type(set))
print()
print('python' in set)
print()
set.add('jython')
print(set)
print()
set.add('nodejs')
print(set)
print()
#to add
set.update(['pypy','iron python'])
print(set)
print()
#to remove single item 
set.remove('c')
print(set)
print()
#pop-to remove and return orbitary item from set
set.pop()
print(set)
print()
#discard
set.discard('c++')
print(set)
print()
#to remove all items from set
set.clear()
print(set)
print()
