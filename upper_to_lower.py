'''
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.



Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"




'''

a=input("Enter string in upper case:")
res=""

for i in a:
    if ord(i)>=65 and ord(i)<=90:
        res+=chr(ord(i)+32)
    else:
        res+=i
print(res)
