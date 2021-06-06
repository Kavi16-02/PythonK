#program to find no. of a in string wrt the n
<<<<<<< HEAD
s = input()
n = int(input())

=======
>>>>>>> 7c0ad4e44f52beb5c5d66b9810cd27f97d8a6554
def rep(s,n):
    r=0
    l=len(s)
    for i in range(l):
        if s[i] == 'a':
            r+=1
    r*= int(n/l)
    for i in range(0, n%l):
        if s[i]=='a':
            r+=1
    return r
<<<<<<< HEAD
k=rep(s,n)
=======
k=rep('kvai',10)
>>>>>>> 7c0ad4e44f52beb5c5d66b9810cd27f97d8a6554
print(k)
