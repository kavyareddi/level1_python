#simple calculator for complex numbers
#it adds two variabes
def add(x, y):
   return x + y
#defining function to substract variables
def subtract(x, y):
   return x - y
#defining functions to multiply variables
def multiply(x, y):
   return x * y
#defining function to divide variables
def divide(x, y):
    try:# handles if zero division or value errors occurs
        return x / y
    except:
        print('zero division error')
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
# Take input from the user
try:
    choice = input("Enter choice(1/2/3/4):")
except:
    print('please enter a valid choice')
#for user to enter the correct format
print('please enter numbers in a+bj format')
#taking input from user
try:
    num1 = complex(input('enter first number'))
    num2 = complex(input('enter second number'))
except:
    print('enter a valid number')
#loops for every operation of choice
if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))#adds numbers
elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))#substracts numbers
elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))#multiplies numbers
elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))#divides numbers
else:
    print("choice error")
