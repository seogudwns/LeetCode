class Solution:
    def totalMoney(self, n: int) -> int:
        return (((n//7)+7)*(n//7))//2*7 + (((n%7)+1)*(n%7))//2+((n//7))*(n%7)