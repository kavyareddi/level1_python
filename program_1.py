#program to find fibanocci series using for loop
#input: Expected an integer which indicates the number of times to print the sequence
#output : prints the fibonacci series for given number of times
# Fibonacci series will start at 0 and travel upto below number
number = int(input("\nPlease Enter the Range Number: "))
# Initializing First and Second Values of a Series
first_value = 0
second_value = 1
# finding and displaying fibanocci series
for num in range(0, number):#goes through every element in that range
    if (num <= 1): #verifyiing the things for numbers less than or equal to 1
        next = num
    else:#if if condition fails it executes the conditions below
        next = first_value + second_value
        first_value = second_value
        second_value = next
    print(next)#prints sequence of fibanocci series

# Python Fibonacci series Program using Recursion
#input: Expected an integer which indicates the number of times to print the sequence
#output : prints the fibonacci series for given number of times
# Recursive Function Beginning
def fibonacci_series(number):
           if(number == 0):
                      return 0
           elif(number == 1):
                      return 1
           else:
                      return (fibonacci_series(number - 2)+ fibonacci_series(number - 1))

# End of the Function

# Fibonacci series will start at 0 and travel upto below number
number = int(input("\nPlease Enter the Range Number: "))

# Find & Displaying Fibonacci series
for num in range(0, number):
           print(fibonacci_series(num))



