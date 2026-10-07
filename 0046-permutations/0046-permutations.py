class Solution(object):
    def permute(self, nums):
        answer = []
        def perm(nums, permutation):
            if len(nums) == 0:
                answer.append(permutation[:])
                return
            for i in range(len(nums)):
                currChar = nums[i]
                newnums = []
                for j in range(i):
                    newnums.append(nums[j])
                for j in range(i + 1, len(nums)):
                    newnums.append(nums[j])
                permutation.append(currChar)
                perm(newnums, permutation)
                permutation.pop()
        perm(nums, [])
        return answer