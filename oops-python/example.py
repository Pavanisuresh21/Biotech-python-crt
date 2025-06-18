class student:
    def __init__(self,name,rno,mat,phy,che):
        self.name=name
        self.rno=rno
        self.mat=mat
        self.phy=phy
        self.che=che
    def calculation(self):
        if (self.mat>=40 and self.phy>=40 and self.che>=40):
            tot=self.mat+self.phy+self.che
            avg=tot/3
            print(tot)
            print("%.2f"%(avg))
            if(self.mat>75 and self.phy>75) or (self.phy>75 and self.che>75) or (self.che>75 and self.mat>75):
                print("Admission is completed")
            else:
                print("Admission is not confirmed")
        else:
            print("Fail")
s1=student("Kiran",501,74,85,85)
s1.calculation()
