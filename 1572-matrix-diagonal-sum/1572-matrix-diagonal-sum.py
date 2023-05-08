class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n,ans = len(mat),0
        for i in range(n): ans += mat[i][i]+mat[i][n-1-i]
        return ans if not n%2 else ans-mat[n//2][n//2]