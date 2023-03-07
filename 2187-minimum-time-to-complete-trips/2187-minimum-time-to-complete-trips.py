class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l,r = 1,totalTrips*min(time)
        while l<r:
            mid = (l+r)//2
            if sum(mid//i for i in time) >= totalTrips: r = mid
            else: l = mid+1
                
        return l