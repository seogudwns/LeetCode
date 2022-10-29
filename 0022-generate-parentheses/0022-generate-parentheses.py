class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l,r = n,n
        
        res = []
        Q = deque([("",l,r,0)])
        while Q:
            arr,l,r,f = Q.popleft()
            if l == 0 and r == 0:
                res.append(arr)
                continue
            
            if f == 0:
                if l>0:
                    Q.append((arr+'(',l-1,r,1))
            else:
                if l>0:
                    Q.append((arr+'(',l-1,r,f+1))
                if r>0:
                    Q.append((arr+')',l,r-1,f-1))
                
        return res
            
                
        
            