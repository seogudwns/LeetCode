from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        Q = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    Q.append((i,j,2))
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        while Q:
            x = Q.popleft()
            for i in directions:
                du,lr,val = x[0]+i[0],x[1]+i[1],x[2]
                if du<0 or du>m-1 or lr<0 or lr>n-1:
                    continue
                if grid[du][lr] == 1:
                    grid[du][lr] += val
                    Q.append((du,lr,val+1))
                    
        lst = sum(grid,[])
        if max(lst) == 0:
            return 0
        elif 1 in lst:
            return -1
        else:
            return max(lst)-2