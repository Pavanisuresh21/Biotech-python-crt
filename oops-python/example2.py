class customer:
    def __init__(self,name,item1,item2,item3,item4):
        self.name=name
        self.item1=item1
        self.item2=item2
        self.item3=item3
        self.item4=item4
    def calculation(self):
        print(self.name)
        tot=self.item1+self.item2+self.item3+self.item4
        print(tot)
        if(tot>200):
            t=tot-tot*(20/100)
            print(t)
        else:
            t=tot
s1=customer("Kiran",80,50,50,70)
s1.calculation()
print()

#second method
class store:
    def __init__(self,name,items):
        self.name=name
        self.items=items
    def calculation(self):
        x=self.items
        tp=0
        for i in range(x):
            p=int(input())
            tp+=p
        return tp

        
c1=store("Kiran",4)
tp=c1.calculation()
if (tp>=200):
    print(tp-tp*0.2)
else:
    print(tp)
