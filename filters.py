'''Filters'''

def is_even(n):
    return n%2==0
def is_odd(n):
    return n%2!=0
nums=[1,2,3,4,5,67,8,8,9]
even = list(filter(is_even,nums))
print(even)
odd=list(filter(is_odd,nums))
print(odd)


'''or using lambda functions'''

nums=[1,2,3,4,5,67,8,8,9]
even = list(filter(lambda n: n%2==0,nums))
print(even)
odd=list(filter(lambda n:n%2!=0,nums))
print(odd)
