from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m,n = len(image),len(image[0])
        
        Q = deque([(sr,sc)])
        first = image[sr][sc]
        if first == color:
            return image
        
        while Q:
            r,c=  Q.popleft()
            image[r][c] = color
            if r>0:
                if image[r-1][c] == first:
                    Q.append((r-1,c))
            if c>0:
                if image[r][c-1] == first:
                    Q.append((r,c-1))
            if r<m-1:
                if image[r+1][c] == first:
                    Q.append((r+1,c))
            if c<n-1:
                if image[r][c+1] == first:
                    Q.append((r,c+1))
        return image
                
                
                