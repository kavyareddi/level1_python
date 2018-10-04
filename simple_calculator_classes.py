#simple calculator using classes
class cal():#defining class
    def __init__(self, a, b):#intializing
        self.a = a
        self.b = b
#Methods for adding, substracting, multiplying, dividing two numbers and returning their respective results
    def add(self):
        return self.a + self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        try:
            return self.a / self.b
        except:
            print('value error')
    def sub(self):
        return self.a - self.b
a = int(float("Enter first number: "))
b = int(float("Enter second number: "))
#object for the class is created with the two numbers taken from the user passed as parameters.
obj = cal(a, b)
choice = 1
#if choice is 0, the loop is exited
while choice != 0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    try:
        choice = int(input("Enter choice: "))#user input for preferred operation
    except:
        print('please enter a valid choice')
    # loops for every operation of choice
    if choice == 1:
        print("Result: ", obj.add())
    elif choice == 2:
        print("Result: ", obj.sub())
    elif choice == 3:
        print("Result: ", obj.mul())
    elif choice == 4:
        print("Result: ", round(obj.div(), 2))
    elif choice == 0:
        print("Exiting!")
    else:
        print("choice error!")

print()




