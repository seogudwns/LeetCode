class Solution:
    def canJump(self, nums: List[int]) -> bool:
        bef,curr = 0,nums[0]+1
        n = len(nums)
        while True:
            # print(bef,curr)
            if curr>=n:
                return True
            for i in range(bef,curr):
                if i+nums[i]+1>curr:
                    bef,curr = i,i+nums[i]+1
                    break
            else:
                return False