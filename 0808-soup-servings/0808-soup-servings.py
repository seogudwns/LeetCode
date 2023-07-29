class Solution:
    def soupServings(self, n: int) -> float:
        @lru_cache(None)
        def dfs(a,b):
            if a<=0:
                if b<=0: return 0.5
                return 1
            elif b<=0: return 0
            return (dfs(a-100,b)+dfs(a-75,b-25)+dfs(a-50,b-50)+dfs(a-25,b-75))/4
        
        return dfs(n,n) if n<4300 else 1