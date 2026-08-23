class Solution(object):
    def lengthOfLastWord(self, s):
        c = 0
        for i in range (len(s)-1, -1, -1):
            if (s[i].isalpha()):
                c += 1
            elif (s[i] == ' ' and c != 0):
                break
        return c           