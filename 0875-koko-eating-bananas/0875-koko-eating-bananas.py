class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        while l<r:
            mid = (l+r)//2
            if sum(ceil(i/mid) for i in piles)<=h: r = mid
            else: l = mid+1
        
        return l