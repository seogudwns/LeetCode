class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return bin(reduce(lambda curr,x: curr^x, nums,k)).count("1")