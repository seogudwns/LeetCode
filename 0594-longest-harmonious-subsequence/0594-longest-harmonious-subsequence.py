class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums = Counter(nums)
        ans,curr = 0,-1
        for i in sorted(nums):
            if i-curr == 1:
                ans = max(ans,nums[curr]+nums[i])
            curr = i
        
        return ans