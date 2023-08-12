class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n,m = len(obstacleGrid),len(obstacleGrid[0])
        last = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            if obstacleGrid[i][0]: break
            last[i][0] = 1
        for i in range(m):
            if obstacleGrid[0][i]: break
            last[0][i] = 1
        
        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j]: continue
                last[i][j] = (last[i-1][j] if not obstacleGrid[i-1][j] else 0) + (last[i][j-1] if not obstacleGrid[i][j-1] else 0)
        
        return last[-1][-1]