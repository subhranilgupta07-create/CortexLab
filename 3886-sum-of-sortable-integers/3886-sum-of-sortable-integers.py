class Solution(object):
    def sortableIntegers(self, nums):
        def is_cyclic_sorted(arr):
            n = len(arr)
            count = 0
            for i in range(n):
                if arr[i] > arr[(i + 1) % n]:
                    count += 1
            return count <= 1
        divisors = []
        n = len(nums)
        valid = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        for k in divisors:
            A = []
            for j in range(0, n, k):
                A.append(nums[j:j+k])
            possible = True
            prev = float('-inf')
            for x in A:
                if not is_cyclic_sorted(x):
                    possible = False
                    break
                drop = -1
                for t in range(k):
                    if x[t] > x[(t+1) % k]:
                        drop = t
                        break
                first = x[(drop+1) % k]
                last = x[drop]
                if first < prev:
                    possible = False
                    break
                prev = last
            if possible:
                valid.append(k)
        return sum(valid)