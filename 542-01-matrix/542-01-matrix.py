from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def check(i,j):
            nonlocal m,n
            for k in directions:
                x1, y1 = i+k[0], j+k[1]
                if x1<0 or y1<0 or x1 == m or y1 == n:
                    continue
                if mat[x1][y1] == 0:
                    return True
            return False
                
        Q = deque()
        result = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and check(i,j):
                    Q.append((i,j,1))
                    result[i][j] = 1
                    
        # ! 탑... 겁나 거슬리는데... 쉬운 방법이 있을까?
        
        while Q:
            x,y,val = Q.popleft()
            for i in directions:
                x1,y1 = x+i[0],y+i[1]
                if x1<0 or y1<0 or x1 == m or y1 == n:
                    continue
                if (mat[x1][y1] == 1 and result[x1][y1] == 0):
                    result[x1][y1] = val+1
                    Q.append((x1,y1,val+1))
                    
        return result
'''

'''