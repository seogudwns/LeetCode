class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m = len(matrix),len(matrix[0])
        row,col = set(),set()
        for i in range(n):
            for j in range(m):
                if not matrix[i][j]:
                    row.add(j)
                    col.add(i)
        
        zeros = [0 for _ in range(m)]
        
        for i in range(n):
            if i in col:
                matrix[i] = zeros
                continue
            for j in range(m):
                if j in row:
                    matrix[i][j] = 0
        
        return matrix