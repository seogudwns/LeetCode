from collections import Counter

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        
        last = 0
        dif = float('inf')
        leng = len(nums)
        for i in range(leng-1):
            l,r = i+1,leng-1
            while l<r:
                curr = nums[i]+nums[l]+nums[r]
                if dif>abs(curr-target):
                    dif = abs(curr-target)
                    last = curr
                
                if curr<target:
                    l += 1
                else:
                    r -= 1
                
        return last