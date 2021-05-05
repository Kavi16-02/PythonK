#problem statement::Use The Function name,return type and argument as:
#int findValue(a,b)
#The function must return 1 if the second number b is the last digits of a,else return 0
#sample input a=12344 b=344
#sample output yes


def findValue(a,b):
    if [len(a)-len(b):] == b:
        return 1
    else:
        return 0

a = input()
b = input()
if findValue(a,b)==1:
    print("yes",end"")
else:
    print("No",end"")
