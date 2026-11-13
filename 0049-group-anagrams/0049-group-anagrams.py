class Solution(object):
    def groupAnagrams(self, strs):
        A = []
        ans = []
        for i in range(len(strs)):
            A.append("".join(sorted(strs[i])))
        for i in range(len(A)):
            found = False
            for j in range(len(ans)):
                if A[i] == ans[j][0]:
                    ans[j].append(strs[i])
                    found = True
                    break
            if not found:
                ans.append([A[i], strs[i]])
        for i in range(len(ans)):
            ans[i].pop(0)
        return ans