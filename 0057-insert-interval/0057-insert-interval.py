class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        l,h = newInterval
        for i,j in intervals:
            if j<l or h<i:
                res.append([i,j])
            else:
                l,h = min(l,i),max(h,j)
            
        res.append([l,h])
        
        return sorted(res)