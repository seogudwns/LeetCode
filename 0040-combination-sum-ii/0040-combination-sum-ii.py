class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        for i in range(len(candidates)-1,-1,-1):
            if candidates[i]>target:
                del candidates[i]
                
        candidates = sorted(candidates,reverse = True)
        leng = len(candidates)
        res = []
        def bt(start,target,lst):
            if target<0:
                return
            elif target == 0:
                lst = sorted(lst)
                if lst not in res:
                    res.append(lst)
                return
            
            for i in range(start,leng):                    
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                bt(i+1,target-candidates[i],lst+[candidates[i]])
            
            return
        bt(0,target,[])
        return res