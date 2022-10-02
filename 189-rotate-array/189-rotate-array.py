class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        leng = len(nums)
        if k == 0 or k == leng or leng <= 1:
            return nums
        
        k = k%leng
        nums[:] = nums[-k:] + nums[:leng-k]