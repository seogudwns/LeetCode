class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0]*(n-2) for _ in range(n-2)]
        
        for i in range(n):
            r1 = deque(grid[i][:2])
            for j in range(1,n-1):
                r1.append(grid[i][j+1])
                maxi = max(r1)
                if i<n-2: ans[i][j-1] = max(ans[i][j-1],maxi)
                if 0<i<n-1: ans[i-1][j-1] = max(ans[i-1][j-1],maxi)
                if 1<i<n: ans[i-2][j-1] = max(ans[i-2][j-1],maxi)
                    
                r1.popleft()
                
        return ans