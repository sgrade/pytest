# 529. Minesweeper
# https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        rows = len(board)
        cols = len(board[0])
           
        directions = [(r, c) for r in [-1, 0, 1] for c in [-1, 0, 1] if not r == c == 0]
        q = deque()
        q.append(tuple(click))
        while q:
            row, col = q.popleft()
            if board[row][col] != 'E':
                continue
            adjacent_mines = 0
            adjacent_cells = []
            for r, c in directions:
                rr = row + r
                cc = col + c
                if 0 <= rr < rows and 0 <= cc < cols:
                    if board[rr][cc] == 'M':
                        adjacent_mines += 1
                    else:
                        adjacent_cells.append((rr, cc))
            if adjacent_mines == 0:
                board[row][col] = 'B'
                q.extend(adjacent_cells)
            else:
                board[row][col] = str(adjacent_mines)
                
        return board
