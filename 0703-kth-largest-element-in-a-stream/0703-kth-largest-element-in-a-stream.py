class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums,self.k = sorted(nums),k

    def add(self, val: int) -> int:
        if len(self.nums)<self.k or self.nums[0]<val: insort_right(self.nums,val)
        return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)