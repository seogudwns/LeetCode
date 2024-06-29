class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        self.dic = defaultdict(set)
        for i in range(len(edges)):
            self.dic[edges[i][1]].add(edges[i][0])
            
        ans = [[] for _ in range(n)]
        @lru_cache(None)
        def chk(i):
            tmp,alr = set(),set()
            Q = [i]
            while Q:
                x = Q.pop()
                for i in self.dic[x]:
                    if i not in alr:
                        tmp.add(i)
                        alr.add(i)
                        Q.append(i)
                
            return sorted(tmp)
            
        for i in range(n):
            ans[i] = chk(i)
        
        return ans