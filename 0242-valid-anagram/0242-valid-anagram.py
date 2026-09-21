class Solution(object):
    def isAnagram(self, s, t):
        A = []
        B = []
        for i in range (len(s)):
            A.append(s[i])
        for i in range (len(t)):
            B.append(t[i]) 
        A.sort()
        B.sort()    
        if (A == B):
            return True
        else:
            return False            