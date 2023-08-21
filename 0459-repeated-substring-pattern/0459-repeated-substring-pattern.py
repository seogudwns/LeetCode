class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1,n//2+1):
            x,y = divmod(n,i)
            if not y and s[:i]*x == s: return True
            
        return False