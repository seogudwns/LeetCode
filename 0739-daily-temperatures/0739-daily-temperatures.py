class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        leng = len(temperatures)
        dp = [0]*len(temperatures)
        check = [[] for _ in range(101)]
        consider = set() # check를 하나씩 다 도는게 싫어서 씀.
        for i in range(leng):
            temp = temperatures[i]
            for j in list(consider):
                if j>=temp:
                    continue
                if check[j]:
                    for k in check[j]:
                        dp[k] = i-k
                    check[j].clear()
                    consider.discard(j)
            check[temp].append(i)
            consider.add(temp)
        
        return dp