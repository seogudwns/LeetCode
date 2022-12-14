class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = Counter(nums)
        res = []
        for i in x:
            res.extend([i]*min(2,x[i]))
        
        nums[:] = res