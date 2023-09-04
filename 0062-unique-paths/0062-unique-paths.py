class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
# #         정석
#         dp = [[0]*m for _ in range(n)]
#         for i in range(m):
#             dp[0][i] = 1
#         for i in range(n):
#             dp[i][0] = 1
        
#         for i in range(1,n):
#             for j in range(1,m):
#                 dp[i][j] = dp[i-1][j]+dp[i][j-1]
        
#         return dp[-1][-1]
        if n>m: n,m = m,n
        if n == 1: return 1
        def mul(a,b):
            if b <= 1: return a
            return a*mul(a+1,b-1)
        return (mul(m,n-1)//mul(1,n-1))