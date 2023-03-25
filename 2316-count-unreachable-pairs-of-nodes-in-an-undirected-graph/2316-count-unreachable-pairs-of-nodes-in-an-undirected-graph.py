class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        chk,gp,n_comp = [False for _ in range(n)],defaultdict(list),[]
        for i,j in edges:
            gp[i].append(j)
            gp[j].append(i)
        
        for i in range(n):
            if chk[i]: continue
            chk[i] = True
            tmp = 1
            Q = [i]
            while Q:
                curr = Q.pop()
                while gp[curr]:
                    j = gp[curr].pop()
                    if chk[j]: continue
                    Q.append(j)
                    chk[j] = True
                    tmp += 1
            n_comp.append(tmp)
            
        x,ans = sum(n_comp),0
        for i in n_comp:
            x -= i
            ans += x*i
        return ans
        