class Solution(object):
    def compress(self, chars):
        c = 1
        A = []
        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                c += 1
            else:
                A.append(chars[i - 1])
                if c > 1:
                    A.extend(list(str(c)))
                c = 1
        A.append(chars[-1])
        if c > 1:
            A.extend(list(str(c)))
        for i in range(len(A)):
            chars[i] = A[i]
        return len(A)