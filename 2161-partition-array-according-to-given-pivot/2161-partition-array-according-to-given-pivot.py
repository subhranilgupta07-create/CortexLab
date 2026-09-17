class Solution(object):
    def pivotArray(self, nums, pivot):
        A = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                A.append(nums[i])
        for i in range(len(nums)):
            if nums[i] == pivot:
                A.append(nums[i])
        for i in range(len(nums)):
            if nums[i] > pivot:
                A.append(nums[i])
        return A