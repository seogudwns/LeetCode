class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lens = len(s)
        if lens < len(t):
            return ""
        
        leng = lens+1
        res = lens+1
        cntt = Counter(t)
        distinct = len(cntt)
        i,j = 0,0
        li,lj = -1,-1
        
        while j < lens:
            sj = s[j]
            if sj in cntt:
                cntt[sj] -= 1
                if cntt[sj] == 0:
                    distinct -= 1
            
            while distinct == 0:
                if j-i+1 < res:
                    res = j-i+1
                    li,lj = i,j
                    
                si = s[i]
                if si in cntt:
                    cntt[si] += 1
                    if cntt[si] == 1:
                        distinct += 1
                
                i += 1
            
            j += 1
        
        return s[li:lj+1]