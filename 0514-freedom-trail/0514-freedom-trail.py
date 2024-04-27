class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n,m = len(ring),len(key)
        def calc(lst,curr): return min(lst[i]+min(abs(curr-i),n-abs(curr-i)) for i in range(n) if lst[i] != 0)

        dp = [[0]*n for _ in range(m)]
        for i in range(n):
            if ring[i] == key[0]:
                dp[0][i] = 1+min(i,n-i)

        for i in range(1,m):
            for j in range(n):
                if ring[j] == key[i]:
                    dp[i][j] = 1+calc(dp[i-1],j)
        
        return min(i for i in dp[-1] if i != 0)