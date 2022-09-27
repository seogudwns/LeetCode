class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = sorted(nums1+nums2)
        leng = len(x)
        if leng%2:
            return x[leng//2]
        else:
            return (x[leng//2]+x[leng//2-1])/2