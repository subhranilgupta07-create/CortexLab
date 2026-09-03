class Solution(object):
    def generate(self, numRows):
        A = []
        for i in range (numRows):
            B = []
            for j in range (i + 1):
                if (j == 0 or j == i):
                    B.append(1)
                else:
                    B.append(A[i - 1][j - 1] + A[i - 1][j])
            A.append(B)    
        return A    