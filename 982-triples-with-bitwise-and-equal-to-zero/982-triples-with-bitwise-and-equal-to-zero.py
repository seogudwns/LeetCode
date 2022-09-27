from collections import Counter

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        
        result = 0
        leng = len(nums)
        X = Counter(i&j for i in nums for j in nums)
        # print(X)
        for i in range(leng):
            for j in X:
                if nums[i]&j == 0:
                    result += X[j]
                        
        return result