class employee:
    def __init__(self):
        print("Moving to data/attribute definition")
        self.id = 123
        self.salary = 23000
        self.designation = "MLE"
        print("Definition of data/attribute completed")

#Create object/ instance of class

    def travel(self, destination):
        print("Manually calling this travel method")
        print(f"Employee is now travelling to {destination}")


abhi = employee()
#printing a attribute/variable
# print(abhi.id)

#calling a method functionality
abhi.travel("Paris")

print(type(abhi))