class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        leng = len(temperatures)
        dp = [0]*len(temperatures)
        check = [[] for _ in range(101)] # key:val = temp:idx
        for i in range(leng):
            temp = temperatures[i]
            for j in range(1,temp):
                if check[j]:
                    for k in check[j]:
                        dp[k] = i-k
                    check[j].clear()
            check[temp].append(i)
        
        return dp