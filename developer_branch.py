# Program to make a simple calculator that can add, subtract, multiply and divide using functions



# This function adds two numbers

def add(x, y):

   return x + y



# This function subtracts two numbers

def subtract(x, y):

   return x - y



# This function multiplies two numbers
def multiply(x, y):

    return x * y




# This function divides two numbers
try:
    def divide(x, y):

        return x / y
except:
    print('bug')





print("Select operation.")

print("1.Add")

print("2.Subtract")

print("3.Multiply")

print("4.Divide")



# Take input from the user

choice = input("Enter choice(1/2/3/4):")
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except:
    print('value error')
try:
    if choice == '1':
        print(num1,"+",num2,"=", add(num1,num2))

    elif choice == '2':

        print(num1,"-",num2,"=", subtract(num1,num2))

    elif choice == '3':

        print(num1,"*",num2,"=", multiply(num1,num2))
    elif choice == '4':

        print(num1,"/",num2,"=", divide(num1,num2))

    else:

        print("choice error")
except (ValueError, ZeroDivisionError):
    print('ZeroDivisionError')


