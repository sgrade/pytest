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
            
        q = deque()
        q.append(click)
        while q:
            row, col = q.popleft()
            if board[row][col] != 'E':
                continue
            adjacent_mines = 0
            adjacent_cells = []
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
                    else:
                        adjacent_cells.append([rr, cc])
            if adjacent_mines != 0:
                board[row][col] = str(adjacent_mines)
            else:
                board[row][col] = 'B'
                q.extend(adjacent_cells)
        return board
