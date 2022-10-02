class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.????????
        """
        # print(nums,k)
        leng = len(nums)
        if leng <= 1 or k == 0 or k == leng:
            return nums
        k = k%leng
        nums[:] = nums[-k:] + nums[:leng-k]
        # print(nums)