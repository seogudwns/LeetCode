class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        leng = len(s)
        def add_res(s,sp,curr):
            if len(sp)>4:
                return
            if len(sp) == 4 and curr == leng:
                res.append('.'.join(sp))
                return
            
            for i in range(curr+1,min(curr+4,leng+1)):
                tmp = s[curr:i]
                if str(int(tmp)) != tmp:
                    continue
                if int(tmp)<256:
                    add_res(s,sp+[tmp],i)
            
        add_res(s,[],0)
        
        return res