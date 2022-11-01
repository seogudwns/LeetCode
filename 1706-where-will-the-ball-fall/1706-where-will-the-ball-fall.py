class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m,n = len(grid),len(grid[0])
        def check(i,j):
            if i == m:
                return j
            if grid[i][j] == 1:
                if j == n-1 or grid[i][j+1] == -1:
                    return -1
                else:
                    return check(i+1,j+1)
            
            else:
                if j == 0 or grid[i][j-1] == 1:
                    return -1
                else:
                    return check(i+1,j-1)
        
        return [check(0,i) for i in range(n)]