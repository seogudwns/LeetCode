class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r = 0,len(arr)-1
        if arr[0]>arr[l]: return 0
        if arr[r]>arr[r-1]: return r+1
        while l<r:
            mid = (l+r)//2
            if arr[mid-1]<arr[mid]<arr[mid+1]: l = mid+1
            elif arr[mid-1]>arr[mid]>arr[mid+1]: r = mid
            else: return mid
        
        return r
                