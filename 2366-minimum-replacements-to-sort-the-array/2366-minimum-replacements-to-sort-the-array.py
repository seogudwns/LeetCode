class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>nums[i+1]:
                x,y = divmod(nums[i],nums[i+1])
                ans += x-1 if not y else x
                nums[i] = nums[i]//(x+1) if y else nums[i]//x
        
        return ans