class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return sorted(x:=Counter(nums),key = lambda y:-x[y])[:k]
        