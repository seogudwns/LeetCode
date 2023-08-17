class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        rot = [(1,0),(0,1),(-1,0),(0,-1)]
        def check(i,j):
            for a,b in rot:
                x1, y1 = i+a, j+b
                if 0<=x1<m and 0<=y1<n and mat[x1][y1] == 0:
                    return True
            return False
                
        Q = deque()
        result = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and check(i,j): Q.append((i,j,1)); result[i][j] = 1
        
        while Q:
            x,y,val = Q.popleft()
            for i,j in rot:
                x1,y1 = x+i,y+j
                if 0<=x1<m and 0<=y1<n and mat[x1][y1] == 1 and result[x1][y1] == 0:
                    result[x1][y1] = val+1
                    Q.append((x1,y1,val+1))
                    
        return result