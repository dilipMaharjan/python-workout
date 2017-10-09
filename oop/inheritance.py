class Parent:
    def __init__(self):
        print "Parent"
    def add(self,num1,num2):
        return num1+num2

class Child(Parent):
    def __init__(self):
        print "Child"

child=Child()
print child.add(1,2)
