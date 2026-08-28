class Solution(object):
    def longestCommonPrefix(self, strs):
        a = ""
        for i in range(len(strs)-1):
            a = ""                         
            for j in range(min(len(strs[i]), len(strs[i+1]))):
                if strs[i][j] == strs[i+1][j]:
                    a += strs[i][j]
                else:
                    break  
            strs[i+1] = a
        return strs[len(strs)-1]