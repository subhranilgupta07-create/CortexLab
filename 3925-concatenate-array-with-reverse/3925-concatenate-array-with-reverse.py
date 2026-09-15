class Solution(object):
    def concatWithReverse(self, nums):
        a=nums[:]
        b=nums[::-1]
        result=a+b
        return result    