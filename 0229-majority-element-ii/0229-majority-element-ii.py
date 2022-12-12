class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x = Counter(nums)
        leng = len(nums)//3
        return [i for i in x if x[i]>leng]
        