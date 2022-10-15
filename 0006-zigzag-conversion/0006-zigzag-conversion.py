class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        ud = 1
        ro = 0
        zzarr = [[] for _ in range(numRows)]
        for i in range(len(s)):
            zzarr[ro].append(s[i])
            if ud == 1:
                ro += 1
            else:
                ro -= 1
            
            if ro == numRows-1:
                ud = 0
            if ro == 0:
                ud = 1
        
        return ''.join([''.join(i) for i in zzarr])
        