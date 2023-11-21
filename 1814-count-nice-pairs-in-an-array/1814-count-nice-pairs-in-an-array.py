class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        return sum(((i*(i-1))//2)%(10**9+7) for i in Counter([i-int(str(i)[::-1]) for i in nums]).values())%(10**9+7)
        