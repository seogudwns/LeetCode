class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = Counter(nums)
        leng = len(nums)/2
        for i in x:
            if x[i]>leng:
                return i
        