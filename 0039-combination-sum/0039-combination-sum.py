class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()
        def solve(idx, current, total):
            if total == target:
                result.append(current[:])
                return
            if idx == len(candidates) or total > target:
                return
            current.append(candidates[idx])
            solve(idx, current, total + candidates[idx])
            current.pop()
            solve(idx + 1, current, total)
        solve(0, [], 0)
        return result