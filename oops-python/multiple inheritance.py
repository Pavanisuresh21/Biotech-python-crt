#multiple inheritance
class father:
    fathername=''
    def father(self):
        print(self.fathername)
class mother:
    mothername=''
    def mother(self):
        print(self.mothername)
class son1(father,mother):
    son1name=''
    def son1information(self):
        print(self.fathername)
        print(self.mothername)
        print(self.son1name)

s1=son1()
s1.son1name="Lava"
s1.fathername="Ram" 
s1.mothername="Sita"
s1.son1information()
