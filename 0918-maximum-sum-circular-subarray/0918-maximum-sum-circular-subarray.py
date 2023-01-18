class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        MinS,MaxS = 0,nums[0]
        Min,Max = 0,nums[0]
        S = 0
        for i in nums:
            S += i
            MinS,MaxS = min(S-Max,MinS),max(S-Min,MaxS)
            Min,Max = min(Min,S),max(Max,S)
        
        return max(MaxS,S-MinS)
            