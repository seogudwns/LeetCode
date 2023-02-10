class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        if sum(sum(grid,[])) in {0,n*m}: return -1
        
        bef,aft,leng,rot = [],[],1,[(-1,0),(1,0),(0,1),(0,-1)]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]: bef.append((i,j))
        
        while True:
            while bef:
                x,y = bef.pop()
                for i,j in rot:
                    nx,ny = x+i,y+j
                    if 0<=nx<n and 0<=ny<m and not grid[nx][ny]:
                        grid[nx][ny] = leng
                        aft.append((nx,ny))
                        
            bef,aft = aft,[]
            
            leng += 1
            if not bef:
                return max(sum(grid,[]))