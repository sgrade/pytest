from collections import deque


def grid_bfs(grid, start_row, start_col):
    """BFS on grid. Example: shortest path, flood fill."""
    rows, cols = len(grid), len(grid[0])
    visited = {(start_row, start_col)}
    queue = deque([(start_row, start_col, 0)])  # row, col, distance
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        r, c, dist = queue.popleft()
        # process (r, c)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if grid[nr][nc] != 0:  # Adjust condition as needed
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))


def grid_dfs(grid, row, col, visited):
    """DFS on grid. Example: count islands, connected components."""
    rows, cols = len(grid), len(grid[0])
    if row < 0 or row >= rows or col < 0 or col >= cols:
        return
    if (row, col) in visited or grid[row][col] == 0:
        return

    visited.add((row, col))
    # process (row, col)

    grid_dfs(grid, row + 1, col, visited)
    grid_dfs(grid, row - 1, col, visited)
    grid_dfs(grid, row, col + 1, visited)
    grid_dfs(grid, row, col - 1, visited)


def num_islands(grid):
    """Count islands (connected 1s)."""
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                grid_dfs(grid, r, c, visited)
                count += 1
    return count


def rotate_90_clockwise(matrix):
    """Rotate matrix 90 degrees clockwise in-place."""
    n = len(matrix)
    # Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for row in matrix:
        row.reverse()


def spiral_order(matrix):
    """Return elements in spiral order."""
    if not matrix:
        return []
    ans = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            ans.append(matrix[top][c])
        top += 1
        for r in range(top, bottom + 1):
            ans.append(matrix[r][right])
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1):
                ans.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1):
                ans.append(matrix[r][left])
            left += 1
    return ans

