class Solution(object):
    def sumCounts(self, nums):
        x = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                A = nums[i:j + 1]
                x += len(set(A)) ** 2
        return x