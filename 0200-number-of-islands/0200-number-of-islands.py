class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        n,m = len(grid),len(grid[0])
        rot = [(0,1),(1,0),(0,-1),(-1,0)]
        
        def dfs(a,b):
            grid[a][b] = 0
            for i,j in rot:
                na,nb = a+i,b+j
                if 0<=na<n and 0<=nb<m and grid[na][nb] == "1":
                    dfs(na,nb)
            return
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i,j)
        
        return ans