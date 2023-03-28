class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last = days[-1]
        chk,days = [0 for _ in range(last+1)],set(days)
        o,s,m = costs
        
        for i in range(1,last+1):
            if i not in days: chk[i] = chk[i-1]
            else: chk[i] = min(chk[i-1]+o,chk[max(0,i-7)]+s,chk[max(0,i-30)]+m)
            
        return chk[-1]