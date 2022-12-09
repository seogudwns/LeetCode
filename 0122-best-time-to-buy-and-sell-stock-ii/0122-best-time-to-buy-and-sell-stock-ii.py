class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lar = 3*10**4+1
        res = 0
        
        curr = lar
        for i in prices:
            if i < curr:
                curr = i
            elif i > curr:
                res += i-curr
                curr = i
        
        return res
        