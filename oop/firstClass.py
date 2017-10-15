class FirstClass:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
    def displayInfo(self):
        return self.firstname + " " +self.lastname

# instanciation

firstClass=FirstClass('Dilip','Maharjan')

#method call
print firstClass.displayInfo()

#implicit method to check of the class has certain attribute
print hasattr(firstClass,'firstname');

#implicit method to set an attribute
setattr(firstClass,'age',27);

print hasattr(firstClass,'age')
print getattr(firstClass,'age')

delattr(firstClass,'age')
print hasattr(firstClass,'age')
