class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                i += 3
            else:
                return nums[i]
        return nums[-1]