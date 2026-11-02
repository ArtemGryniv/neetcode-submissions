from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i,j))
        
        if not q:
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == 1:
                        return -1
            return 0

        minute = -1
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()

                if c - 1 >= 0 and grid[r][c-1] == 1:
                    grid[r][c - 1] = 2
                    q.append((r, c - 1))
                
                if c + 1 < len(grid[r]) and grid[r][c+1] == 1:
                    grid[r][c + 1] = 2
                    q.append((r, c + 1))

                if r - 1 >= 0 and grid[r-1][c] == 1:
                    grid[r-1][c] = 2
                    q.append((r - 1, c))

                if r + 1 < len(grid) and grid[r+1][c] == 1:
                    grid[r+1][c] = 2
                    q.append((r + 1, c))

            minute += 1

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1

        return minute 
                