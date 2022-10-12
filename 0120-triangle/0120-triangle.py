class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        leng,width = len(triangle),2
        if leng == 1:
            return triangle[0][0]
        
        for i in range(1,leng):
            triangle[i][0] += triangle[i-1][0]
            triangle[i][width-1] += triangle[i-1][width-2]
            for j in range(1,width-1):
                triangle[i][j] += min(triangle[i-1][j-1:j+1])
            # print(triangle[i])
            width += 1
            
        return min(triangle[-1])