class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
#         leng = len(jobDifficulty)
#         if leng < d:
#             return -1
#         elif leng == d:
#             return sum(jobDifficulty)
        
#         dp = [[0 for _ in range(leng)] for i in range(d)]
        
#         @lru_cache(maxsize = None)
#         def maxi(i,j):
#             return max(jobDifficulty[i:j+1]) if i+1<j else jobDifficulty[i]
        
#         num = jobDifficulty[0]
#         for i in range(leng):
#             if num<jobDifficulty[i]:
#                 num = jobDifficult[i]
#             dp[0][i] = num
#         # define first days.
#         # In dp[0], each value of dp[0][i] = max(jobDifficulty[:i])
        
#         for i in range(1,d):
#             for j in range(i,leng):
#                 # print(mini(i,j),i,j)
#                 num = min(dp[i-1][i:j]) if i != j else dp[i-1][i]
#                 # print(num)
#                 dp[i][j] = num+maxi(i,j)
        
#         for i in dp:
#             print(i)
        
#         return min(dp[-1][d:])

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

# ! others code.
        prefixSum = [0]
        for n in jobDifficulty:
            prefixSum.append(prefixSum[-1]+n)
        
        
        maxList = deque([jobDifficulty[-1]])
        for i in range(len(jobDifficulty)-2, -1, -1):
            maxList.appendleft(max(jobDifficulty[i], maxList[0]))
        
		
        memo = {}
        
        @lru_cache(maxsize = None)
        def dp(i, k):
            if (i,k) in memo: return memo[(i,k)]
            if k == 1: return maxList[i]
            if len(jobDifficulty)-i < k: return -1
            if len(jobDifficulty)-i == k: 
                memo[(i,k)] = prefixSum[-1]-prefixSum[i]
                return memo[(i,k)]
            
            ans = float('inf')
            cur_max = jobDifficulty[i]
            
            for j in range(i, len(jobDifficulty)-1):
                cur_max = max(cur_max, jobDifficulty[j])
                res = dp(j+1, k-1)
                if res == -1: break
                ans = min(ans, res+cur_max)
                
            memo[(i,k)] = ans
            return ans
        x = dp(0,d)
        
        dp.cache_clear()
        
        return x