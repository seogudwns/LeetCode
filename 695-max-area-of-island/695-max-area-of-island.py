class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        Q = set()
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt = 0
                    Q.add((i,j))
                    
                    while Q:
                        x,y = Q.pop()
                        grid[x][y] = 0
                        cnt += 1
                        if 0<x and grid[x-1][y] == 1:
                            Q.add((x-1,y))
                        if 0<y and grid[x][y-1] == 1:
                            Q.add((x,y-1))
                        if x<m-1 and grid[x+1][y] == 1:
                            Q.add((x+1,y))
                        if y<n-1 and grid[x][y+1] == 1:
                            Q.add((x,y+1))
                        # print('Q :',Q)
                    result = max(result,cnt)
                    # print(grid,cnt)
                
                            
                
        # 초기 : deque를 사용했으나 같은 원소가 들어갈 수 있다는 것을 고려하지 못함.
        return result