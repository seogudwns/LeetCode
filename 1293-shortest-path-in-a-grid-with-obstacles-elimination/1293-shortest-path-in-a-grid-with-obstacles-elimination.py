class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # basic bfs.. k를 고려해야하는군.. from hint
        m, n = len(grid), len(grid[0])
        # for i in range(m):
        #     print(grid[i])
        if n==m==1:
            return 0
        
        rot = [(1,0),(0,1),(0,-1),(-1,0)]
        Q = deque([(0,0,k,0)])
        seen = set()
        while Q:
            y,x,res,leng = Q.popleft()
            if (y,x,res) in seen or res<0:
                continue
            if y == m-1 and x == n-1:
                return leng
            seen.add((y,x,res))
            
            if grid[y][x] == 1:
                res -= 1
                
            for i,j in rot:
                ynew, xnew = y+i, x+j
                if 0<=ynew<m and 0<=xnew<n:
                    Q.append((ynew,xnew,res,leng+1))
            
        return -1