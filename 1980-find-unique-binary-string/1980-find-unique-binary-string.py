class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        curr,nums = 2**(n+1)-1,sorted(nums)
        while nums:
            if nums[-1] != bin(curr)[-n:]:
                return bin(curr)[-n:]
            nums.pop()
            curr-=1
            
        return "0"*n