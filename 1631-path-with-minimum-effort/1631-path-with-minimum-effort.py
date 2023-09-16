class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])
        rot = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = [[10**6 for _ in range(col)] for _ in range(row)]
        dist[0][0] = 0
        minHeap = [(0, 0, 0)] 
        
        while minHeap:
            e, x, y = heappop(minHeap)
            if e>dist[-1][-1]: continue

            if x == row - 1 and y == col - 1:
                return dist[-1][-1]
            
            for dx, dy in rot:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < row and 0 <= ny < col:
                    ne = max(e, abs(heights[x][y] - heights[nx][ny]))
                    
                    if ne < dist[nx][ny]:
                        dist[nx][ny] = ne
                        heappush(minHeap, (ne, nx, ny))
        
#         # TLE..
#         row,col,ans = len(heights[0]),len(heights),10**6+1
#         rot = [(0,1),(1,0),(0,-1),(-1,0)]
#         chk = [[True]*row for _ in range(col)]
#         chk2 = [[ans]*row for _ in range(col)]
        
#         @lru_cache(None)
#         def backt(x,y,curr):
#             # print(x,y,curr)
#             if chk2[y][x]<curr: return
#             chk2[y][x] = curr
#             nonlocal ans
#             if curr>ans: return
#             if x == row-1 and y == col-1:
#                 ans = min(ans,curr)
#                 return
#             for i,j in rot:
#                 nx,ny = x+i,y+j
#                 if 0<=nx<=row-1 and 0<=ny<=col-1 and chk[ny][nx]:
#                     chk[ny][nx] = False
#                     backt(nx,ny,max(curr,abs(heights[y][x]-heights[ny][nx])))
#                     chk[ny][nx] = True
            
#         backt(0,0,0)
#         return ans
        
#         # (From 마지막 ex..) dp 안됨.            
#         for i in range(1,row): ans[0][i] = max(ans[0][i-1],abs(heights[0][i]-heights[0][i-1]))
#         for i in range(1,col): ans[i][0] = max(ans[i-1][0],abs(heights[i][0]-heights[i-1][0]))
        
#         for i in range(1,row):
#             for j in range(1,col):
#                 ans[i][j] = min(max(ans[i-1][j],abs(heights[i][j]-heights[i-1][j])),max(ans[i][j-1],abs(heights[i][j]-heights[i][j-1])))
        
#         return ans[-1][-1]