class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        x = 0
        for i in range(n):
            if matrix[i][0] > target:
                x = i-1
                break
            elif matrix[i][0] == target:
                return True
        if matrix[i][0] < target:
            x = i
        
        if x == -1:
            return False
        
        return target in matrix[x]