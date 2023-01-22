class Solution:
    def check_pel(self,ss):
        n = len(ss)//2
        for i in range(n):
            if ss[i] != ss[-i-1]:
                return False
        return True
    
    def partition(self, s: str) -> List[List[str]]:
        Q = deque([([],s)])
        ans = []
        while Q:
            curr,resi = Q.popleft()
            if not resi:
                ans.append(curr)
                continue
            
            for i in range(1,len(resi)+1):
                if self.check_pel(resi[:i]):
                    Q.append((curr+[resi[:i]],resi[i:]))
                    
        return ans