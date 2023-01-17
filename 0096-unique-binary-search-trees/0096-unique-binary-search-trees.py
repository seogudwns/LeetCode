'1,2,5,14,42,132'
class Solution:
    def numTrees(self, n: int) -> int:
        res = 1
        for i in range(n+2,2*n+1):
            res *= i
        for i in range(1,n+1):
            res //= i
        return res