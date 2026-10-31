class Solution(object):
    def targetIndices(self, nums, target):
        A = []
        nums.sort()
        for i in range (len(nums)):
            if (nums[i] == target):
                A.append(i)
        return A        