class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        l, r = k, k
        min_val = nums[k]
        max_score = min_val
        
        while l > 0 or r < len(nums) - 1:
            if l == 0 or (r < len(nums) - 1 and nums[r + 1] > nums[l - 1]): r += 1
            else: l -= 1
            min_val = min(min_val, nums[l], nums[r])
            max_score = max(max_score, min_val * (r - l + 1))
            
        return max_score