class Solution:
    def bfs(self,node,bef):
        res = []
        if not self.tree[node]:
            # print('last',node,1)
            return 1
        
        for i in self.tree[node]:
            # print(i,self.s[i],node,self.s[node])
            child = self.bfs(i,node)
            if self.s[i] != self.s[node]:
                heapq.heappush(res,-child)
            else:
                heapq.heappush(res, 0)
        
        tmp = -heapq.heappop(res)+1
        
        # print(node,bef,res,tmp)
        self.ans.add(tmp)
        if not res:
            # print('last',node,tmp)
            return tmp
        
        self.ans.add(tmp-heapq.heappop(res))
        print('last',node,tmp)
        return tmp
    
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        if n == 1:
            return 1
        
        self.s = s
        self.tree = [[] for _ in range(n)]
        for i in range(1,n):
            self.tree[parent[i]].append(i)
        # print(self.tree)
        self.ans = {1}
        self.bfs(0,0)
        
        # print(self.ans)
        return max(self.ans)