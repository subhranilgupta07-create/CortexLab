class Solution(object):
    def groupAnagrams(self, strs):
        A = []
        for i in range(len(strs)):
            A.append("".join(sorted(strs[i])))
        visited = [False] * len(strs)
        ans = []
        for i in range(len(A)):
            if visited[i]:
                continue
            temp = []
            for j in range(len(A)):
                if A[i] == A[j] and not visited[j]:
                    temp.append(strs[j])
                    visited[j] = True
            ans.append(temp)
        return ans