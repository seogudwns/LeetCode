# class Solution:
#     def uniquePathsIII(self, grid: List[List[int]]) -> int:
#         n,m = len(grid),len(grid[0])
#         cnt = 0
#         stt,end = 0,0
#         check = [0 for _ in range(n)]
#         rot = [(1,0),(0,1),(-1,0),(0,-1)]
#         res = 0
        
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == 0:
#                     cnt += 1
#                     check[i] += 2**j
#                 elif grid[i][j] == 1:
#                     stt = (i,j)
#                 elif grid[i][j] == 2:
#                     end = (i,j)
#         check[stt[0]] += 2**stt[1]
        
#         print(check)
            
#         Q = [(stt[0],stt[1],0,check)]
#         while Q:
#             x,y,dist,check = Q.pop()
#             if (x,y) == end:
#                 if dist == cnt:
#                     res += 1
#                 continue
                
#             for i,j in rot:
#                 nx,ny = x+i,y+j
#                 if 0<=nx<n and 0<=ny<m:
#                     if not check[nx] & 2**ny:
#                         continue
#                     check[nx] -= 2**ny
#                     print(nx,ny,check)
#                     Q.append((nx,ny,dist+1,check))
#                     check[nx] += 2**ny
        
#         return res

# Others.. 시간이 없당..ㅇㅅㅇ
class Solution:
     def uniquePathsIII(self, grid: list[list[int]]) -> int:

        M, N = range(len(grid)), range(len(grid[0]))

        zeros = sum(row.count(0) for row in grid)       # count the zeros to ensure all cells visited
        start = tuple((r,c) for r in M for c in N       # find start in grid
                           if grid[r][c] == 1)[0]
        self.ans = 0

        def dfs(row, col, zeros):
            grid[row][col] = 3                          # change 0 to 3 to avoid returning

            for dr, dc in ((-1,0),(0,-1),(1,0),(0,1)):  # explore the grid recursively
                R, C = row+dr, col+dc
                if R in M and C in N:
                    if grid[R][C] == 0: dfs(R, C, zeros-1)
                    if grid[R][C] == 2 and zeros == 0: self.ans += 1

            grid[row][col] = 0                          # change back
            return

        dfs(*start, zeros)
        return self.ans