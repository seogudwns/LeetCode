class Solution:
    def reverse(self, x: int) -> int:
        y = 0
        if x<0:
            y = -int(str(abs(x))[::-1])
        else:
            y = int(str(x)[::-1]) 

        if -2**31-1 < y < 2**31:
            return y
        
        return 0
