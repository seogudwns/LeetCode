class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        return sorted([[i,j] for i in arr for j in arr if i < j],key=lambda x: x[0]/x[1])[k-1]