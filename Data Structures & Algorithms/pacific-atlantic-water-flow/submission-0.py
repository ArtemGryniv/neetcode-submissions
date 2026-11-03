class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(r,c, visited):
            if (r,c) in visited:
                return 
            
            visited.add((r,c))
            
            if r + 1 < len(heights) and (r + 1,c) not in visited and heights[r + 1][c] >= heights[r][c]:
                dfs(r+1,c, visited)

            if r - 1 >= 0 and (r - 1,c) not in visited and heights[r - 1][c] >= heights[r][c]:
                dfs(r-1,c, visited)
            
            if c + 1 < len(heights[r]) and (r,c + 1) not in visited and heights[r][c + 1] >= heights[r][c]:
                dfs(r,c+1, visited)
            
            if c - 1 >= 0 and (r,c - 1) not in visited and heights[r][c - 1] >= heights[r][c]:
                dfs(r,c - 1, visited)


        pacific_boarder = []
        atlantic_boarder = []
        rows = len(heights)
        columns = len(heights[0])
        for i in range(rows):
            pacific_boarder.append((i, 0))
            atlantic_boarder.append((i, columns - 1))
        
        for j in range(1, columns):
            pacific_boarder.append((0, j))

        for j in range(columns - 1):
            atlantic_boarder.append((rows - 1, j))

        visited_pacific = set()
        for tile in pacific_boarder:
            r,c = tile
            dfs(r,c, visited_pacific)

        visited_atlantic = set()
        for tile in atlantic_boarder:
            r,c = tile
            dfs(r,c, visited_atlantic)

        combined = visited_pacific & visited_atlantic
        out = []
        for tile in combined:
            out.append(list(tile))

        return out