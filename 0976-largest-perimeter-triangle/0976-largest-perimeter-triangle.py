class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums)<3:
            return 0
        
        nums = sorted(nums)
        leng = len(nums)-1
        
        while leng != 1:
            if nums[leng-2]+nums[leng-1]>nums[leng]:
                return sum(nums[leng-2:leng+1])
            leng -= 1
        
        return 0