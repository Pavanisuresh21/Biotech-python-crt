#set operations
#union
set1={1,2,3,4,5}
set2={4,5,6,7}
print(set1|set2)
print()
#intersection
print(set1 &set2)
print()
#difference
print(set1-set2)
print()
#symbiotic difference
print(set1^set2)
print()
#subset
a={1,2,3}
b={1,2,3,4,5}
isub=a.issubset(b)
print(isub)
print()
#superset
i=b.issuperset(a)
print(i)
print()
