class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        def dfs(r,c):
            if grid[r][c] == 0:
                return
            
            nonlocal area
            area += 1
            grid[r][c] = 0

            if c - 1 >= 0:
                dfs(r, c - 1)
            if c + 1 < len(grid[r]):
                dfs(r, c + 1)
            if r - 1 >= 0:
                dfs(r - 1, c)
            if r + 1 < len(grid):
                dfs(r + 1, c)


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i,j)
                    max_area = max(max_area, area)

        return max_area