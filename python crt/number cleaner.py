num_list=list(map(int,input("enter list of positive and negative numbers:").split()))
print(num_list)
for i in range(len(num_list)):
    if(num_list[i]<0):
        num_list[i]=num_list[i]*0
print(num_list)
for i in range(len(num_list)):
    if(num_list[i]%2==0 and num_list[i]!=0):
        print(num_list[i])
    elif(num_list[i]%3==0 and num_list[i]!=0):
        print(num_list[i])

        

