class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[[]]]
        for n in range(1,len(nums)):
            res.append([list(i) for i in combinations(nums,n)])
        
        res.append([nums])
        return sum(res,[])