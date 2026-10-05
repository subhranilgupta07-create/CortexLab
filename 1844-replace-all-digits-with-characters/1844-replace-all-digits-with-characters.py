import re
class Solution(object):
    def replaceDigits(self, s):
        ch = 'a'
        a = ""
        for i in range(len(s)):
            if re.match(r"[0-9]", s[i]):
                a += chr(ord(ch) + int(s[i]))
            else:
                a += s[i]
                ch = s[i]
        return a