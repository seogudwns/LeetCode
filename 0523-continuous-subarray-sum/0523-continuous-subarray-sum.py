class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        num,dic = 0,dict()
        for i in range(len(nums)):
            num = (num + nums[i])%k
            if i>0 and num == 0:
                return True
            
            if num in dic:
                if i-dic[num]>1:
                    return True
            else:
                dic[num] = i
        
        return False
        
#         # 누적합.. TLE.. 뭐지??
#         leng = len(nums)
#         nums = [0]+nums
#         for i in range(leng):
#             nums[i+1] += nums[i]
        
#         for i in range(leng-1):
#             for j in range(i+2,leng+1):
#                 if not (nums[j]-nums[i])%k:
#                     return True
        
#         return False
        
#         # init code. TLE
#         leng = len(nums)
#         for i in range(leng-1):
#             tmp = nums[i]
#             for j in range(i+1,leng):
#                 tmp += nums[j]
#                 if not tmp%k: 
#                     print(i,j)
#                     return True
        
#         return False