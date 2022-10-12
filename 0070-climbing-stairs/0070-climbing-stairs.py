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
        if n<2:
            return 1
        
        lst = [1,1]
        for _ in range(n-1):
            lst.append(lst[-1]+lst[-2])
        
        return lst[-1]
        