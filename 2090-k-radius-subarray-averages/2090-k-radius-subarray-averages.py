# class Solution:
#     def getAverages(self, nums: List[int], k: int) -> List[int]:
#         # return [-1 if i<k or i>len(nums)-k-1 else sum(nums[i-k:i+k+1])//(2*k+1) for i in range(len(nums))] #TLE..
        
#         ans,cnt,chk,n = [],0,True,len(nums)
#         for i in range(n):
#             cnt += nums[i]
#             if i>=2*k+1: cnt -= nums[i-2*k-1]
#             ans.append(-1 if i<k or i>n-k-1 else cnt//(2*k+1))
#             print(nums[max(i-2*k-1,0):i+1],cnt)
        
#         return ans

class Solution(object):
    def getAverages(self, nums, k):
            n = len(nums)
            ans = [-1] * n
            length = 2 * k + 1
            if length > n:
                return ans

            total_sum = sum(nums[:length])
            ans[k] = total_sum // length
            for last in range(length, n):
                total_sum += nums[last] - nums[last-length]
                ans[last - k] = total_sum // length

            return ans
        