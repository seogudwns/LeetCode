class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1,numRows):
            tmp = [0]+res[-1]+[0]
            res.append([tmp[j]+tmp[j+1] for j in range(i+1)])
        
        return res