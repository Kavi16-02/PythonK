'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2'''

class Solution:
    def majorityElement(self, nums):
        maj=nums[0]
        c=1
        for i in range(1,len(nums)):
            if nums[i]!=maj:
                c-=1
            else:
                c+=1
            if c==0:
                maj=nums[i]
                c=1
        return maj
k=Solution()
print(k.majorityElement([2,4,3,3,3,5,4,3,3,3,3,4,4,4,4,4,4,4,4]))
