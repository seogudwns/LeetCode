class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = Counter(nums)
        return sorted(x,key = lambda y:-x[y])[:k]
        