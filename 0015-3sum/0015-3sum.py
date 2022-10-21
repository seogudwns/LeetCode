class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res=[]
        nums = sorted(nums)
        
        for i in range(n-2):
            curr = nums[i]
            if i == 0 or curr != nums[i-1]:
                j = i + 1
                k = n-1
                while j < k:
                    sum = curr + nums[j] + nums[k]
                    if sum == 0:
                        res.append([curr, nums[j], nums[k]])
                        
                        while j < k and nums[j] == nums[j+1]:
                            j+=1
                        while j < k and nums[k] == nums[k-1]:
                            k-=1
                        j+=1 
                        k-=1

                    elif sum < 0: 
                        j += 1
                    else: 
                        k -= 1
                        
        return res
        
        
#         ! TLE.. why???
#         nums = sorted(nums)
#         n = len(nums)
        
#         start,mid = 0,1
#         res = []
#         while start != n-2:
#             tmp = -(nums[start]+nums[mid])
#             for i in range(mid+1,n):
#                 if nums[i] >= tmp:
#                     if nums[i] == tmp:
#                         res.append([nums[start],nums[mid],nums[i]])
#                     break
                
            
#             if mid != n-1:
#                 mid += 1
#                 while nums[mid-1] == nums[mid]:
#                     if mid == n-1:
#                         break
#                     mid += 1
#             else:
#                 start+=1
#                 while nums[start-1] == nums[start]:
#                     if start == n-2:
#                         break
#                     start += 1
#                 mid = start+1
        
#         return res
                