class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        rot = [(0,1),(1,0),(0,-1),(-1,0)]
        
        @lru_cache(None)
        def cnt(i,j):
            ans = 1
            nonlocal rot
            for a,b in rot:
                ni,nj = i+a,j+b
                if 0<=ni<n and 0<=nj<m and grid[ni][nj]>grid[i][j]:
                    ans += cnt(ni,nj)
            
            return ans%M
        
        ans,M = 0,10**9+7
        for i in range(n):
            for j in range(m):
                ans = (ans+cnt(i,j))%M
        
        return ans