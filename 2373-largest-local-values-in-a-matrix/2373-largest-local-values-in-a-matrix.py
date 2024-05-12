class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
#         n = len(grid)
#         ans = [[0]*(n-2) for _ in range(n-2)]
        
#         r1,r2,r3 = deque(grid[0][:2]),deque(grid[1][:2]),deque(grid[2][:2])
#         for i in range(1,n-1):
#             r1.append(grid[0][i+1])
#             r2.append(grid[1][i+1])
#             r3.append(grid[2][i+1])
#             maxi = max(r1),max(r2),max(r3)
#             ans[0][i-1] = max(maxi)
#             if len(ans)>1: ans[1][i-1] = max(maxi[1:])
#             if len(ans)>2: ans[2][i-1] = maxi[2]
#             r1.popleft()
#             r2.popleft()
#             r3.popleft()
            
#         r1,r2,r3 = deque(grid[-3][:2]),deque(grid[-2][:2]),deque(grid[-1][:2])
#         for i in range(1,n-1):
#             r1.append(grid[-3][i+1])
#             r2.append(grid[-2][i+1])
#             r3.append(grid[-1][i+1])
#             maxi = max(r1),max(r2),max(r3)
#             if len(ans)>2: ans[-3][i-1] = max(ans[-3][i-1],maxi[0])
#             if len(ans)>1: ans[-2][i-1] = max(maxi[0],maxi[1],ans[-2][i-1])
#             ans[-1][i-1] = max(maxi)
#             r1.popleft()
#             r2.popleft()
#             r3.popleft()
        
#         for i in range(2,n-2):
#             r1 = deque(grid[i+1][:2])
#             for j in range(1,n-1):
#                 r1.append(grid[i+1][j+1])
#                 maxi = max(r1)
#                 ans[i-1][j-1] = max(ans[i-1][j-1],maxi)
#                 if i == 4 and j == 8:
#                     print(ans[i-1][j-1])
#                     print(r1)
#                     break
                
#                 r1.popleft()
                
                
#         return ans
        n, res = len(grid), []

        for i in range(1, n - 1):
            temp_row = []
            for j in range(1, n - 1):
                temp = 0

                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        temp = max(temp, grid[k][l])

                temp_row.append(temp)
            res.append(temp_row)

        return res