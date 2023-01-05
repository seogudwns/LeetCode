class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points,key=lambda x: (x[1],x[0]))
        print(points)
        get = [points[0][1]]
        for i,j in points:
            if get[-1]<i:
                get.append(j)
        
        return len(get)