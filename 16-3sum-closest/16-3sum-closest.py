from collections import Counter

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        # print(nums)
        last = 0
        dif = float('inf')
        leng = len(nums)
        
        for i in range(leng-2):
            l,r = i+1,leng-1
            while l<r:
                curr = nums[i]+nums[l]+nums[r]
                if abs(curr-target)<dif:
                    dif = abs(curr-target)
                    last = curr
                
                if curr<target:
                    l += 1
                else:
                    r -= 1
                    
            if dif == 0:
                return target
                
        return last

#         nums = sorted(nums)
#         last = 0
#         dif = float('inf')
#         leng = len(nums)
        
#         for i in range(leng-2):
#             l,r = i+1,leng-1
#             while l<r:
#                 curr = nums[i]+nums[l]+nums[r]
#                 if abs(curr-target)<dif:
#                     dif = abs(curr-target)
#                     last = curr
                
#                 if curr<target:
#                     l += 1
#                 else:
#                     r -= 1
                
#         return last