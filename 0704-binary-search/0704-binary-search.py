class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1
        pos = -1
        while (low <= high):
            mid = low + (high - low)//2
            if (nums[mid] == target):
                pos = mid
                return pos
            elif (nums[mid] > target):
                high = mid - 1
            else:
                low = mid + 1    
        return pos            