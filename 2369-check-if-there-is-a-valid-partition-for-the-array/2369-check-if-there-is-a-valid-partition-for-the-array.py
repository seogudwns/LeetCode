class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        @lru_cache(None)
        def chk(m):
            if m == n: return True
            elif n-1 == m: return False
            elif n-2 == m: return nums[-1] == nums[-2]
            return (chk(m+2) if nums[m] == nums[m+1] else False) or (chk(m+3) if nums[m] == nums[m+1] == nums[m+2] or nums[m]+2 == nums[m+1]+1 == nums[m+2] else False)
        
        return chk(0)