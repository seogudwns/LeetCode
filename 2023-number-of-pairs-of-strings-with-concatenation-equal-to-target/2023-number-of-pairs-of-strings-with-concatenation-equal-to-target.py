class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j: continue
                if (nums[i][0] == target[0] and nums[j][-1] == target[-1] and nums[i]+nums[j]==target): 
                    ans+=1
        
        return ans
        