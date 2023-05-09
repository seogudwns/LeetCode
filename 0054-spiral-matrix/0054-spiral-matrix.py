class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix),len(matrix[0])
        if m == 1:
            return matrix[0]
        elif n == 1:
            return [matrix[i][0] for i in range(m)]

        m-=1
        res = []
        x,y,idx = 0,-1,0
        rot = [(0,1),(1,0),(0,-1),(-1,0)]
        while m != -1 and n != -1:
            # print(x,y,m,n)
            dx,dy = rot[idx]
            if not idx%2: # row
                for i in range(n):
                    y += dy
                    # print(x,y)
                    res.append(matrix[x][y])
                n -= 1

            else:
                for i in range(m):
                    x += dx
                    # print(x,y)
                    res.append(matrix[x][y])
                m -= 1
            
            idx = (idx+1)%4
        
        return res