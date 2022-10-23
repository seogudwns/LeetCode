class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        nums = Counter(nums)
        f,n = -1,-1
        for i in range(1,leng+1):
            if i not in nums:
                n = i
            elif nums[i] == 2:
                f = i
            
        return [f,n]