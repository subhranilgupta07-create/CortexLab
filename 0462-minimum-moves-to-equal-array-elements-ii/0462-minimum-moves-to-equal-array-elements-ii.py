class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        if (len(nums) % 2 == 0):
            median = (nums[len(nums)//2] + nums[len(nums)//2 - 1])/2
        else:
            median = nums[len(nums)//2] 
        S = 0      
        if isinstance(median, int):
            for i in range (len(nums)):
                S += abs(nums[i] - median)
        elif isinstance(median, float):
            for i in range (len(nums)):
                S1 += abs(nums[i] - (median - 0.5))
                S2 += abs(nums[i] - (median + 0.5)) 
            S = min(S1, S2)  
        return S              