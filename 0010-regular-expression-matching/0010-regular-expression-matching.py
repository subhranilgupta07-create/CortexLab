import re
class Solution(object):
    def isMatch(self, s, p):
        if re.match("^" + p + "$", s):
            return True
        else:
            return False