class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        sample = [i for i in range(1,n+1)]
        for i in range(n):
            if sorted(matrix[i]) == sorted(matrix[j][i] for j in range(n)) == sample: continue
            return False
        return True