class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n,rQ,dQ = len(senate),deque(),deque()
        
        for i,c in enumerate(senate):
            if c == "R": rQ.append(i)
            else: dQ.append(i)
                
        while dQ and rQ:
            d,r = dQ.popleft(), rQ.popleft()
            if d < r: dQ.append(d+n)
            else: rQ.append(r+n)
        return "Radiant" if rQ else "Dire"