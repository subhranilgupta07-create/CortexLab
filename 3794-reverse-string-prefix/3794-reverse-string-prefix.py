class Solution(object):
    def reversePrefix(self, s, k):
        s1 = ""
        s1 = (s[0:k])[::-1]
        s1 += s[k:]
        return s1