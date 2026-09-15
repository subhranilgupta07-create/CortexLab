class Solution(object):
    def reverseOnlyLetters(self, s):
        s1 = ""
        for i in range (len(s)):
            if (s[i].isalpha()):
                s1 += s[i]
        s1 = s1[::-1]
        s2 = ""
        j = 0
        for i in range (len(s)):
            if (s[i].isalpha()):
                s2 += s1[j]
                j += 1
            else:
                s2 += s[i]
        return s2                 