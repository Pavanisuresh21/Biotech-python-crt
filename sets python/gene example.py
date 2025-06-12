#input=[3.2,5.5,12.4,16.7,2.1]
#output=["underexpressed","normal","normal","overexpressed","underexpressed"]
size=int(input("Enter the size of input:"))
underexpressed=0
normal=0
overexpressed=0
list=[]

for i in range(size):
    gene=float(input("Enter the value:"))    
    if(gene<5):
        list.append("underexpressed")
    elif(gene>=5 and gene<=15):
        list.append("normal")
    else:
        list.append("overexpressed")
print("Gene values:",list)

