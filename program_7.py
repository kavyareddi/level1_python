#Python Program to Check if a Date is Valid and Print the Incremented Date if it is
print('please enter date in dd/mm/yy format')#user to enter the valid format
try:
    date=input("Enter the date: ")#taking input from user
    dd, mm, yy = date.split('/')
except:
    print('please enter a valid date')
try:
    dd = int(dd)#taking input values as integers
    mm = int(mm)
    yy = int(yy)
except:
    print('please enter numbers')
try:
    if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):#looping for maximum value in month
        max1=31
    elif(mm==4 or mm==6 or mm==9 or mm==11):
        max1=30
    elif(yy%4==0 and yy%100!=0 or yy%400==0):
        max1=29
    else:
        max1=28
except:
    print('please enter valid numbers')

if(mm<1 or mm>12):#condition for invalid month
    print("invalid date.")
elif(dd<1 or dd>max1):#condition when day is out of index
    print('invalid date')
elif(dd==max1 and mm!=12):
    dd=1
    mm=mm+1 #incrementing month by value 1
    print("The incremented date is: ",dd,mm,yy)
elif(dd==31 and mm==12):
    dd=1
    mm=1
    yy=yy+1
    print("The incremented date is: ",dd,mm,yy)
else:
    dd=dd+1
    print("The incremented date is: ",dd,mm,yy)