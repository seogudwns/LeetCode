class Solution:
    def integerBreak(self, n: int) -> int:
        ans = n-1
        for i in range(2,n//2+1):
            x,y = divmod(n,i)
            ans = max(ans,(x+1)**y*x**(i-y))
        
        return ans