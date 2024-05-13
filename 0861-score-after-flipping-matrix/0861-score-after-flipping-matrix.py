class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        ans,n,m = 0,len(grid),len(grid[0])
        for i in range(n):
            if not grid[i][0]:
                grid[i] = [0 if grid[i][j] else 1 for j in range(m)]
        
        for i in range(m):
            tmp = sum(grid[j][i] for j in range(n))
            ans *= 2
            ans += max(n - tmp,tmp)
        
        return ans
            
            
            