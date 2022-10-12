class Solution:
    def rob(self, nums: List[int]) -> int:
        result = [0,0]
        for m in nums:
            result.append(max(result[-2]+m,result[-1]))
        return result[-1]