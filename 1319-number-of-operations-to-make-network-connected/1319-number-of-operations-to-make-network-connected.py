class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        N = len(connections)
        if n-1>N: return -1
        
        check,nbr,comp = [False for _ in range(n)],[[] for _ in range(n)],0
        for i,j in connections:
            nbr[i].append(j)
            nbr[j].append(i)
        
        for i in range(n):
            if check[i]: continue
            
            comp += 1
            tmp = [i]
            while tmp:
                x = tmp.pop()
                if check[x]: continue
                check[x] = True

                for j in nbr[x]: tmp.append(j)
            
        return comp-1