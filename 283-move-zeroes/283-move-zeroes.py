class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_cnt = nums.count(0)
        order = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[order] = nums[i]
                order+=1
        
        if zero_cnt:
            nums[-zero_cnt:] = [0]*zero_cnt