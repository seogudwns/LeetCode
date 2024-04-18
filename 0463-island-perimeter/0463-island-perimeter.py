class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        n,m = len(grid),len(grid[0])
        rot = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    for x,y in rot:
                        ni,nj = i+x,j+y
                        if ni<0 or nj < 0 or ni == n or nj == m or not grid[ni][nj]:
                            ans += 1
        
        return ans