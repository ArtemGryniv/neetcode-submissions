from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))

        level = 0
        land = 2 ** 31 - 1
        while q:
            for _ in range(len(q)):
                cell = q.popleft()
                r,c = cell
                grid[r][c] = level

                if r + 1 < len(grid) and grid[r + 1][c] == land and (r + 1, c) not in visited:
                    q.append((r + 1, c))
                    visited.add((r + 1, c))
                if r - 1 >= 0  and grid[r - 1][c] == land and (r - 1, c) not in visited:
                    q.append((r - 1, c))
                    visited.add((r - 1, c))
                if c + 1 < len(grid[r]) and grid[r][c + 1] == land and (r, c + 1) not in visited:
                    q.append((r, c + 1))
                    visited.add((r, c + 1))
                if c - 1 >= 0 and grid[r][c - 1] == land and (r, c - 1) not in visited:
                    q.append((r, c - 1))
                    visited.add((r, c - 1))

            level += 1
