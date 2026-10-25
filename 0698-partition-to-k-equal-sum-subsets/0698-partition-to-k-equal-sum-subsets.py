class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)
        if total % k != 0 or len(nums) < k:
            return False
        target = total // k
        nums.sort(reverse=True)
        subsets = [[] for _ in range(k)]
        sums = [0] * k
        def solve(idx):
            if idx == len(nums):
                return all(s == target for s in sums)
            for i in range(k):
                if sums[i] + nums[idx] <= target:
                    subsets[i].append(nums[idx])
                    sums[i] += nums[idx]
                    if solve(idx + 1):
                        return True
                    sums[i] -= nums[idx]
                    subsets[i].pop()
                if not subsets[i]:
                    break
            return False
        return solve(0)