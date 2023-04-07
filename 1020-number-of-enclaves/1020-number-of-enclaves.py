class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ans,n,m = 0,len(grid),len(grid[0])
        lr,ud = (0,1,0,-1),(1,0,-1,0)
        def dfs(i,j):
            grid[i][j] = 0

            a,b = 1,1
            for k in range(4):
                ni,nj = i+lr[k],j+ud[k]
                if 0<=ni<n and 0<=nj<m and grid[ni][nj]:
                    c,d = dfs(ni,nj)
                    a+=c
                    b*=d
            if i == 0 or i == n-1 or j == 0 or j == m-1: return 0,0
            return a,b
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    a,b = dfs(i,j)
                    ans += a*b
        
        return ans