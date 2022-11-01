class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # print(2**31 - 1) # == 2147483648 - 1
        if abs(dividend)<abs(divisor):
            return 0
        
        if dividend*divisor>0:
            return min(2147483647,abs(dividend)//abs(divisor))
        
        return -(min(2147483648,abs(dividend)//abs(divisor)))
# 이건 너무 억지다...