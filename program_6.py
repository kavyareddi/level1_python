#Python Program to Print Sum of Negative Numbers, Positive Even Numbers and Positive Odd numbers in a List
try:
    n=int(input("Enter the number of elements to be in the list:"))
except:
    print('value error')
b=[]
for i in range(0,n):
    try:
        a=float(input("Element: "))
        b.append(a)
    except:
        print('value error')
sum1=0
sum2=0
sum3=0

for index in b:
    try:
        if(index>0):
            if(index%2==0):
                sum1=sum1+index
            else:
                sum2=sum2+index
        else:
            sum3=sum3+index
    except:
        print('bug')

print("Sum of all positive even numbers:",sum1)
print("Sum of all positive odd numbers:",sum2)
print("Sum of all negative numbers:",sum3)