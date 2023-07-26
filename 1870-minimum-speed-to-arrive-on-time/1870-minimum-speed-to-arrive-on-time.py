class Solution:
    def needtime(self,dis,spd):
        return ceil(dis/spd)
    
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist)-1>=hour: return -1
        l,r,n = 1,10**7,len(dist)-1
        ans = r
        
        while l<r:
            mid = (l+r)//2
            chk = sum(self.needtime(dist[i],mid) for i in range(n))+dist[-1]/mid
            if chk<=hour:
                ans = min(ans,mid)
                r = mid
            else:
                l = mid+1
        return ans