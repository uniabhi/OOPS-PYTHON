class employee:
    
    def __init__(self):
        # print(id(self))
        print("Moving to data/attribute definition")
        self.name = "Default User"
        self.id = 123
        self.salary = 23000
        self.designation = "MLE"
        # print("Definition of data/attribute completed")

#Create object/ instance of class

    def travel(self):
        print("Manually calling this travel method")
        print(f"Employee is now travelling to delhi")


abhi = employee()
print(id(abhi))


kumar = employee()
#printing a attribute/variable
# print(abhi.id)

#calling a method functionality
# abhi.travel("Paris")
print(id(kumar))

# print(type(abhi))
abhi.name = "Singh"
print(abhi.name)