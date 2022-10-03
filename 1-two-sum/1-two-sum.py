class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        leng = len(nums)
        for i in range(leng):
            tmp = target-nums[i]
            for j in range(i+1,leng):
                if tmp == nums[j]:
                    return [i,j]