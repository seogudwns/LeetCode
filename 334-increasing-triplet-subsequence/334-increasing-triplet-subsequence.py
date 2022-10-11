class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        X = Counter(nums)
        if len(X.keys()) < 3 or nums == sorted(nums,reverse=True):
            return False
        
        # basic code..
        n = len(nums)
        for i in range(n-2):
            for j in range(i+1,n-1):
                if nums[i]<nums[j]:
                    for k in range(j+1,n):
                        if nums[j]<nums[k]:
                            return True
        return False