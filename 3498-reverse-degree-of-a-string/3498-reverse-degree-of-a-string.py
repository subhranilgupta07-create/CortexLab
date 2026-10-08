class Solution(object):
    def reverseDegree(self, s):
          S = 0
          for i in range (len(s)):
            S += (123 - ord(s[i])) * (i + 1)
          return S  