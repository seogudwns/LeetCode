class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        points = sorted(points)
        slope, M = defaultdict(int), 0

        for i, (x1, y1) in enumerate(points):
            slope.clear()
            
            for x2, y2 in points[i + 1:]:
                dx, dy = x2 - x1, y2 - y1
                G = gcd(dx, dy)                 
                
                m = (dx//G,dy//G)
                
                slope[m] += 1
                if slope[m] > M: M = slope[m]
    
        return M + 1