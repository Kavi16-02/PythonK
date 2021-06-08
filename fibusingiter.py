#Fibonacci of a number using Iterative method

n=int(input("Enter N:"))
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    prevPrevNum=0
    prevNum=1
    for i in range(2,n+1):
        currentNumber=prevPrevNum+prevNum
        prevPrevNum=prevNum
        prevNum=currentNumber
    return currentNumber
print("Fib of n",fib(n))
