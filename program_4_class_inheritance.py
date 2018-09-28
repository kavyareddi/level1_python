#program on class inheritance
#input : defining classe subclass and thier attributes


class Person:
    # initializing the variables
       # defining constructor
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

        # defining class methods

    def showName(self):
        print(self.name)

    def showAge(self):
        print(self.age)


# definition of subclass starts here
class Student(Person):

    def __init__(self, studentName, studentAge, studentId):
        Person.__init__(self, studentName,studentAge)
        self.studentId = studentId

    def getId(self):
        return self.studentId  # returns the value of student id


# end of subclass definition


# Create an object of the superclass
person1 = Person("kavya", 23)
# call member methods of the objects
person1.showAge()
# Create an object of the subclass
student1 = Student("karthik", 22, 102)
print(student1.getId())
student1.showName()