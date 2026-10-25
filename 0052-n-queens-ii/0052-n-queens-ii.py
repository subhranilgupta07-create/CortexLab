class Solution(object):
    def totalNQueens(self, n):
        allBoards = []
        board = [['.' for j in range(n)] for i in range(n)]
        self.BT(board, allBoards, 0)
        return len(allBoards)
    def BT(self, board, allBoards, col):
        if col == len(board):
            self.saveBoard(board, allBoards)
            return
        for row in range(len(board)):
            if self.isSafe(board, row, col):
                board[row][col] = 'Q'
                self.BT(board, allBoards, col + 1)
                board[row][col] = '.'
    def isSafe(self, board, row, col):
        for i in range(len(board)):
            if board[row][i] == 'Q':
                return False
        for i in range(len(board)):
            if board[i][col] == 'Q':
                return False
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        i, j = row, col
        while i < len(board) and j >= 0:
            if board[i][j] == 'Q':
                return False
            i += 1
            j -= 1
        i, j = row, col
        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True
    def saveBoard(self, board, allBoards):
        newBoard = []
        for i in range(len(board)):
            row = ""
            for j in range(len(board)):
                if board[i][j] == 'Q':
                    row += 'Q'
                else:
                    row += '.'
            newBoard.append(row)
        allBoards.append(newBoard)