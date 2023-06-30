# class Solution:
#     def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
#         col_chk = {i for i in range(1,col+1)}
#         wat = [set() for i in range(col)]
#         days=0
#         cells = deque(cells)
#         while col_chk:
#             i,j = cells.popleft()
#             col_chk.discard(j)
#             wat[j-1].add(i-1)
#             days+=1
            
#         while True:
#             print(days,wat)
#             stt,idx,nex = wat[0],0,set()
#             while stt:
#                 idx+=1
#                 if idx == col: 
#                     return days-1
                
#                 for i in stt:
#                     for j in range(max(0,i-1),min(row,i+2)):
#                         if j in wat[idx]:
#                             nex.add(j)
#                 stt,nex = nex,set()
            
                
#             i,j = cells.popleft()
#             wat[j-1].add(i-1)
#             days+=1
        
#         return -1


class Solution:
    def is_possible(self, mid, n, m, cells):
        grid = [[0] * m for _ in range(n)]
        for i in range(mid):
            row, col = cells[i]
            grid[row - 1][col - 1] = 1
        
        # Check if there is a path from the first row to the last row
        visited = set()
        stack = [(0, col) for col in range(m) if grid[0][col] == 0]
        
        while stack:
            row, col = stack.pop()
            if row == n - 1:
                return True
            
            if (row, col) in visited:
                continue
            visited.add((row, col))
            
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] == 0:
                    stack.append((new_row, new_col))
        
        return False

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        left, right = 1, len(cells)
        result = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            if self.is_possible(mid, row, col, cells):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result
