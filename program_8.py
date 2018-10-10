
# Python Program to find number of Times a given letter occurs in a string recursively

def check(string, ch):#defining function for string and choice of letter
    if not string: #
        return 0
    elif string[0] == ch:#compares string with the ch
        return 1 + check(string[1:], ch) #returns the count of occurance if codition is satisfied
    else:
        return check(string[1:], ch)

string =input("Enter string:")# input for string
ch = input("Enter character to check:")#input for letter to search
print("Count is:")
print(check(string, ch))