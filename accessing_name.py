class Person:
    def  __init__(self, fname,lname):
        self.fname=fname
        self.lname=lname
    def values(self):
        print("My names are ", self.fname," ",self.lname)
    @classmethod
    def valinput(inputer):
        return inputer(
            input("First Name: "),
            input("Last Name :")
            )
nowValue=Person.valinput()
print(nowValue.fname)

class Student(Person):
    print(nowValue.lname)


