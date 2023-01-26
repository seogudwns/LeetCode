class Solution:
    def bfs(self,curr,ks,char):
        if self.check[ks][curr]<=char or self.ans < char: return
        self.check[ks][curr] = char
        
        if curr == self.dst or ks == self.k:
            if curr == self.dst: self.ans = min(self.ans,char)
            return
        
        for i in self.mv[curr]:
            self.bfs(i,ks+1,char+self.charges[(curr,i)])
        
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        self.charges,self.mv,self.ans,self.k,self.dst = defaultdict(int),defaultdict(set),10**6+1,k,dst

        for i,j,char in flights:
            self.charges[(i,j)] = char
            self.mv[i].add(j)
        self.check = [[float('inf') for _ in range(n)] for _ in range(k+1)]
        
        self.bfs(src,-1,0)
        
        return self.ans if self.ans != 10**6+1 else -1