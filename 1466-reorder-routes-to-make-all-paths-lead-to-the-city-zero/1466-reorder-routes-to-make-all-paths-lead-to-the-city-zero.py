class Solution:
    def dfs(self,bef,curr):
        for i,chk in self.roads[curr]:
            if i == bef: continue
            if not chk: self.cnt += 1
            self.dfs(curr,i)
        return
    
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.roads,self.cnt = defaultdict(list),0
        for i,j in connections:
            self.roads[i].append((j,0))
            self.roads[j].append((i,1))
        
        self.dfs(0,0)    
        return self.cnt