class Solution(object):
    def isPalindrome(self, s):
        s1 = ""
        for i in range(len(s)):
            if s[i].isalnum():
                s1 += s[i].lower()
        return s1 == s1[::-1]