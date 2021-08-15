'''Example for Instance method'''

class Emp:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def disp(self):
        return self.name,self.age
    def get_name(self):        #Accessor Methods
        return self.name
    def set_age(self,value):   #Mutator methods
        self.age=value
        return value
k1=Emp('kavi',2)
k2=Emp('sharma',12)
print(k1.age)
print(k1.get_name())
print(k1.set_age(21))
