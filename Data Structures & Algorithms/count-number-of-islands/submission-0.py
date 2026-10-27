class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            if grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            if c + 1 < len(grid[r]):
                dfs(r, c + 1)
            if c - 1 >= 0:
                dfs(r, c - 1)
            if r - 1 >= 0:
                dfs(r - 1, c)
            if r + 1 < len(grid):
                dfs(r + 1, c)

            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i,j)

        return count

