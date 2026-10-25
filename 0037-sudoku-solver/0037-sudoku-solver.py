class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + c // 3].add(num)
        def BT(idx):
            if idx == len(empty):
                return True
            best = idx
            best_candidates = None
            for k in range(idx, len(empty)):
                r, c = empty[k]
                b = (r // 3) * 3 + c // 3
                candidates = [
                    str(n) for n in range(1, 10)
                    if str(n) not in rows[r]
                    and str(n) not in cols[c]
                    and str(n) not in boxes[b]
                ]
                if not candidates:
                    return False
                if best_candidates is None or len(candidates) < len(best_candidates):
                    best = k
                    best_candidates = candidates
                if len(best_candidates) == 1:
                    break
            empty[idx], empty[best] = empty[best], empty[idx]
            r, c = empty[idx]
            b = (r // 3) * 3 + c // 3
            if best != idx:
                best_candidates = [
                    str(n) for n in range(1, 10)
                    if str(n) not in rows[r]
                    and str(n) not in cols[c]
                    and str(n) not in boxes[b]
                ]
            for num in best_candidates:
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[b].add(num)
                if BT(idx + 1):
                    return True
                board[r][c] = '.'
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[b].remove(num)
            empty[idx], empty[best] = empty[best], empty[idx]
            return False
        BT(0)