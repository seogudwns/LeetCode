class Solution:
    def rob(self, nums: List[int]) -> int:
        p0, p1 = 0, 0
        for m in nums:
            p1, p0 = max(p0 + m, p1), p1
            print(p1,p0)
        return p1