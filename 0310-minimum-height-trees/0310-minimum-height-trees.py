class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        
        gp = defaultdict(set)
        deg = [0 for _ in range(n)]
        for i,j in edges:
            gp[i].add(j)
            gp[j].add(i)
            deg[i] += 1
            deg[j] += 1
        
        leaves = [i for i in range(n) if deg[i] == 1]
        nex = []
        
        while n>2:
            n -= len(leaves)
            while leaves:
                leaf = leaves.pop()
                par = gp[leaf].pop()
                deg[par] -= 1
                gp[par].discard(leaf)
                if len(gp[par]) == 1:
                    nex.append(par)
            
            leaves,nex = nex,[]
        
        return leaves