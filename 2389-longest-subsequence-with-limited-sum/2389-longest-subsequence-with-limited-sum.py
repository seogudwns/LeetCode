class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums = sorted(nums)
        pref = list(accumulate(nums))
        return [bisect_right(pref,q) for q in queries]