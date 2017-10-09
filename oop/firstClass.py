class FirstClass:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
    def displayInfo(self):
        return self.firstname + " " +self.lastname
firstClass=FirstClass('Dilip','Maharjan')
print firstClass.displayInfo()
print hasattr(firstClass,'firstname');
setattr(firstClass,'age',27);
print hasattr(firstClass,'age')
print getattr(firstClass,'age')
delattr(firstClass,'age')
print hasattr(firstClass,'age')
