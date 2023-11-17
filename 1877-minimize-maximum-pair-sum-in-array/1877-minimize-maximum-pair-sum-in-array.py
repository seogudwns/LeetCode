class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = deque(sorted(nums))
        ans = 0
        while nums:
            ans = max(ans,nums.pop()+nums.popleft())
        
        return ans