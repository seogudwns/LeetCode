class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        ans = [[nums[i]] for i in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(i):
                if not nums[i]%ans[j][-1] and len(ans[i])<len(ans[j])+1:
                    ans[i] = ans[j]+[nums[i]]

        return sorted(ans,key=lambda x: len(x))[-1]
                    
        