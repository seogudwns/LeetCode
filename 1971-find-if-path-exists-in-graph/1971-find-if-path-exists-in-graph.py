class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1: return True
        
        gp,chk = defaultdict(set),[False for _ in range(n)]
        for i,j in edges:
            gp[i].add(j)
            gp[j].add(i)
        
        Q = [source]
        while Q:
            curr = Q.pop()
            chk[curr] = True
            for nex in gp[curr]:
                if nex == destination: return True
                elif not chk[nex]:
                    Q.append(nex)
        
        return False