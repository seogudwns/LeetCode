class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]: return -1
        n,m = len(grid),len(grid[0])
        rot = [(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]
        grid[0][0] = 1
        Q = deque([(0,0)])
            
        while Q:
            x,y = Q.popleft()
            curr = grid[x][y]
            for i,j in rot:
                nx,ny = x+i,y+j
                if nx==-1 or nx == n or ny==-1 or ny == m or grid[nx][ny]:
                    continue
                Q.append((nx,ny))
                grid[nx][ny] = curr+1
                
            if grid[-1][-1]:
                return grid[-1][-1]
            
        return -1