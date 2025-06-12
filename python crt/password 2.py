password=input("enter your password:")
num=0
spe=0
cap=0
for i in range(0,len(password)):
    if password[i].isalpha():
        if password[i].isupper():
            cap+=1
        elif password[i].isnumeric():
            num+=1
        else:
            spe+=1
if spe!=0 and num!=0 and cap!=0:
    print("it is valid password")
else:
    print("it is not a valid password")
