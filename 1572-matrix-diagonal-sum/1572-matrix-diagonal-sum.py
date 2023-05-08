class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = sum(mat[i][i]+mat[i][n-1-i] for i in range(n))
        return ans if not n%2 else ans-mat[n//2][n//2]