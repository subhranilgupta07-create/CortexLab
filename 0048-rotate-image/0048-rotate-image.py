class Solution(object):
    def rotate(self, matrix):
        matrix[:] = [list(row) for row in zip(*matrix)]
        for i in range (len(matrix)):
            for j in range (len(matrix)//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][len(matrix)-j-1]
                matrix[i][len(matrix)-j-1] = temp