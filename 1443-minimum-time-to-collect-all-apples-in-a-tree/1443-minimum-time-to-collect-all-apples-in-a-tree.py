class Solution:
    def dfs(self,node,bef):
        child_check = 0
        for i in self.edges[node]:
            if i != bef:
                child_check |= self.dfs(i,node)
        
        if child_check or self.hasApple[node]:
            if node != 0:
                self.res += 2
            return True
        
        return False
    
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.res = 0
        self.hasApple = hasApple
        self.edges = [[] for _ in range(n)]
        
        for i,j in edges:
            self.edges[i].append(j)
            self.edges[j].append(i)
        
        self.dfs(0,0)
        
        return self.res