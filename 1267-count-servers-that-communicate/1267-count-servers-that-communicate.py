class Solution(object):
    def countServers(self, grid):
        R = len(grid)
        C = len(grid[0])
        row = [0] * R
        col = [0] * C
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        S = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1 and (row[i] > 1 or col[j] > 1):
                    S += 1
        return S