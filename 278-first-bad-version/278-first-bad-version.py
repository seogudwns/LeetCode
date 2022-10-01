# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while True:
            mid = (left+right)//2
            
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1