class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        c = 1
        for i in range (1, len(nums)):
            if (nums[i] == nums[i - 1]):
                c += 1
            else:
                if c > len(nums)//2:
                    return nums[i - 1]    
                c = 1  
        if c > len(nums) // 2:
            return nums[-1]        