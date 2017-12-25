class Parent:

    def print_last_name(self):
        print("Khandaker")

class Child(Parent):
    def __init__(self, firstName):
        self.firstName = firstName
    def print_last_name(self):
        print("Ahmed")

Child1 = Child("Mamun")
print(Child1.firstName)
Child1.print_last_name()