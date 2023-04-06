class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols: return False
            if grid[i][j] == 1: return True
            grid[i][j] = 1
            l,r,u,d = dfs(i, j-1),dfs(i, j+1),dfs(i-1, j),dfs(i+1, j)
            return all([l,r,u,d])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and dfs(i, j):
                    count += 1
        
        return count

