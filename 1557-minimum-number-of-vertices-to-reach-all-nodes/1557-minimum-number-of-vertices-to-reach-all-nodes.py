class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = {i for i in range(n)}
        for i,j in edges: ans.discard(j)
        return ans
    
    
        # ans,nex = set(),set()
        # for i,j in edges:
        #     ans.add(i)
        #     nex.add(j)
        # return sorted(ans-nex)