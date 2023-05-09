# 529. Minesweeper
# https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        rows = len(board)
        cols = len(board[0])

        diff_r = diff_c = [-1, 0, 1]

        def count_mines(row, col):
            adjacent_mines = 0
            for r in diff_r:
                for c in diff_c:
                    if r == 0 and c == 0:
                        continue
                    rr = row + r
                    cc = col + c
                    if rr < 0 or rr >= rows or cc < 0 or cc >= cols:
                        continue
                    if board[rr][cc] == 'M':
                        adjacent_mines += 1
            return adjacent_mines
            
        q = deque()
        q.append(click)
        while len(q) > 0:
            row, col = q.popleft()
            if board[row][col] != 'E':
                continue
            adjacent_mines = count_mines(row, col)
            if adjacent_mines != 0:
                board[row][col] = str(adjacent_mines)
                continue
            board[row][col] = 'B'
            for r in diff_r:
                for c in diff_c:
                    if r == 0 and c == 0:
                        continue
                    rr = row + r
                    cc = col + c
                    if rr < 0 or rr >= rows or cc < 0 or cc >= cols or board[rr][cc] != 'E':
                        continue
                    q.append([rr, cc])
        
        return board
