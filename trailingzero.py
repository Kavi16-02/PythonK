'''Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?



Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.'''

class Solution:
    def trailingZeroes(self, n):
        c=0
        while n>0:
            n=n//5
            c+=n
        return c
k=Solution()
print(k.trailingZeroes(10))
