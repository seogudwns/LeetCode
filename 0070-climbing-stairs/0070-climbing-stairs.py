# n = 4 case.
# 1 1 1 1
# 1 1 2
# 1 2 1
# 2 1 1
# 2 2

# n = 5
# 1 1 1 1 1
# 1 1 1 2
# 1 1 2 1
# 1211
# 2111
# 122
# 212
# 221

class Solution:
    def climbStairs(self, n: int) -> int:
        @functools.lru_cache(maxsize = 50)
        def fibo(n):
            if n<2:
                return 1
            return fibo(n-1)+fibo(n-2)
        
        return fibo(n)
        