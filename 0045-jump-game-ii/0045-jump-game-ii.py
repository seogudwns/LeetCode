class Solution:
    def jump(self, nums: List[int]) -> int:
        leng,res = len(nums),[-1 for _ in nums]

        res[0] = 0
        for i in range(leng-1):
            curr = res[i]
            for j in range(i,min(leng,1+i+nums[i])):
                if res[j] != -1: continue
                res[j] = curr + 1
            if res[-1] != -1: return res[-1]
            
        return res[-1]