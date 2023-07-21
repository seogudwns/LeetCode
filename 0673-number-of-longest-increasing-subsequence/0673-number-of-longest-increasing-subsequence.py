class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

#         겁나 빠른 TLE
#         cnt = {i:[] for i in range(len(nums))}
#         cnt[0].append(nums[0])
#         for i in range(1,len(nums)):
#             curr = nums[i]
#             for j in range(i):
#                 for k in cnt[j]:
#                     if k<curr:
#                         cnt[j+1].append(curr)
#             cnt[0].append(curr)
        
#         N = len(nums)-1
#         while not cnt[N]:
#             del cnt[N]
#             N -= 1
            
#         return len(cnt[N])

        n=len(nums)
        dp=[1]*n
        count=[1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    if 1+dp[j]>dp[i]:
                        dp[i]=dp[j]+1

                        count[i]=count[j]

                    elif dp[j]+1==dp[i]:
                        count[i]+=count[j]

        longest_len=max(dp)
        return sum(count[i] for i in range(n) if dp[i]==longest_len)