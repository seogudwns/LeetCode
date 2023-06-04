class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        chk,ans,gp = [False]*n,0,dict()
        
        for i in range(n):
            tmp = set()
            for j in range(n):
                if isConnected[i][j]:
                    tmp.add(j)
            gp[i] = tmp
        
        for i in range(n):
            if not chk[i]:
                ans += 1
                Q = {i}
                while Q:
                    x = Q.pop()
                    if chk[x]: continue
                    chk[x] = True
                    Q = Q.union(gp[x])
                    
        return ans