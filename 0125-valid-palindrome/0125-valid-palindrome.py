class Solution(object):
    def isPalindrome(self, s):
        s1 = ""
        for i in range (0, len(s)):
            if s[i].isalnum():
                s1 += s[i]
        s1 = s1.lower()
        if s1 == s1[::-1]:
            return True
        else:
            return False    