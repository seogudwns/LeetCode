class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l = max(candies)
        return [False if i+extraCandies<l else True for i in candies]