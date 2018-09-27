# program to print the greatest of two strings
# input : takes two strings as inputs
#output : prints the string which staisfies the given condition
#giving input strings
string1=str(input("Enter first string:"))
string2=str(input("Enter second string:"))
#intializing counter
count1=0
count2=0
# looping through the strings
for search in string1:
      count1 = count1 + 1
for count in string2:
      count2 = count2 + 1
#comparing the strings
if(count1 < count2):
      print("Larger string is:")
      print(string2)
elif(count1 == count2):
      print("Both strings are equal.")
else:
      print("Larger string is:")
      print(string1)
#sorting out the characters in first string that are not in second string
a = list(set(string1)-set(string2))
print("The letters are:")
for letter in a:
    print(letter)