'''You are given a binary array nums (0-indexed).

We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit).

For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
Return an array of booleans answer where answer[i] is true if xi is divisible by 5.

'''
a=[1,0,1,1,1,1]
num=''
sol=[]
for i in a:
    num=num+str(i)
    dec=int(num,2)
    if dec%5==0:
        sol.append(True)
    else:
        sol.append(False)
print(sol)
