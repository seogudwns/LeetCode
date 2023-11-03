class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        curr,idx,leng,bef = target[0],0,len(target),0
        while idx<leng:
            interv = target[idx]-bef
            for i in range(interv-1): 
                ans.append('Push')
                ans.append('Pop')
            ans.append('Push')
            bef = target[idx]
            idx += 1
            
        return ans