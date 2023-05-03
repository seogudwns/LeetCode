class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [sorted(set(nums1)-set(nums2)),sorted(set(nums2)-set(nums1))]