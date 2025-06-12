size=int(input("enter the size of list :"))
list=[]
unique_list=[]
for i in range (size):
    temp=int(input(f"enter the integer value at {i} index position:"))
    list.append(temp)
print(f"user entered list : {list}")
for i in list:
    if i not in unique_list:
        unique_list.append(i)
print(f"unique_list:{unique_list}")
