class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:        
        leng = len(grid)
        if leng == 1: return 0
        dep = [0 for _ in range(leng**2)]
        for i in range(leng):
            for j in range(leng):
                dep[grid[i][j]] = (i,j)
        dp = [[False for _ in range(leng)] for _ in range(leng)]
        dp[0][0] = True
        n,Q = max(grid[0][0],grid[-1][-1]),deque([(0,0)])
        candid,rot = set(),[(-1,0),(0,1),(1,0),(0,-1)]
        while n<leng**2:
            while Q:
                x,y = Q.popleft()
                for i,j in rot:
                    nx,ny = x+i,y+j
                    if 0<=nx<leng and 0<=ny<leng:
                        if nx == ny == leng-1: return n
                        if dp[nx][ny]:
                            continue
                        elif grid[nx][ny]<=n:
                            Q.append((nx,ny))
                            dp[nx][ny] = True
                        else:
                            candid.add(grid[nx][ny])

            mini = min(candid)
            for i in range(n+1,mini+1):
                if i in candid:
                    Q.append((dep[i]))
                    dp[dep[i][0]][dep[i][1]] = True
            n = mini
            candid.discard(n)
        return n
        