class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        chk = [0]*n
        def dfs(x):
            if chk[x] in [1,2]: return True # checked case.
            
            chk[x] = 1
            Q = [x]
            while Q:
                y = Q.pop()
                if chk[y] == 1:
                    for i in graph[y]:
                        if chk[i] == 1:
                            return False
                        elif chk[i] == 2:
                            continue
                        chk[i] = 2
                        Q.append(i)
                elif chk[y] == 2:
                    for i in graph[y]:
                        if chk[i] ==2:
                            return False
                        elif chk[i] == 1:
                            continue
                        chk[i] = 1
                        Q.append(i)
                        
            return True
        
        for i in range(n):
            if not dfs(i):
                return False
        
        return True