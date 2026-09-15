class Solution(object):
    def concatWithReverse(self, nums):
        A = []
        for i in range (len(nums)):
            A.append(nums[i])
        for i in range(len(nums) - 1, -1, -1):
            A.append(nums[i])
        return A    