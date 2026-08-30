class Solution:
    def diagonalSum(self, mat):
        a = 0
        b = 0

        for i in range(len(mat)):
            for j in range(len(mat)):
                if i == j:
                    a += mat[i][j]
                elif (i + j == len(mat) - 1) and (i != j):
                    b += mat[i][j]

        return a + b