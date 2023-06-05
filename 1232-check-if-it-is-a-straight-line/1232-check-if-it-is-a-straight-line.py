class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0,y0 = coordinates[0]
        x1,y1 = coordinates[1]
        
        interv_x,interv_y = x1-x0,y1-y0
        for i in range(2,len(coordinates)):
            x2,y2 = coordinates[i]
            if interv_x*(y2-y0) != interv_y*(x2-x0): return False
        
        return True