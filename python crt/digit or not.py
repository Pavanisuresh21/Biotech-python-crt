a=int(input())
if(a<=999 and a>=100 or a>=-999 and a<=-100):
    print("three digit")
elif(a>=999 and a<=100 or a<=-999 and a>=-100):
    print("not three digit")
elif(a<=9999 and a>=1000 or a>=-9999 and a<=-1000):
    print("four digit")
elif(a>=9999 and a<=1000 or a<=-9999 and a>=-1000):
    print("not four digit")
else:
    print("not 3-digit or 4-digit")
