class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n,m = len(nums),len(queries)
        res = [0 for _ in range(m)]
        
        nums = [0]+sorted(nums)
        for i in range(1,n+1):
            nums[i] += nums[i-1]
        
        for i in range(m):
            curr = queries[i]
            for j in range(n):
                if nums[j]<=curr<nums[j+1]:
                    res[i] = j
                    break
            else:
                res[i] = n
        return res