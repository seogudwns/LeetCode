class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        leng = len(s)
        def add_res(s,sp,curr):
            if len(sp)>4:
                return
            if len(sp) == 4 and curr == leng:
                sp = [0]+sp
                res.append('.'.join([s[sp[i]:sp[i+1]] for i in range(4)]))
                return
            
            for i in range(curr+1,min(curr+4,leng+1)):
                tmp = s[curr:i]
                if str(int(tmp)) != tmp:
                    continue
                if int(tmp)<256:
                    add_res(s,sp+[i],i)
            
        add_res(s,[],0)
        
        return res