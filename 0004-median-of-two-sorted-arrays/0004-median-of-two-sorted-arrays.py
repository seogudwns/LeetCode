class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return sorted(nums1+nums2)[(len(nums1)+len(nums2))//2] if (len(nums1)+len(nums2))%2 else (sum(sorted(nums1+nums2)[(len(nums1)+len(nums2))//2-1:(len(nums1)+len(nums2))//2+1]))/2