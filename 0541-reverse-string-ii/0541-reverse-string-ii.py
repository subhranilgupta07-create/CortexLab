class Solution(object):
    def reverseStr(self, s, k):
        for i in range (0, len(s), 2*k):
            s1 = s[i:i + k]
            s1 = s1[::-1]
            s = s[:i] + s1 + s[i+k:]
        return s        