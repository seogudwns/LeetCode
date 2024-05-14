class Solution:
    def dfs(self,bef,x,y):
        tmp = 0
        for i,j in self.rot:
            nx,ny = x+i,y+j
            if 0<=nx<self.n and 0<=ny<self.m  and not self.mining[nx][ny] and self.grid[nx][ny]:
                self.mining[nx][ny] = True
                tmp = max(tmp,self.grid[nx][ny]+self.dfs((x,y),nx,ny))
                self.mining[nx][ny] = False
        
        self.ans = max(self.ans,tmp)
        
        return tmp
                
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.n,self.m = len(grid),len(grid[0])
        self.rot = [(0,1),(1,0),(0,-1),(-1,0)]
        self.ans = 0
        self.grid,self.mining = grid,[[False]*self.m for _ in range(self.n)]
        
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j]:
                    self.mining[i][j] = True
                    self.ans = max(self.ans,self.grid[i][j]+self.dfs((-1,-1),i,j))
                    self.mining[i][j] = False
                    
        return self.ans