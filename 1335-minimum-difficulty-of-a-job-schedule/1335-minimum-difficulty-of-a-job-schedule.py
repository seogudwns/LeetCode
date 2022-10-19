class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        leng = len(jobDifficulty)
        if leng < d:
            return -1
        elif leng == d:
            return sum(jobDifficulty)
        elif d == 1:
            return max(jobDifficulty)
        
        dp = [[3000000 for _ in range(leng)] for i in range(d)]
        
        @lru_cache(maxsize = None)
        def maxi(i,j=leng-1):
            return max(jobDifficulty[i:j+1]) if i<j else jobDifficulty[i]
        
        num = jobDifficulty[0]
        for i in range(leng):
            if num<jobDifficulty[i]:
                num = jobDifficulty[i]
            dp[0][i] = num
        # define first days.
        # In dp[0], each value of dp[0][i] = max(jobDifficulty[:i])
        
        for i in range(1,d-1):
            for j in range(i,leng):
                for k in range(i-1,j):
                    tmp = dp[i-1][k]+maxi(k+1,j)
                    if dp[i][j] > tmp:
                        dp[i][j] = tmp
                        
        for j in range(d-1,leng):
            for k in range(d-2,j):
                tmp = dp[-2][k]+maxi(k+1)
                if dp[-1][j] > tmp:
                    dp[-1][j] = tmp
        
        # for i in dp:
        #     print(i)
        maxi.cache_clear()
        
        return min(dp[-1][d:])

# ex1. 654321, 2
# [6,6,6,6,6,6]
# [0,11,10,9,8,7]

# ex2. 717171, 3
# [7,7,7,7,7,7]
# [0,14,14,14,14,8]
# [0,0,21,21,21,21,15]

# ex1. 654321, 3
# [6,6,6,6,6,6]
# [0,11,10,9,8,7]
# [0,0,15,13,11,9]

#ex4. [380,302,102,681,863,676,243,671,651,612,162,561,394,856,601,30,6,257,921,405,716,126,158,476,889,699,668,930,139,164,641,801,480,756,797,915,275,709,161,358,461,938,914,557,121,964,315], 10
# --> 3807

# ! others code.
#         prefixSum = [0]
#         for n in jobDifficulty:
#             prefixSum.append(prefixSum[-1]+n)
        
        
#         maxList = deque([jobDifficulty[-1]])
#         for i in range(len(jobDifficulty)-2, -1, -1):
#             maxList.appendleft(max(jobDifficulty[i], maxList[0]))
        
		
#         memo = {}
        
#         @lru_cache(maxsize = None)
#         def dp(i, k):
#             if (i,k) in memo: return memo[(i,k)]
#             if k == 1: return maxList[i]
#             if len(jobDifficulty)-i < k: return -1
#             if len(jobDifficulty)-i == k: 
#                 memo[(i,k)] = prefixSum[-1]-prefixSum[i]
#                 return memo[(i,k)]
            
#             ans = float('inf')
#             cur_max = jobDifficulty[i]
            
#             for j in range(i, len(jobDifficulty)-1):
#                 cur_max = max(cur_max, jobDifficulty[j])
#                 res = dp(j+1, k-1)
#                 if res == -1: break
#                 ans = min(ans, res+cur_max)
                
#             memo[(i,k)] = ans
#             return ans
#         x = dp(0,d)

#         dp.cache_clear()
        
#         return x