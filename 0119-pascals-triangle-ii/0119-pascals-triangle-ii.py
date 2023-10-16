class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans,nex = [1],[]
        for i in range(rowIndex):
            nex = [1]+[ans[i]+ans[i+1] for i in range(len(ans)-1)]+[1]
            ans,nex = nex,[]
            
        return ans