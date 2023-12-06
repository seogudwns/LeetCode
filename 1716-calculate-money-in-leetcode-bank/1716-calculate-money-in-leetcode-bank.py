class Solution:
    def totalMoney(self, n: int) -> int:
        x,y = divmod(n,7)
        return ((x+7)*x)//2*7 + ((y+1)*y)//2 + x*y
        # return (((n//7)+7)*(n//7))//2*7 + (((n%7)+1)*(n%7))//2+((n//7))*(n%7)