class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        # l0 ~ l2 : 0 Absent with 0~2 last Late.
        # l3 ~ l5 : 1 Absent with 0~2 last Late.
        l0,l1,l2 = [0,1],[0,1],[0,0]
        l3,l4,l5 = [0,1],[0,0],[0,0]
        # if n < 3:
        #     return n**2 - 1
        for i in range(n-1):
            # No Absent.
            l0.append((l0[-1]+l1[-1]+l2[-1])%MOD) # last time, Present.
            l2.append(l1[-1]) # before last time, Late. 
            l1.append(l0[-2]) # before last time, Present.
            
            l3.append((l3[-1]+l0[-2]+l1[-2]+l2[-2]+l4[-1]+l5[-1])%MOD) # last time, Present or it does not have Absent, last time, Absent. 
            
            # already 1 Absent.
            l5.append(l4[-1]) # before last time, Late.
            l4.append(l3[-2]) # before last time, Present or Late.
        
        return (l0[-1]+l1[-1]+l2[-1]+l3[-1]+l4[-1]+l5[-1])%MOD