class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals,key=lambda x:x[1])
        ans = 0
        endTime = -60000
        for i,j in intervals:
            if i < endTime:
                ans += 1
            else:
                endTime = j  
        return ans
