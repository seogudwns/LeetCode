class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = Counter(nums)
        ans = [0]*len(nums)
        
        if 0 in x:
            if x[0]==1:
                y = 1
                for i in x:
                    if i != 0:
                        if i != 1:
                            y *= i**x[i]
                    
                ans[nums.index(0)] = y
        else:
            y = 1
            for i in x:
                if i != 1:
                    y *= i**x[i]
                    
            for i in range(len(nums)):
                ans[i] = y//nums[i]
            
        return ans