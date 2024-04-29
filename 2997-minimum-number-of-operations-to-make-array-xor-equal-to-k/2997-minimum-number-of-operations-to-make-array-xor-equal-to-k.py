class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        curr = k
        for i in nums:
            curr ^= i
        
        return bin(curr).count("1")