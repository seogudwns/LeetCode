class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = sorted(set(nums))
        ans,curr,bef = 0,1,10**9
        for i in nums:
            if i-1 != bef:
                ans = max(ans,curr)
                curr = 1
            else: curr += 1
            bef = i
        return max(ans,curr)