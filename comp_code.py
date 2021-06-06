#program to find no. of a in string wrt the n
s = input()
n = int(input())
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
k=rep(s,n)
print(k)
