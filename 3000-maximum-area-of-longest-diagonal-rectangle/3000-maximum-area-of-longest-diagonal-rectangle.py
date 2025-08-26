class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxi,ans = 0,0
        for x,y in dimensions:
            sq = x**2+y**2
            if maxi<sq:
                maxi = sq
                ans = x*y
            elif maxi == sq:
                ans = max(ans,x*y)
        
        return ans