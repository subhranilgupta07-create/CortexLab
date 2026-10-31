class Solution(object):
    def minSwaps(self, nums):
        c = 0
        A = []
        for i in range(len(nums)):
            S = 0
            n = nums[i]
            while n > 0:
                S += n % 10
                n //= 10
            A.append((S, nums[i]))
        B = sorted(A)
        pos = {nums[i]: i for i in range(len(nums))}
        visited = [False] * len(nums)
        for i in range(len(nums)):
            if visited[i] or A[i] == B[i]:
                continue
            cycle = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = pos[B[j][1]]
                cycle += 1
            c += cycle - 1
        return c